#! /usr/bin/env python3
"""
@author  : MG
@Time    : 2021/2/1 9:32
@File    : export_strategy_setting.py
@contact : mmmaaaggg@163.com
@desc    : 用于导出 策略设置 生成 json 文件，该文件用于覆盖
.vntrader\cta_strategy_setting.json
.vntrader\portfolio_strategy_setting.json
文件
"""
import json
import logging
import os
from collections import OrderedDict
from datetime import date
from typing import List, Union, Optional

from ibats_utils.mess import date_2_str

from vnpy_extra.constants import INSTRUMENT_TYPE_SUBSCRIPTION_DIC, STOP_OPENING_POS_PARAM, BASE_POSITION
from vnpy_extra.db.orm import AccountStrategyMapping, SymbolsInfo, set_account, StrategyBacktestStats, get_account
from vnpy_extra.utils.symbol import get_instrument_type, get_main_contract

logger = logging.getLogger(__name__)


def generate_setting_dic(vt_symbols: Union[str, list], strategy_class_name: str,
                         strategy_settings: dict) -> (dict, bool):
    """生成 cta/portfolio setting dict数据"""
    if isinstance(vt_symbols, str):
        vt_symbols = vt_symbols.split('_')

    if len(vt_symbols) == 1:
        is_cta = True
        setting_dic = OrderedDict()
        setting_dic["class_name"] = strategy_class_name
        setting_dic["vt_symbol"] = get_vt_symbols_4_subscription(vt_symbols[0])
        setting_dic["setting"] = settings = OrderedDict()
        settings['class_name'] = strategy_class_name
        for k, v in strategy_settings.items():
            settings[k] = v
    else:
        is_cta = False
        setting_dic = OrderedDict()
        setting_dic["class_name"] = strategy_class_name
        setting_dic["vt_symbols"] = [get_vt_symbols_4_subscription(_) for _ in vt_symbols]
        setting_dic["setting"] = settings = OrderedDict()
        for k, v in strategy_settings.items():
            settings[k] = v

    settings.setdefault('base_position', 1)
    settings.setdefault('stop_opening_pos', 0)
    return setting_dic, is_cta


def get_vt_symbols_4_subscription(vt_symbols):
    """获取可进行行情订阅的合约代码"""
    instrument_type = get_instrument_type(vt_symbols)
    subscription_type = INSTRUMENT_TYPE_SUBSCRIPTION_DIC[instrument_type.upper()]
    return subscription_type + vt_symbols[len(instrument_type):]


def generate_strategy_setting_file(
        stats_list: Optional[List[StrategyBacktestStats]] = None, *,
        ignore_stop_opening_pos_stg=False,
        ignore_old_symbol=False,
        include_holding_pos_stg=True,
        copy_2_folder_path=None,
        backup_strategy_setting_file=True,
):
    """
    生成策略配置文件
    :param stats_list
    :param ignore_stop_opening_pos_stg 忽略 stop_opening_pos == True 的策略
    :param ignore_old_symbol 忽略 过期合约
    :param include_holding_pos_stg 检查策略当前持仓，如果策略持仓，则无论是否 stop_opening_pos == True 都要输出
    :param copy_2_folder_path 将生成的 cta_strategy_setting.json portfolio_strategy_setting.json 复制到制定目录同时不全确实策略
    :param backup_strategy_setting_file 备份原有策略文件
    """
    user_name, broker_id = get_account()
    if stats_list is None:
        stats_list: List[StrategyBacktestStats] = AccountStrategyMapping.get_stats_by_account()

    cta_count, cta_stop_opening_pos = 0, 0
    portfolio_count, portfolio_stop_opening_pos = 0, 0
    cta_dic = OrderedDict()
    portfolio_dic = OrderedDict()
    for stats in stats_list:
        symbols: str = stats.symbols_info.symbols
        strategy_class_name = stats.stg_info.strategy_class_name
        short_name = stats.short_name_of_account
        strategy_settings = stats.strategy_settings_of_account
        if strategy_settings is None:
            logger.warning(
                f"{short_name} {strategy_class_name}[{stats.stg_info_id}]"
                f"on {symbols}[{stats.symbols_info_id}]"
                f"id_name={stats.id_name} strategy_settings is None")
            continue
        if strategy_settings.get('base_position', 1) == 0:
            continue
        setting_dic, is_cta = generate_setting_dic(symbols, strategy_class_name, strategy_settings)
        if (
                ignore_stop_opening_pos_stg and setting_dic['setting']['stop_opening_pos'] == 1
        ) or (
                ignore_old_symbol and
                SymbolsInfo.get_or_create_curr_symbols(symbols, create_if_not_exist=True).symbols != symbols
        ):
            if include_holding_pos_stg:
                if stats.position_of_account == 0:
                    continue
                else:
                    logger.warning(f"{short_name} on {symbols}[{stats.symbols_info_id}] "
                                   f"持仓 {stats.position_of_account} "
                                   f"stop_opening_pos=True 但继续输出到 setting 文件")
            else:
                continue

        if is_cta:
            cta_dic[short_name] = setting_dic
            cta_count += 1
            cta_stop_opening_pos += setting_dic['setting'].get('stop_opening_pos', 0)
        else:
            portfolio_dic[short_name] = setting_dic
            portfolio_count += 1
            portfolio_stop_opening_pos += setting_dic['setting'].get('stop_opening_pos', 0)

    folder_path = os.path.join("output", "strategy_settings", date_2_str(date.today()), f"{user_name}[{broker_id}]")
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "cta_strategy_setting.json")
    with open(file_path, 'w') as f:
        json.dump(cta_dic, f, indent=4)
    if cta_count:
        logger.info(f"{user_name}[{broker_id}] cta 策略 {cta_count} 个，"
                    f"其中 stop_opening_pos {cta_stop_opening_pos} 个")
        if copy_2_folder_path:
            patch_missing_settings_by_dir(cta_dic, copy_2_folder_path, backup_strategy_setting_file)

    file_path = os.path.join(folder_path, "portfolio_strategy_setting.json")
    with open(file_path, 'w') as f:
        json.dump(portfolio_dic, f, indent=4)
    if portfolio_count:
        logger.info(f"{user_name}[{broker_id}] portfolio 策略 {portfolio_count} 个，"
                    f"其中 stop_opening_pos {portfolio_stop_opening_pos} 个")
        if copy_2_folder_path:
            patch_missing_settings_by_dir(portfolio_dic, copy_2_folder_path, backup_strategy_setting_file)


def replace_vt_symbol_2_curr_contract_of_settings(file_path: str):
    """将 settings 中的 vt_symbol 转变为 主力合约"""
    with open(file_path, 'r') as fp:
        settings = json.load(fp)
        new_settings = {}
        vt_symbol_change_set = set()
        for short_name, setting_dic in list(settings.items()):
            if "vt_symbol" in setting_dic:
                vt_symbol = setting_dic["vt_symbol"]
                symbols_info = SymbolsInfo.get_or_create_curr_symbols(
                    vt_symbol, create_if_not_exist=True)
                setting_dic["vt_symbol"] = vt_symbol_new = get_vt_symbols_4_subscription(symbols_info.symbols)
                origin_symbols_str = vt_symbol.split('.')[0]
                new_symbols_str = vt_symbol_new.split('.')[0]
                new_settings[short_name.replace(origin_symbols_str, new_symbols_str)] = setting_dic
                if vt_symbol != vt_symbol_new:
                    vt_symbol_change_set.add((vt_symbol, vt_symbol_new))

            elif "vt_symbols" in setting_dic:
                vt_symbols: list = setting_dic["vt_symbols"]
                vt_symbol_new_list = [
                    SymbolsInfo.get_or_create_curr_symbols(_).symbols for _ in vt_symbols]
                setting_dic["vt_symbols"] = vt_symbols_new = [
                    get_vt_symbols_4_subscription(_) for _ in vt_symbol_new_list]
                origin_symbols_str = '_'.join([_.split('.')[0] for _ in vt_symbols])
                new_symbols_str = '_'.join([_.split('.')[0] for _ in vt_symbols_new])
                new_settings[short_name.replace(origin_symbols_str, new_symbols_str)] = setting_dic
                if origin_symbols_str != new_symbols_str:
                    vt_symbol_change_set.add(('_'.join(vt_symbols), '_'.join(vt_symbols_new)))

            else:
                logging.warning(f"setting = {setting_dic} 无效")

    file_name, ext = os.path.splitext(file_path)
    new_file_name = f"{file_name}_new{ext}"
    with open(new_file_name, 'w') as fp:
        json.dump(new_settings, fp, indent=4)

    if vt_symbol_change_set:
        count = len(vt_symbol_change_set)
        for num, (old, new) in enumerate(vt_symbol_change_set, start=1):
            logger.info(f"{num}/{count}) {old} -> {new}")


def _test_replace_vt_symbol_2_curr_contract_of_settings():
    file_path = r'D:\github\vnpy_extra\vnpy_extra\db\output\strategy_settings\2021-07-30\cta_strategy_setting_1m.json'
    replace_vt_symbol_2_curr_contract_of_settings(file_path=file_path)


def _test_generate_strategy_setting_file():
    # user_name, broker_id = "19510002", "5118"  # 民生期货
    user_name, broker_id = "11859087", "95533"  # 建信期货（资本）
    # user_name, broker_id = "721018", "1025"  # 721018 "量化起航一号（迈科）"
    set_account(user_name, broker_id)
    generate_strategy_setting_file(ignore_stop_opening_pos_stg=True)


def refresh_vt_symbol_2_curr_contract_by_account(
        user_name=None, broker_id=None, remove_stg_if_no_position=True, track_backtest=False, track_backtest_pool=3,
        copy_freeze=True, pre_call_before_backtest=None):
    if user_name:
        set_account(user_name, broker_id)
    else:
        user_name, broker_id = get_account()

    logger.info(f"更新 {user_name}[{broker_id}] 账户中的策略到最新的合约")
    stats_list: List[StrategyBacktestStats] = AccountStrategyMapping.get_stats_by_account()
    count = len(stats_list)
    vt_symbol_change_set = set()
    add_stg_list = []
    delete_stg_id_set = set()
    for num, stats in enumerate(stats_list, start=1):
        vt_symbol = stats.symbols_info.symbols
        vt_symbol_main: str = get_main_contract(vt_symbol)
        stats_main: StrategyBacktestStats = StrategyBacktestStats.get_by_keys(
            stats.stg_info.strategy_class_name, vt_symbol_main, id_name=stats.id_name)
        if stats_main is None:
            logger.warning(
                f"{stats.stg_info.strategy_class_name}[{stats.stg_info_id} on {vt_symbol_main} has not record")
            continue
        symbol_info_curr: SymbolsInfo = SymbolsInfo.get_or_create_curr_symbols(
            vt_symbol_main, create_if_not_exist=True)
        vt_symbol_curr = symbol_info_curr.symbols
        if vt_symbol.upper() == vt_symbol_curr.upper():
            continue
        stats_curr = stats_main.apply_2_symbol(vt_symbol_curr)
        if stats_curr is None:
            continue
        freeze = getattr(stats, 'freeze_of_account', 0) if copy_freeze else 0
        strategy_settings = stats.strategy_settings_of_account
        base_position = strategy_settings.get(BASE_POSITION, 1)
        stop_opening_pos = strategy_settings.get(STOP_OPENING_POS_PARAM, 0)
        if freeze:
            logger.warning(f"{num}/{count}) [{stats.stg_info_id}]{stats.stg_info.strategy_class_name:50s} "
                           f"{vt_symbol}[{stats.symbols_info_id}] -> {vt_symbol_curr}[{symbol_info_curr.id}] 冻结状态")
        else:
            logger.info(f"   {num}/{count}) [{stats.stg_info_id}]{stats.stg_info.strategy_class_name:50s} "
                        f"{vt_symbol}[{stats.symbols_info_id}] -> {vt_symbol_curr}[{symbol_info_curr.id}]")

        stats_curr.add_2_account_strategy_mapping(
            freeze=freeze, base_position=base_position, stop_opening_pos=stop_opening_pos)
        add_stg_list.append((stats, stats_curr))
        vt_symbol_change_set.add((vt_symbol, vt_symbol_curr))
        if remove_stg_if_no_position and stats.position_of_account == 0:
            AccountStrategyMapping.delete_if_no_position(
                stg_info_id=stats.stg_info_id,
                symbols_info_id=stats.symbols_info_id,
                id_name=stats.id_name,
                short_name=stats.short_name,
            )
            delete_stg_id_set.add(stats.id)

    vt_symbol_str = "\n".join([f"{vt_symbol} -> {vt_symbol_curr}"
                               for vt_symbol, vt_symbol_curr in vt_symbol_change_set])
    stats_str = "\n".join([f"{stats.short_name} [{stats.stg_info_id}] "
                           f"{stats.symbols_info.symbols}[{stats.symbols_info_id}] 持仓 {stats.position_of_account} "
                           f"{'[已删除]' if stats.id in delete_stg_id_set else ''}-> "
                           f"{stats_curr.symbols_info.symbols}[{stats_curr.symbols_info_id}]"
                           f"id_name='{stats.id_name}'"
                           for stats, stats_curr in add_stg_list])
    logger.info(f"\n"
                f"{len(add_stg_list)}/{len(stats_list)} 个策略存在主力合约切换：\n"
                f"{stats_str}\n"
                f"包含{len(vt_symbol_change_set)}个合约：\n"
                f"{vt_symbol_str}\n"
                )

    if track_backtest:
        symbols_list = None
        strategy_class_name_list = None
        user_name_broker_id_pair_list = [(user_name, broker_id)]
        try:
            from vnpy_extra.backtest.maintain.track_performance import backtest_all_strategies
            backtest_all_strategies(
                symbols_list=symbols_list,
                strategy_class_name_list=strategy_class_name_list,
                user_name_broker_id_pair_list=user_name_broker_id_pair_list,
                pool_size=track_backtest_pool,
                output_setting_json=True,
                ignore_backtest_in_n_days=2,
                pre_call_before_backtest=pre_call_before_backtest,
            )
        except:
            logging.exception("追踪回测异常")


def export_setting_files(
        user_name=None, broker_id=None,
        refresh_vt_symbol=False,
        ignore_stop_opening_pos_stg=True,
        ignore_old_symbol=True,
        include_holding_pos_stg=True,
):
    if user_name and broker_id:
        set_account(user_name, broker_id)

    if refresh_vt_symbol:
        refresh_vt_symbol_2_curr_contract_by_account()

    generate_strategy_setting_file(
        ignore_stop_opening_pos_stg=ignore_stop_opening_pos_stg,
        ignore_old_symbol=ignore_old_symbol,
        include_holding_pos_stg=include_holding_pos_stg,
    )


def _test_refresh_vt_symbol_2_curr_contract_by_account():
    user_name, broker_id = "11859087", "95533"  # 建信期货（资本）
    set_account(user_name, broker_id)
    refresh_vt_symbol_2_curr_contract_by_account()


def patch_missing_settings_by_dir(settings: Union[dict, str], folder_path, backup_strategy_setting_file=True):
    """
    通过 folder_path/.vntrader 目录下的 cta_strategy_data.json 文件检查是否存在遗失的 setting_dict，并补充到 settings 中
    settings 可以是 字典，也可以是 文件目录
    """
    # 整理参数，确定是 cta_strategy_setting 还是 portfolio_strategy_setting
    if isinstance(settings, str):
        _, setting_file_name = os.path.split(settings)
        with open(settings) as fp:
            settings = json.load(fp)
    else:
        for _, setting_dic in settings.items():
            if "vt_symbols" in setting_dic:
                setting_file_name = "portfolio_strategy_setting.json"
            else:
                setting_file_name = "cta_strategy_setting.json"

            break
        else:
            raise ValueError(f"settings 为空，无法判断是 cta 或 portfolio")

    # 读取旧 settings 数据
    strategy_setting_file_path = os.path.join(folder_path, ".vntrader", setting_file_name)
    with open(strategy_setting_file_path) as fp:
        settings_old = json.load(fp)
    # 数据文件名称
    data_file_name = f'{setting_file_name[:-len("_setting.json")]}_data.json'
    data_file_path = os.path.join(folder_path, ".vntrader", data_file_name)
    with open(data_file_path) as fp:
        data_dic = json.load(fp)

    for key, status_dic in data_dic.items():
        pos = status_dic["pos"]
        # 获取持仓量
        holding_count = sum([abs(_) for _ in pos.values()]) if isinstance(pos, dict) else pos
        if holding_count > 0 and key not in settings:
            if key not in settings_old:
                logger.warning(f"{key} 持仓 {status_dic.get('pos', 0)} 在 {setting_file_name} 中不存在，无法进行补充")
                continue
            settings[key] = setting_dic = settings_old[key].copy()
            setting_dic[STOP_OPENING_POS_PARAM] = 1
            logger.info(f"{key} 持仓 {status_dic.get('pos', 0)} 补充到 {setting_file_name} 中：{setting_dic}")

    if backup_strategy_setting_file:
        os.rename(strategy_setting_file_path,
                  f"{strategy_setting_file_path[:-len('.json')]}.bak{date_2_str(date.today())}.json")

    with open(strategy_setting_file_path, 'w') as fp:
        json.dump(settings, fp, indent=4)

    return settings


def _test_patch_missing_settings_by_dir():
    settings_file_path = r"c:\github\quant_vnpy\scripts_at_convenience\pm\output\strategy_settings\2021-12-09\11859087[95533]\cta_strategy_setting.json"
    folder_path = r"d:\TraderTools\vnpy_work_root\jianxin_11859087"
    patch_missing_settings_by_dir(settings_file_path, folder_path, backup_strategy_setting_file=True)


if __name__ == "__main__":
    # _test_replace_vt_symbol_2_main_contract_of_settings()
    # _test_generate_strategy_setting_file()
    # _test_refresh_vt_symbol_2_main_contract()
    _test_patch_missing_settings_by_dir()
