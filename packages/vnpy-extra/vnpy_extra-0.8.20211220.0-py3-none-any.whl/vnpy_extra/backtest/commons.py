"""
@author  : MG
@Time    : 2021/1/8 7:42
@File    : run.py
@contact : mmmaaaggg@163.com
@desc    : 用于作为回测方法的公共方法
"""
import hashlib
import itertools
import json
import os
from collections import OrderedDict
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, Future
from datetime import date, timedelta
from multiprocessing import Queue, Lock
from multiprocessing import cpu_count, Manager
from queue import Empty
from typing import Optional, Union, Type, List, Callable, Iterator, Dict, Tuple

import pandas as pd
from ibats_utils.decorators import no_with_if_is_none
from ibats_utils.mess import date_2_str, datetime_2_str
from ibats_utils.os import load_class
from tqdm import tqdm
from vnpy.app.cta_strategy import CtaTemplate
from vnpy.app.portfolio_strategy import StrategyTemplate
from vnpy.trader.constant import Interval

from vnpy_extra.backtest import CrossLimitMethod, generate_mock_load_bar_data, DuplicateNameOptions
from vnpy_extra.backtest import DEFAULT_STATIC_ITEM_DIC, CleanupOrcaServerProcessIntermittent
from vnpy_extra.backtest.cta_strategy.engine import BacktestingEngine as CtaBacktestingEngine
from vnpy_extra.backtest.portfolio_strategy.engine import BacktestingEngine as PortfolioBacktestingEngine
from vnpy_extra.config import logging
from vnpy_extra.constants import STOP_OPENING_POS_PARAM, ENABLE_COLLECT_DATA_PARAM, SYMBOL_SIZE_DIC, \
    INSTRUMENT_RATE_DIC, DEFAULT_CAPITAL
from vnpy_extra.db.export_strategy_setting import generate_setting_dic
from vnpy_extra.db.orm import set_account_backtest, StrategyBacktestStats, StrategyBacktestStatusEnum, StrategyInfo
from vnpy_extra.report.collector import trade_data_collector, order_data_collector
from vnpy_extra.utils.exception import MissMatchParametersError
from vnpy_extra.utils.symbol import get_instrument_type, get_price_tick, get_vt_symbol_multiplier, get_vt_symbol_rate

logger = logging.getLogger(__name__)
HAS_PANDAS_EXCEPTION = False
# 默认 root_folder_name 使用程序创建时的系统日期，为了防止跨日出现多个不同日期的文件夹，该日期初始化后不再改变
_root_folder_name = date_2_str(date.today())


def set_default_root_folder_name(name=date_2_str(date.today())):
    """设置默认输出根目录"""
    global _root_folder_name
    if name is None:
        name = date_2_str(date.today())

    _root_folder_name = name


def get_output_file_path(*args, root_folder_name=None):
    """
    获取输出文件的目录
    root_folder_name 为根目录，None则为当前系统日期
    """
    if root_folder_name is None or root_folder_name == "":
        root_folder_name = _root_folder_name
    file_path = os.path.join('output', root_folder_name, *[_ for _ in args if _ is not None])
    dir_path, _ = os.path.split(file_path)
    os.makedirs(dir_path, exist_ok=True)
    return file_path


def run_backtest(
        strategy_class: Union[Type[CtaTemplate], Type[StrategyTemplate]],
        multi_symbols: bool,
        engine_kwargs: dict,
        strategy_kwargs: Optional[dict] = None,
        root_folder_name=None,
        file_name_header=None,
        engine: Optional[Union[CtaBacktestingEngine, PortfolioBacktestingEngine]] = None,
        output_available_only=False,
        output_trades=False,
        output_orders=False,
        open_browser_4_charts=False,
        log_statistic_markdown=False,
        show_indexes=None,
        print_statistics=True,
        lock: Optional[Lock] = None,
        enable_collect_data=False,
        save_stats: Optional[bool] = None,
        strategy_stats_original: Optional[StrategyBacktestStats] = None,
        enable_join_collector=True,
        ignore_existed_backtest=False,
        output_path_has_strategy_class_name=False,
        output_separate_by_backtest_status=False,
        output_setting_json=True,
        file_name_include_symbol=False,
        short_name_with_file_name_if_exist=True,
        stg_info_duplicate_name_options=DuplicateNameOptions.raise_error,
        default_backtest_status=None,
) -> Optional[dict]:
    """
    本地化运行策略回测程序
    :param strategy_class 策略类
    :param multi_symbols 是否多合约
    :param engine_kwargs 回测引擎参数，或者回测引擎参数列表
    :param strategy_kwargs 策略类 参数数组字典,key为参数名称, value 为数组
    :param file_name_header 自定义文件头名称，默认为None，所有["参数名+参数", ...]用下划线链接
    :param engine 回测引擎
    :param output_available_only 仅当策略有效是才输出统计数据、图片、参数等文件
    :param output_trades 输出交易数据到 csv 文件（不受 output_available_only 影响）
    :param output_orders 输出订单数据到 csv 文件（不受 output_available_only 影响）
    :param open_browser_4_charts
    :param root_folder_name 策略类 保存跟目录名称,None 时为当前系统日期
    :param log_statistic_markdown Markdown 格式记录统计数据
    :param show_indexes 展示指标
    :param print_statistics 输出统计结果
    :param lock 进程锁
    :param enable_collect_data 是否运行收集数据
    :param save_stats 保存统计数据，默认情况下只记录 CrossLimitMethod.open_price 的回测结果数据
    :param strategy_stats_original 此前回测的统计数据对象
    :param enable_join_collector 是否交易结束后关闭 collector
    :param ignore_existed_backtest 默认为False.是否忽略以及存在的回测.即,如果当前回测在数据库中已经存在,则跳过该测试.
    :param output_path_has_strategy_class_name 默认为False.输出文件路径是否包含 策略类名称.
    :param output_separate_by_backtest_status 默认为False.输出文件路径是否包含按 backtest_status 分目录存放.
    :param output_setting_json 生成 setting json 文件
    :param file_name_include_symbol 生成文件的文件名带 symbol 用以进行区分，默认False，过长文件名可能导致系统不支持长文件名错误。
    :param short_name_with_file_name_if_exist 默认 True。如果当前回测存在 short_name 则将short_name添加到文件名末尾。
    :param stg_info_duplicate_name_options 默认 DuplicateNameOptions.raise_error。策略重名应对措施。该参数仅在 save_stats == True 的情况下启用
    :param default_backtest_status 指定默认 回测状态为 None
    """
    set_account_backtest()
    # 整理参数
    engine_kwargs = engine_kwargs.copy()
    engine_kwargs.setdefault('capital', DEFAULT_CAPITAL)
    start = engine_kwargs.setdefault("start", date(2017, 1, 1))
    end = engine_kwargs.setdefault("end", date.today() - timedelta(days=90))
    interval = engine_kwargs.setdefault("interval", Interval.MINUTE)
    cross_limit_method = engine_kwargs.setdefault("cross_limit_method", CrossLimitMethod.open_price)
    if save_stats is None:
        # 默认情况下只记录 CrossLimitMethod.open_price 的回测结果数据
        save_stats = cross_limit_method == CrossLimitMethod.open_price

    strategy_class_name = strategy_class.__name__
    module_name = strategy_class.__module__
    if save_stats:
        with no_with_if_is_none(lock):
            stg_obj = StrategyInfo.get_instance_by_strategy_class_name(strategy_class_name)

        if stg_obj is not None and stg_obj.module_name != module_name:
            if stg_info_duplicate_name_options == DuplicateNameOptions.raise_error:
                raise ValueError(
                    f"策略 {strategy_class_name} 与数据库中 {stg_obj.module_name}.{stg_obj.strategy_class_name} 重名。"
                    f"如果希望继续执行当前回测，请调整 stg_info_duplicate_name_options 参数。")
            elif stg_info_duplicate_name_options == DuplicateNameOptions.replace:
                with no_with_if_is_none(lock):
                    StrategyInfo.update_module_name(strategy_class_name, module_name)

                logger.warning(
                    f"策略 {strategy_class_name} 存在模块冲突。 {stg_obj.module_name}.{stg_obj.strategy_class_name} --> "
                    f"已经被替换为 {module_name}.{strategy_class_name}。")
            elif stg_info_duplicate_name_options == DuplicateNameOptions.no_change:
                module_name = stg_obj.module_name
            else:
                raise ValueError(f"stg_info_duplicate_name_options={stg_info_duplicate_name_options} 不是有效的选项")

    if multi_symbols:
        vt_symbols = engine_kwargs["vt_symbols"]
        vt_symbol_str = "_".join(vt_symbols)
        output_path_vt_symbol = symbol_str = "_".join([_.split('.')[0] for _ in vt_symbols])
        tmp_name = get_output_file_path(
            strategy_class_name if output_path_has_strategy_class_name else None,
            output_path_vt_symbol, cross_limit_method.name, None,
            'params', f'{file_name_header}_param.json', root_folder_name=root_folder_name)
        if len(tmp_name) > 255:
            output_path_vt_symbol = hashlib.md5(output_path_vt_symbol.encode('utf-8')).hexdigest()

        engine_kwargs.setdefault('sizes', {vt_symbol: SYMBOL_SIZE_DIC[get_instrument_type(vt_symbol)]
                                           for vt_symbol in vt_symbols})
        engine_kwargs.setdefault('rates', {vt_symbol: INSTRUMENT_RATE_DIC[get_instrument_type(vt_symbol)]
                                           for vt_symbol in vt_symbols})
        engine_kwargs.setdefault('slippages', {vt_symbol: 0 for vt_symbol in vt_symbols})
        engine_kwargs.setdefault('priceticks', {vt_symbol: get_price_tick(vt_symbol)
                                                for vt_symbol in vt_symbols})
    else:
        vt_symbol = engine_kwargs["vt_symbol"]
        output_path_vt_symbol = vt_symbol_str = vt_symbol
        symbol_str = vt_symbol_str.split('.')[0]
        engine_kwargs.setdefault('size', get_vt_symbol_multiplier(vt_symbol))
        engine_kwargs.setdefault("rate", get_vt_symbol_rate(vt_symbol))
        engine_kwargs.setdefault("slippage", 0)
        engine_kwargs.setdefault('pricetick', get_price_tick(vt_symbol))

    if default_backtest_status is not None:
        try:
            StrategyBacktestStatusEnum(default_backtest_status)
        except ValueError as exp:
            logger.exception(f"default_backtest_status={default_backtest_status} 无效")
            raise exp from exp

    # 初始化引擎
    load_data = True
    if engine is None:
        if multi_symbols:
            engine = PortfolioBacktestingEngine()
        else:
            engine = CtaBacktestingEngine()
    else:
        if multi_symbols:
            vt_symbols = [_.upper() for _ in engine_kwargs["vt_symbols"]]
            load_data = not (
                    engine.vt_symbols == vt_symbols
                    and engine.start == start
                    and engine.end == end
                    and engine.interval == interval)
        else:
            vt_symbol = engine_kwargs["vt_symbol"]
            load_data = not (
                    engine.vt_symbol == vt_symbol
                    and engine.start == start
                    and engine.end == end
                    and engine.interval == interval)

        # 清除上一轮测试数据
        engine.clear_data()

    # 设置环境参数
    engine.set_parameters(**engine_kwargs)

    # 设置策略参数
    if strategy_kwargs is None:
        logger.warning('%s 回测没有设置参数项，使用默认参数', strategy_class_name)
        strategy_kwargs = {}

    if enable_collect_data:
        strategy_kwargs['enable_collect_data'] = enable_collect_data

    try:
        engine.add_strategy(strategy_class=strategy_class, setting=strategy_kwargs)
        engine.strategy.set_is_realtime_mode(False)
    except MissMatchParametersError as exp:
        logger.error(exp.args[0])
        return None

        # 获取 id_name
    id_name = engine.strategy.get_id_name()
    if strategy_stats_original is None:
        with no_with_if_is_none(lock):
            strategy_stats_original = StrategyBacktestStats.get_by_keys(
                strategy_class_name, vt_symbol_str, id_name, cross_limit_method.value)

    if strategy_stats_original is not None:
        backtest_status_old = strategy_stats_original.backtest_status
        short_name = strategy_stats_original.short_name
        shown_name = strategy_stats_original.shown_name
    else:
        backtest_status_old, short_name, shown_name = None, None, None

    if output_separate_by_backtest_status:
        if backtest_status_old is not None:
            backtest_status_enum: StrategyBacktestStatusEnum = StrategyBacktestStatusEnum(
                backtest_status_old)
            backtest_status_path = f"{backtest_status_enum.value}{backtest_status_enum.name}"
        elif default_backtest_status is not None:
            backtest_status_enum: StrategyBacktestStatusEnum = StrategyBacktestStatusEnum(default_backtest_status)
            backtest_status_path = f"{backtest_status_enum.value}{backtest_status_enum.name}"
        else:
            backtest_status_path = None
    else:
        backtest_status_path = None

    if backtest_status_old is not None:
        backtest_status = backtest_status_old
    elif default_backtest_status is not None:
        backtest_status = default_backtest_status
    else:
        backtest_status = StrategyBacktestStatusEnum.Unavailable.value

    root_folder_path = get_output_file_path(
        strategy_class_name if output_path_has_strategy_class_name else None,
        output_path_vt_symbol, cross_limit_method.name, backtest_status_path, root_folder_name=root_folder_name)

    if file_name_header is None or file_name_header == "":
        file_name_header = f"{id_name}_{symbol_str}" if file_name_include_symbol else id_name

    if short_name_with_file_name_if_exist and short_name is not None:
        engine.strategy.strategy_name = short_name
        full_name = f"{file_name_header}_[{short_name}]"
        # os file path max len 255
        if len(os.path.abspath(root_folder_path)) + len(full_name) < 240:
            file_name_header = full_name

    image_file_name = get_output_file_path(
        strategy_class_name if output_path_has_strategy_class_name else None,
        output_path_vt_symbol, cross_limit_method.name, backtest_status_path,
        'images', f'{file_name_header}.png', root_folder_name=root_folder_name)
    stat_file_name = get_output_file_path(
        strategy_class_name if output_path_has_strategy_class_name else None,
        output_path_vt_symbol, cross_limit_method.name, backtest_status_path,
        'stats', f'{file_name_header}_stats.md', root_folder_name=root_folder_name)
    daily_result_file_name = get_output_file_path(
        strategy_class_name if output_path_has_strategy_class_name else None,
        output_path_vt_symbol, cross_limit_method.name, backtest_status_path,
        'data', f'{file_name_header}_result.csv', root_folder_name=root_folder_name)
    param_file_name = get_output_file_path(
        strategy_class_name if output_path_has_strategy_class_name else None,
        output_path_vt_symbol, cross_limit_method.name, backtest_status_path,
        'params', f'{file_name_header}_param.json', root_folder_name=root_folder_name)
    # output_setting_json 绝对是否生成 setting json 文件
    if output_setting_json:
        setting_json_file_name = get_output_file_path(
            strategy_class_name if output_path_has_strategy_class_name else None,
            output_path_vt_symbol, cross_limit_method.name, backtest_status_path,
            'setting', f'{file_name_header}_setting.json', root_folder_name=root_folder_name)
    else:
        setting_json_file_name = None

    # 生成订单记录文件
    if output_orders:
        order_file_name = get_output_file_path(
            strategy_class_name if output_path_has_strategy_class_name else None,
            output_path_vt_symbol, cross_limit_method.name, backtest_status_path,
            'orders', f'{file_name_header}_orders.csv', root_folder_name=root_folder_name)
    else:
        order_file_name = None

    # 生成交易记录文件
    if output_trades:
        trade_file_name = get_output_file_path(
            strategy_class_name if output_path_has_strategy_class_name else None,
            output_path_vt_symbol, cross_limit_method.name, backtest_status_path,
            "trades", f'{file_name_header}_trades.csv', root_folder_name=root_folder_name)
    else:
        trade_file_name = None

    if ignore_existed_backtest:
        # 检查是否跳过回测
        is_existed = False
        if strategy_stats_original is not None:
            # 检查数据库中回测状态是否存在
            is_existed = True
        elif os.path.exists(param_file_name):
            # 检查当前系统回测文件是否存在
            is_existed = True

        if is_existed:
            logger.warning(
                f"ignore {strategy_class_name}[{vt_symbol_str}] {id_name} {cross_limit_method.name} "
                f"回测结果已经存在不再重复测试")
            return None

    # 加载历史数据
    if load_data:
        def write_log_func(msg, level=None):
            if level is None:
                level = 'info'

            engine.output(msg)
            getattr(logger, level.lower())(msg)

        load_main_continuous_md = getattr(engine.strategy, 'load_main_continuous_md', False)
        fix_db_bar_datetime = getattr(engine.strategy, 'fix_db_bar_datetime', False)
        write_log_func(f'load_main_continuous_md={load_main_continuous_md}, fix_db_bar_datetime={fix_db_bar_datetime}')
        with generate_mock_load_bar_data(
                write_log_func=write_log_func,
                load_main_continuous_md=load_main_continuous_md,
                fix_db_bar_datetime=fix_db_bar_datetime,
        ):
            with no_with_if_is_none(lock):
                engine.load_data()

    # 开始回测
    if enable_collect_data:
        # 删除策略历史交易数据
        from vnpy_extra.db.orm import TradeDataModel
        TradeDataModel.clear_by_strategy_name(strategy_class_name)

    try:
        engine.run_backtesting()
    except ValueError as exp:
        # ValueError 错误有些情况是由于行情数据无效导致的，因此退出循环直接结束
        # File "D:\vnstudio\lib\site-packages\vnpy\app\cta_strategy\backtesting.py", line 313, in run_backtesting
        #     for ix, i in enumerate(range(0, total_size, batch_size)):
        # ValueError: range() arg 3 must not be zero
        logger.exception("run_backtesting error\n相关参数：\nengine_kwargs:\n%s\nstrategy_kwargs:\n%s",
                         engine_kwargs, strategy_kwargs)
        raise exp from exp
    except:
        logger.exception("run_backtesting error\n相关参数：\nengine_kwargs:\n%s\nstrategy_kwargs:\n%s",
                         engine_kwargs, strategy_kwargs)
        return None

    # 输出订单数据
    if output_orders:
        orders = engine.get_all_orders()
        pd.DataFrame([{
            "vt_symbol": _.vt_symbol,
            "datetime": datetime_2_str(_.datetime),
            "direction": _.direction.value,
            "offset": _.offset.value,
            "price": _.price,
            "volume": _.volume,
            "traded": _.traded,
            "status": _.status,
            "reference": _.reference,
        } for _ in orders]).to_csv(order_file_name, index=False)

    # 输出交易数据
    if output_trades:
        trades = engine.get_all_trades()
        pd.DataFrame([{
            "vt_symbol": _.vt_symbol,
            "datetime": datetime_2_str(_.datetime),
            "direction": _.direction.value,
            "offset": _.offset.value,
            "price": _.price,
            "volume": _.volume,
        } for _ in trades if _.volume != 0]).to_csv(trade_file_name, index=False)

    if enable_collect_data and enable_join_collector:
        # 仅用于测试 trade_data_collector 使用，一般回测状态下不进行数据采集
        trade_data_collector.join_queue()
        order_data_collector.join_queue()
        trade_data_collector.is_running = False
        order_data_collector.is_running = False

    # 统计结果
    df: pd.DataFrame = engine.calculate_result()
    # 统计绩效
    statistics = engine.calculate_statistics(output=print_statistics)
    statistics["module_name"] = module_name
    statistics["strategy_class_name"] = strategy_class_name
    statistics['symbols'] = vt_symbol_str
    statistics["cross_limit_method"] = cross_limit_method.value
    statistics["backtest_status"] = backtest_status
    statistics["id_name"] = id_name

    has_file_not_found_error = False
    # 保存参数
    try:
        # param_file_name 作为判断重复回测的依据，无论回测是否有效都要输出该文件。
        with open(param_file_name, 'w') as fp:
            json.dump(strategy_kwargs, indent=4, fp=fp)
    except FileNotFoundError:
        if has_file_not_found_error:
            pass
        else:
            logger.exception("写文件失败，不影响后续程序继续运行")
            has_file_not_found_error = True

    if output_available_only and not statistics['available']:
        pass
    else:
        if df is not None:
            # engine.output(df)
            try:
                df[[_ for _ in df.columns if _ != "trades"]].to_csv(daily_result_file_name)
            except FileNotFoundError:
                has_file_not_found_error = True
                logger.exception("写文件失败，不影响后续程序继续运行")
            # 展示图表
            charts_data = engine.show_chart(
                image_file_name=image_file_name,
                open_browser_4_charts=open_browser_4_charts,
                show_indexes=show_indexes,
                lock=lock,
            )
        else:
            charts_data = None

        image_file_url = image_file_name.replace('\\', '/')
        statistics["image_file_url"] = f"![img]({image_file_url})"
        statistics["image_file_path"] = image_file_name

        # 保存参数
        try:
            # 生成 setting json 文件
            if output_setting_json:
                settings, is_cta = generate_setting_dic(vt_symbol_str, strategy_class_name, strategy_kwargs)
                with open(setting_json_file_name, 'w') as fp:
                    json.dump({file_name_header: settings}, indent=4, fp=fp)

        except FileNotFoundError:
            if has_file_not_found_error:
                pass
            else:
                logger.exception("写文件失败，不影响后续程序继续运行")
                has_file_not_found_error = True

        try:
            # 保存绩效结果
            statistics_s = pd.Series(statistics)
            statistics_s.name = file_name_header
            statistics_s.index.rename('item', inplace=True)
            if log_statistic_markdown:
                logger.info("\n:%s", statistics_s.to_markdown())

            with open(stat_file_name, 'w') as f:
                statistics_s.to_markdown(f, 'w')

        except AttributeError:
            global HAS_PANDAS_EXCEPTION
            if not HAS_PANDAS_EXCEPTION:
                logger.warning("pandas 需要 1.0.0 以上版本才能够支持此方法")
                HAS_PANDAS_EXCEPTION = True
        except FileNotFoundError:
            if has_file_not_found_error:
                pass
            else:
                logger.exception("写文件失败，不影响后续程序继续运行")
                has_file_not_found_error = True

        logger.info("策略回测文件保存到目录：%s", root_folder_path)

        if short_name is not None:
            statistics['short_name'] = short_name

        if shown_name is not None:
            statistics['shown_name'] = shown_name

        # 将回测结果保存到数据库
        if save_stats:
            strategy_settings = {k: v for k, v in strategy_kwargs.items()
                                 if k not in (ENABLE_COLLECT_DATA_PARAM, STOP_OPENING_POS_PARAM)}
            interval = engine_kwargs["interval"]
            engine_kwargs["interval"] = interval.value if isinstance(interval, Interval) else str(interval)
            with no_with_if_is_none(lock):
                StrategyBacktestStats.update_stats(
                    strategy_settings=strategy_settings,
                    engine_kwargs=engine_kwargs,
                    statistics=statistics,
                    charts_data=charts_data,
                    old_id_name=strategy_stats_original.id_name if strategy_stats_original is not None else None,
                )

    if enable_collect_data and enable_join_collector:
        trade_data_collector.join()
        order_data_collector.join()

    return statistics


def run_backtest_from_queue(strategy_cls: Type[Union[CtaTemplate, StrategyTemplate]],
                            task_queue: Queue, engine_key_results_dic: dict, lock: Lock,
                            statistic_item_dic, multi_valued_param_name_list, name, multi_symbols: bool):
    """
    :param strategy_cls 策略类
    :param task_queue 任务参数队列
    :param engine_key_results_dic 执行结果队列
    :param lock 进程锁
    :param statistic_item_dic 统计项
    :param multi_valued_param_name_list 参数名称
    :param name 进程名称
    :param multi_symbols 是否多合约
    """
    logger.info("启动子进程 %s 监控任务队列 task_queue,结果返回给 engine_key_results_dic", name)
    if multi_symbols:
        engine = PortfolioBacktestingEngine()
    else:
        engine = CtaBacktestingEngine()

    job_count = 0
    symbols = ''
    vt_symbols_last = None
    while True:
        try:
            # 阻塞等待消息队列传递参数
            engine_param_key, backtest_param_kwargs = task_queue.get(block=True, timeout=5)
            engine_kwargs = backtest_param_kwargs["engine_kwargs"]
            vt_symbols = engine_kwargs["vt_symbols"] if "vt_symbols" in engine_kwargs else engine_kwargs["vt_symbol"]
            if vt_symbols_last and vt_symbols_last != vt_symbols:
                logger.warning(f"{vt_symbols_last} -> {vt_symbols} 合约切换，当前任务队列结束，切换新的任务队列")
                task_queue.task_done()
                task_queue.put((engine_param_key, backtest_param_kwargs), block=True)
                logger.warning("put key=%s task=%s in queue 任务重新推入队列", engine_param_key, backtest_param_kwargs)
                break

            job_count += 1
            logger.debug('process %s %d task| key=%s, backtest_param_kwargs=%s',
                         name, job_count, engine_param_key, backtest_param_kwargs)
            try:
                stats_dic = run_backtest(
                    strategy_cls,
                    multi_symbols=multi_symbols,
                    engine=engine,
                    print_statistics=False,
                    lock=lock,
                    **backtest_param_kwargs
                )
            except Exception:
                logger.exception("%s %s run_backtest error %s", strategy_cls.__name__, name, backtest_param_kwargs)
                task_queue.task_done()
                continue

            task_queue.task_done()
            # 当前测试已存在因此直接跳过,或者回测没有产生交易.
            if stats_dic is None:
                continue
            strategy_kwargs = backtest_param_kwargs["strategy_kwargs"]
            # 按顺序更新参数及统计指标
            statistics_with_param_dic = OrderedDict([
                (k, v) for k, v in strategy_kwargs.items() if k in multi_valued_param_name_list])
            for k in statistic_item_dic.keys():
                statistics_with_param_dic[k] = stats_dic[k] if k in stats_dic else None

            with no_with_if_is_none(lock):
                # 多进程 dict 对象只能使用 赋值 操作。不可以使用 [].append 的操作。
                # 因此不可以使用 setdefault(key, []).append()
                if engine_param_key in engine_key_results_dic:
                    results = engine_key_results_dic[engine_param_key]
                    results.append(statistics_with_param_dic)
                else:
                    results = [statistics_with_param_dic]

                engine_key_results_dic[engine_param_key] = results

            symbols = statistics_with_param_dic['symbols']
            logger.debug('%s[%s] process %s %d task| key=%s finished',
                         strategy_cls.__name__, symbols, name, job_count, engine_param_key)
            # logger.warning("symbols=%s, statistics_with_param_dic: %s", symbols, statistics_with_param_dic)
        except Empty:
            break
        finally:
            logger.warning("%s[%s] Process '%s' 没有收到任务信息,结束进程，累计完成 %d 个任务",
                           strategy_cls.__name__, symbols, name, job_count)


def get_param_values_iter(param_values_dic: Union[dict, List[dict]]) -> Tuple[List[str], Iterator[list]]:
    if isinstance(param_values_dic, dict):
        param_values_dic_list = [param_values_dic]
    elif isinstance(param_values_dic, list):
        param_values_dic_list = param_values_dic
    else:
        raise ValueError(f"param_values_dic {type(param_values_dic)} 参数类型不支持")

    param_name_list = None
    param_values_iter_source = []
    for param_values_dic in param_values_dic_list:
        if param_name_list is None:
            param_name_list = list(param_values_dic.keys())

        param_iter = itertools.product(*[
            param_values_dic[_] if _ in param_values_dic else [None] for _ in param_name_list
        ])
        param_values_iter_source.append(param_iter)

    param_values_iter = itertools.chain(*param_values_iter_source)
    return param_name_list, param_values_iter


def get_param_values_iter_vt_symbol(
        param_values_dic: Union[dict, List[dict]]) -> Iterator[Tuple[List[str], Iterator[list]]]:
    if isinstance(param_values_dic, dict):
        param_values_dic_list = [param_values_dic]
    elif isinstance(param_values_dic, list):
        param_values_dic_list = param_values_dic
    else:
        raise ValueError(f"param_values_dic {type(param_values_dic)} 参数类型不支持")

    param_name_list = None
    param_values_iter_source = []
    for param_values_dic in param_values_dic_list:
        if param_name_list is None:
            param_name_list = list(param_values_dic.keys())

        param_iter = itertools.product(*[
            param_values_dic[_] if _ in param_values_dic else [None] for _ in param_name_list
        ])
        param_values_iter_source.append(param_iter)

    param_values_iter = itertools.chain(*param_values_iter_source)
    yield param_name_list, param_values_iter


def get_backtest_params_iter(
        backtest_param_dic_list: Union[dict, List[dict]],
        param_values_dic: Union[dict, List[dict]],
) -> Tuple[List[str], Iterator[Tuple[dict, list, Optional[StrategyBacktestStats]]]]:
    """
    返回参数参数名称列表以及迭代器兑现
    :param backtest_param_dic_list 合约列表(可以是 str 数组,或者 tuple 数组,如果是 tuple 对应 (vt_symbol, slippage, size)
    :param param_values_dic 策略类 参数数组字典,key为参数名称, value 为数组
    """
    param_name_list, param_values_iter = get_param_values_iter(param_values_dic)

    if isinstance(backtest_param_dic_list, dict):
        backtest_param_dic_list = [backtest_param_dic_list]

    backtest_params_iter = itertools.product(backtest_param_dic_list, param_values_iter, [None])
    return param_name_list, backtest_params_iter


def get_backtest_params_iter_separated_by_vt_symbol(
        backtest_param_dic_list: Union[dict, List[dict]],
        param_values_dic: Union[dict, List[dict]],
) -> Iterator[Tuple[str, Tuple[List[str], Iterator[Tuple[dict, list, Optional[StrategyBacktestStats]]]]]]:
    """
    返回参数参数名称列表以及迭代器兑现
    :param backtest_param_dic_list 合约列表(可以是 str 数组,或者 tuple 数组,如果是 tuple 对应 (vt_symbol, slippage, size)
    :param param_values_dic 策略类 参数数组字典,key为参数名称, value 为数组
    """
    backtest_param_dic_list_separated_by_vt_symbols = defaultdict(list)
    # 按照 vt_symbol_key 进行分组整理
    for backtest_param_dic in backtest_param_dic_list:
        vt_symbol_key = "vt_symbols" if "vt_symbols" in backtest_param_dic else "vt_symbol"
        vt_symbol = backtest_param_dic[vt_symbol_key]
        backtest_param_dic_new = backtest_param_dic.copy()
        backtest_param_dic_new[vt_symbol_key] = vt_symbol
        backtest_param_dic_list_separated_by_vt_symbols[vt_symbol].append(backtest_param_dic_new)

    # 生成迭代器
    for vt_symbol, backtest_param_dic_list_new in backtest_param_dic_list_separated_by_vt_symbols.items():
        for param_name_list, param_values_iter in get_param_values_iter_vt_symbol(param_values_dic):
            backtest_params_iter = itertools.product(backtest_param_dic_list_new, param_values_iter, [None])
            yield vt_symbol, param_name_list, backtest_params_iter


def bulk_backtest(
        strategy_cls: Union[Type[StrategyTemplate], Type[CtaTemplate]],
        multi_symbols: bool,
        engine_param_dic_list: Union[dict, List[dict]],
        strategy_param_dic_list: Union[Dict[str, list], List[Dict[str, list]]],
        available_backtest_params_check_func: Optional[Callable] = None,
        file_name_func: Optional[Callable] = None,
        statistic_item_dic: Optional[dict] = None,
        engine_param_key_func: Optional[Callable] = None,
        output_available_only: bool = True,
        open_browser_4_charts: bool = False,
        root_folder_name: Optional[str] = None,
        multi_process: int = 0,
        save_stats: Optional[bool] = None,
        enable_collect_data=False,
        ignore_existed_backtest=False,
        output_path_has_strategy_class_name=True,
        output_separate_by_backtest_status=False,
        output_setting_json=True,
        file_name_include_symbol=False,
        stg_info_duplicate_name_options=DuplicateNameOptions.raise_error,
):
    """
    :param strategy_cls 策略类
    :param multi_symbols 是否多合约
    :param engine_param_dic_list 回测引擎参数，或者回测引擎参数列表
    :param strategy_param_dic_list 策略类 参数数组字典,key为参数名称, value 为数组
    :param available_backtest_params_check_func 如果希望忽略部分参数组合，可以自定义函数，对每一个组合进行筛选，False为忽略该参数
    :param file_name_func 自定义文件头名称，默认为None，所有["参数名+参数", ...]用下划线链接
    :param statistic_item_dic 策略类 统计项默认 DEFAULT_STATIC_ITEM_DIC
    :param engine_param_key_func engine param key
    :param output_available_only
    :param open_browser_4_charts
    :param root_folder_name 策略类 保存跟目录名称,None 时为当前系统日期
    :param multi_process 0 单进程, -1 为CPU数量,正数为对应的进程数
    :param save_stats 保存统计数据，默认情况下只记录 CrossLimitMethod.open_price 的回测结果数据
    :param enable_collect_data 是否运行收集数据
    :param ignore_existed_backtest 默认为False.是否忽略以及存在的回测.即,如果当前回测在数据库中已经存在,则跳过该测试.
    :param output_path_has_strategy_class_name 默认为False.输出文件路径是否包含 策略类名称.
    :param output_separate_by_backtest_status 默认为False.输出文件路径是否包含按 backtest_status 分目录存放.
    :param output_setting_json 生成 setting json 文件
    :param file_name_include_symbol 生成文件的文件名带 symbol 用以进行区分，默认False，过长文件名可能导致系统不支持长文件名错误。
    :param stg_info_duplicate_name_options 默认 DuplicateNameOptions.raise_error。策略重名应对措施。该参数仅在 save_stats == True 的情况下启用
    """
    if root_folder_name is None:
        root_folder_name = f'{strategy_cls.__name__}_{date_2_str(date.today())}'

    # 整理参数
    param_name_list, backtest_params_iter = get_backtest_params_iter(engine_param_dic_list, strategy_param_dic_list)
    bulk_backtest_with_backtest_params_iter(
        strategy_cls=strategy_cls,
        multi_symbols=multi_symbols,
        param_name_list=param_name_list,
        backtest_params_iter=backtest_params_iter,
        available_backtest_params_check_func=available_backtest_params_check_func,
        file_name_func=file_name_func,
        statistic_item_dic=statistic_item_dic,
        engine_param_key_func=engine_param_key_func,
        output_available_only=output_available_only,
        open_browser_4_charts=open_browser_4_charts,
        root_folder_name=root_folder_name,
        multi_process=multi_process,
        save_stats=save_stats,
        enable_collect_data=enable_collect_data,
        ignore_existed_backtest=ignore_existed_backtest,
        output_path_has_strategy_class_name=output_path_has_strategy_class_name,
        output_separate_by_backtest_status=output_separate_by_backtest_status,
        output_setting_json=output_setting_json,
        file_name_include_symbol=file_name_include_symbol,
        stg_info_duplicate_name_options=stg_info_duplicate_name_options,
    )


def bulk_backtest_multi_process_by_symbols(
        strategy_cls: Union[Type[StrategyTemplate], Type[CtaTemplate]],
        multi_symbols: bool,
        engine_param_dic_list: Union[dict, List[dict]],
        strategy_param_dic_list: Union[Dict[str, list], List[Dict[str, list]]],
        available_backtest_params_check_func: Optional[Callable] = None,
        file_name_func: Optional[Callable] = None,
        statistic_item_dic: Optional[dict] = None,
        engine_param_key_func: Optional[Callable] = None,
        output_available_only: bool = True,
        open_browser_4_charts: bool = False,
        root_folder_name: Optional[str] = None,
        multi_process: int = 0,
        save_stats: Optional[bool] = None,
        enable_collect_data=False,
        ignore_existed_backtest=False,
        output_path_has_strategy_class_name=True,
        output_separate_by_backtest_status=False,
        output_setting_json=True,
        file_name_include_symbol=False,
        stg_info_duplicate_name_options=DuplicateNameOptions.raise_error,
        pre_call_before_backtest=None,
):
    """
    多进程批量回测，每个 symbols 占用单独一个进程。进程结束相关内存释放。相比 bulk_backtest 可以有效避免内存不足问题。
    :param strategy_cls 策略类
    :param multi_symbols 是否多合约
    :param engine_param_dic_list 回测引擎参数，或者回测引擎参数列表
    :param strategy_param_dic_list 策略类 参数数组字典,key为参数名称, value 为数组
    :param available_backtest_params_check_func 如果希望忽略部分参数组合，可以自定义函数，对每一个组合进行筛选，False为忽略该参数
    :param file_name_func 自定义文件头名称，默认为None，所有["参数名+参数", ...]用下划线链接
    :param statistic_item_dic 策略类 统计项默认 DEFAULT_STATIC_ITEM_DIC
    :param engine_param_key_func engine param key
    :param output_available_only
    :param open_browser_4_charts
    :param root_folder_name 策略类 保存跟目录名称,None 时为当前系统日期
    :param multi_process 0 单进程, -1 为CPU数量,正数为对应的进程数
    :param save_stats 保存统计数据，默认情况下只记录 CrossLimitMethod.open_price 的回测结果数据
    :param enable_collect_data 是否运行收集数据
    :param ignore_existed_backtest 默认为False.是否忽略以及存在的回测.即,如果当前回测在数据库中已经存在,则跳过该测试.
    :param output_path_has_strategy_class_name 默认为False.输出文件路径是否包含 策略类名称.
    :param output_separate_by_backtest_status 默认为False.输出文件路径是否包含按 backtest_status 分目录存放.
    :param output_setting_json 生成 setting json 文件
    :param file_name_include_symbol 生成文件的文件名带 symbol 用以进行区分，默认False，过长文件名可能导致系统不支持长文件名错误。
    :param stg_info_duplicate_name_options 默认 DuplicateNameOptions.raise_error。策略重名应对措施。该参数仅在 save_stats == True 的情况下启用
    :param pre_call_before_backtest 回测前调用当前函数，主要用于动态加载使用
    """
    if root_folder_name is None:
        root_folder_name = f'{strategy_cls.__name__}_{date_2_str(date.today())}'

    if multi_process < 0:
        # 默认CPU数量
        multi_process = cpu_count()

    if multi_process == 0:
        # 整理参数
        param_name_list, backtest_params_iter = get_backtest_params_iter(engine_param_dic_list, strategy_param_dic_list)
        bulk_backtest_with_backtest_params_iter(
            strategy_cls=strategy_cls,
            multi_symbols=multi_symbols,
            param_name_list=param_name_list,
            backtest_params_iter=backtest_params_iter,
            available_backtest_params_check_func=available_backtest_params_check_func,
            file_name_func=file_name_func,
            statistic_item_dic=statistic_item_dic,
            engine_param_key_func=engine_param_key_func,
            output_available_only=output_available_only,
            open_browser_4_charts=open_browser_4_charts,
            root_folder_name=root_folder_name,
            multi_process=0,
            save_stats=save_stats,
            enable_collect_data=enable_collect_data,
            ignore_existed_backtest=ignore_existed_backtest,
            output_path_has_strategy_class_name=output_path_has_strategy_class_name,
            output_separate_by_backtest_status=output_separate_by_backtest_status,
            output_setting_json=output_setting_json,
            file_name_include_symbol=file_name_include_symbol,
            stg_info_duplicate_name_options=stg_info_duplicate_name_options,
            pre_call_before_backtest=pre_call_before_backtest,
        )
    else:
        pool = ProcessPoolExecutor(max_workers=multi_process)
        future = None
        try:
            for vt_symbol, param_name_list, backtest_params_iter in get_backtest_params_iter_separated_by_vt_symbol(
                    engine_param_dic_list, strategy_param_dic_list):
                future = pool.submit(
                    bulk_backtest_with_backtest_params_iter,
                    strategy_cls=strategy_cls,
                    multi_symbols=multi_symbols,
                    param_name_list=param_name_list,
                    backtest_params_iter=backtest_params_iter,
                    available_backtest_params_check_func=available_backtest_params_check_func,
                    file_name_func=file_name_func,
                    statistic_item_dic=statistic_item_dic,
                    engine_param_key_func=engine_param_key_func,
                    output_available_only=output_available_only,
                    open_browser_4_charts=open_browser_4_charts,
                    root_folder_name=root_folder_name,
                    multi_process=0,
                    save_stats=save_stats,
                    enable_collect_data=enable_collect_data,
                    ignore_existed_backtest=ignore_existed_backtest,
                    output_path_has_strategy_class_name=output_path_has_strategy_class_name,
                    output_separate_by_backtest_status=output_separate_by_backtest_status,
                    output_setting_json=output_setting_json,
                    file_name_include_symbol=file_name_include_symbol,
                    stg_info_duplicate_name_options=stg_info_duplicate_name_options,
                    pre_call_before_backtest=pre_call_before_backtest,
                )
                logger.info(f"启动子进程 {vt_symbol}")
        finally:
            pool.shutdown(wait=True)
            logger.info("进程池（pool）关闭")
            if future is not None and future.exception() is not None:
                logger.error(f"{future.exception()}")


def bulk_backtest_with_backtest_params_iter(
        strategy_cls: Union[Type[StrategyTemplate], Type[CtaTemplate]],
        multi_symbols: bool,
        param_name_list: List[str],
        backtest_params_iter: Iterator[Tuple[dict, list, Optional[StrategyBacktestStats]]],
        available_backtest_params_check_func: Optional[Callable] = None,
        file_name_func: Optional[Callable] = None,
        statistic_item_dic: Optional[dict] = None,
        engine_param_key_func: Optional[Callable] = None,
        output_available_only: bool = True,
        open_browser_4_charts: bool = False,
        root_folder_name: Optional[str] = None,
        multi_process: int = 0,
        save_stats: Optional[bool] = None,
        enable_collect_data=False,
        ignore_existed_backtest=False,
        output_path_has_strategy_class_name=True,
        output_separate_by_backtest_status=False,
        output_setting_json=True,
        file_name_include_symbol=False,
        short_name_with_file_name_if_exist=True,
        stg_info_duplicate_name_options=DuplicateNameOptions.raise_error,
        default_backtest_status=None,
        strategy_module_name=None,
        strategy_class_name=None,
        pre_call_before_backtest=None,
        **kwargs
):
    """
    :param strategy_cls 策略类
    :param multi_symbols 是否多合约
    :param param_name_list 回测参数名称列表
    :param backtest_params_iter 回测参数迭代器，
    :param available_backtest_params_check_func 如果希望忽略部分参数组合，可以自定义函数，对每一个组合进行筛选，False为忽略该参数
    :param file_name_func 自定义文件头名称，默认为None，所有["参数名+参数", ...]用下划线链接
    :param statistic_item_dic 策略类 统计项默认 DEFAULT_STATIC_ITEM_DIC
    :param engine_param_key_func engine param key
    :param output_available_only 仅当策略有效是才输出统计数据、图片、参数等文件
    :param open_browser_4_charts
    :param root_folder_name 策略类 保存跟目录名称,None 时为当前系统日期
    :param multi_process 0 单进程, -1 为CPU数量,正数为对应的进程数
    :param save_stats 保存统计数据，默认情况下只记录 CrossLimitMethod.open_price 的回测结果数据
    :param enable_collect_data 是否运行收集数据
    :param ignore_existed_backtest 默认为False.是否忽略以及存在的回测.即,如果当前回测在数据库中已经存在,则跳过该测试.
    :param output_path_has_strategy_class_name 默认为False.输出文件路径是否包含 策略类名称.
    :param output_separate_by_backtest_status 默认为False.输出文件路径是否包含按 backtest_status 分目录存放.
    :param output_setting_json 生成 setting json 文件
    :param file_name_include_symbol 生成文件的文件名带 symbol 用以进行区分，默认False，过长文件名可能导致系统不支持长文件名错误。
    :param short_name_with_file_name_if_exist 默认 True。如果当前回测存在 short_name 则将short_name添加到文件名末尾。
    :param stg_info_duplicate_name_options 默认 DuplicateNameOptions.raise_error。策略重名应对措施。该参数仅在 save_stats == True 的情况下启用
    :param default_backtest_status 指定默认 回测状态为 None
    :param strategy_module_name 策略的 module_name 如果非空，则取代 strategy_cls 进行动态获取
    :param strategy_class_name 策略的 class_name
    :param pre_call_before_backtest 回测前调用当前函数，主要用于动态加载使用
    """
    if pre_call_before_backtest:
        pre_call_before_backtest()
    if strategy_module_name and strategy_class_name:
        try:
            strategy_cls = load_class(strategy_module_name, strategy_class_name)
            logger.info(f"动态获取类 {strategy_module_name}.{strategy_class_name}")
        except AttributeError:
            logger.exception(f"动态获取类 {strategy_module_name}.{strategy_class_name} 异常")
            return

    if statistic_item_dic is None:
        statistic_item_dic = DEFAULT_STATIC_ITEM_DIC

    data, backtest_params_list = [], []
    for _ in backtest_params_iter:
        data.append(_[1])
        backtest_params_list.append(_)

    params_df = pd.DataFrame(data, columns=param_name_list)
    backtest_params_count = params_df.shape[0]
    strategy_class_name = strategy_cls.__name__
    # 记录所有 单一值 变量的名字
    single_valued_param_name_set = set()
    for param_name in param_name_list:
        if params_df[param_name].unique().shape[0] == 1:
            single_valued_param_name_set.add(param_name)

    multi_valued_param_name_list = [_ for _ in param_name_list if _ not in single_valued_param_name_set]
    logger.info(
        f'{strategy_class_name} 开始批量运行，包含 {len(param_name_list)} 个参数，总计 {backtest_params_count:,d} 个回测')

    # 重新包装迭代器
    backtest_params_iter = tqdm(enumerate(backtest_params_list), total=backtest_params_count)

    # 多进程情况启动进程池
    is_multi_process = multi_process not in (0, 1)
    if is_multi_process:
        # 多进程情况下启动子进程,等待消息带回来传递参数
        if multi_process == -1:
            # 默认CPU数量
            multi_process = cpu_count()

        engine = None
        pool = ProcessPoolExecutor(max_workers=multi_process)
        manager = Manager()
        # task_queue = JoinableQueue(multi_process * 2)
        task_queue = manager.Queue(multi_process * 2)
        engine_key_results_dic = manager.dict()
        lock = manager.Lock()
        process_num = 0

        def submit_new_job(finished_future: Optional[Future] = None):
            """
            用于向进程池提交任务
            当 finished_future is not None 时，代表当前函数为进程结束的回调函数，此时如果 任务队列为空，则不再想进程池添加新任务。
            """
            nonlocal process_num
            if finished_future is not None:
                if task_queue.empty():
                    logger.warning(f"任务结束，不再启动新的进程")
                    return

            process_num += 1
            name = f"process_{process_num:03d}"
            future = pool.submit(
                run_backtest_from_queue,
                strategy_cls, task_queue, engine_key_results_dic, lock,
                statistic_item_dic, multi_valued_param_name_list, name, multi_symbols
            )
            # 模块内的回调函数方法，parse会使用future对象的返回值，对象返回值是执行任务的返回值
            # 回调应该是相当于parse(future)
            future.add_done_callback(submit_new_job)
            logger.info(f"启动子进程 {name}")

        # 建立子进程实例
        for _ in range(multi_process):
            submit_new_job()

        cleanup_thread = CleanupOrcaServerProcessIntermittent()
        cleanup_thread.start()
    else:
        # 单进程准备好回测引擎
        if multi_symbols:
            engine = PortfolioBacktestingEngine()
        else:
            engine = CtaBacktestingEngine()

        pool = None
        task_queue = None
        cleanup_thread = None
        engine_key_results_dic = defaultdict(list)

    # 开始对每一种参数组合进行回测
    output_path_vt_symbol = ''
    for n, (engine_kwargs, param_values, strategy_stats_original) in backtest_params_iter:
        # 设置参数
        strategy_kwargs = {k: v for k, v in zip(param_name_list, param_values)}
        backtest_param_kwargs = dict(
            engine_kwargs=engine_kwargs,
            strategy_kwargs=strategy_kwargs,
            output_available_only=output_available_only,
            open_browser_4_charts=open_browser_4_charts,
            save_stats=save_stats,
            strategy_stats_original=strategy_stats_original,
            enable_collect_data=enable_collect_data,
            enable_join_collector=False,
            ignore_existed_backtest=ignore_existed_backtest,
            output_path_has_strategy_class_name=output_path_has_strategy_class_name,
            output_separate_by_backtest_status=output_separate_by_backtest_status,
            output_setting_json=output_setting_json,
            file_name_include_symbol=file_name_include_symbol,
            short_name_with_file_name_if_exist=short_name_with_file_name_if_exist,
            stg_info_duplicate_name_options=stg_info_duplicate_name_options,
            default_backtest_status=default_backtest_status,
        )
        backtest_param_kwargs.update(kwargs)
        # 检查参数有效性
        if available_backtest_params_check_func is not None and not available_backtest_params_check_func(
                **backtest_param_kwargs):
            continue
        cross_limit_method = engine_kwargs["cross_limit_method"] \
            if "cross_limit_method" in engine_kwargs else CrossLimitMethod.open_price
        # 设置 engine_param_key
        engine_param_key = engine_param_key_func(**engine_kwargs)
        # 设置 root_folder_name, file_name_header 参数
        root_folder_name_curr = root_folder_name
        file_name_header = None
        if file_name_func is not None:
            file_name_header = file_name_func(cross_limit_method=cross_limit_method, **backtest_param_kwargs)
            if isinstance(file_name_header, tuple):
                root_folder_name_ret, file_name_header = file_name_header
                if root_folder_name_ret is not None:
                    root_folder_name_curr = os.path.join(root_folder_name_curr, root_folder_name_ret)

        # 2021-02-01
        # 默认文件名可以为 None，以下代码废弃
        # if file_name_header is None:
        #     file_name_header = '_'.join([f"{k}{v}" for k, v in zip(param_name_list, param_values)]) \
        #                        + f'_{cross_limit_method.value}{cross_limit_method.name}'

        backtest_param_kwargs["file_name_header"] = file_name_header
        backtest_param_kwargs["root_folder_name"] = root_folder_name_curr
        # 设置进度条显示名称
        if multi_symbols:
            vt_symbols = engine_kwargs["vt_symbols"]
            description_vt_symbol = " vs ".join(engine_kwargs["vt_symbols"])
            output_path_vt_symbol = "_".join([_.split('.')[0] for _ in vt_symbols])
            if len(f'available_{strategy_class_name}_{output_path_vt_symbol}_{date_2_str(date.today())}.csv') > 255:
                output_path_vt_symbol = hashlib.md5(output_path_vt_symbol.encode('utf-8')).hexdigest()

        else:
            output_path_vt_symbol = description_vt_symbol = engine_kwargs["vt_symbol"]

        if file_name_header is not None:
            description_header = f" <{file_name_header}>"
        else:
            description_header = ""

        description = f"{strategy_class_name} [{description_vt_symbol}]{description_header}"

        backtest_params_iter.set_description(description)
        # 开始回测
        if is_multi_process:
            logger.debug("put key=%s task=%s in queue", engine_param_key, backtest_param_kwargs)
            # 多进程 参数加入队列
            task_queue.put((engine_param_key, backtest_param_kwargs), block=True)
        else:
            # 单进程直接调用
            stats_dic = run_backtest(
                strategy_cls,
                multi_symbols=multi_symbols,
                engine=engine,
                print_statistics=False,
                **backtest_param_kwargs
            )
            # 当前测试已存在因此直接跳过,或者回测没有产生交易.
            if stats_dic is None:
                continue
            # 按顺序更新参数及统计指标
            statistics_with_param_dic = OrderedDict([
                (k, v) for k, v in strategy_kwargs.items() if k in multi_valued_param_name_list])
            for k in statistic_item_dic.keys():
                statistics_with_param_dic[k] = stats_dic[k] if k in stats_dic else ''

            logger.warning("engine_param_key: %s", engine_param_key)
            engine_key_results_dic[engine_param_key].append(statistics_with_param_dic)

    # 如果是多进程，则等待全部进程结束
    if is_multi_process:
        logger.info(f"等待清空任务队列，当前任务队列还有 {task_queue.qsize()} 个任务")
        task_queue.join()
        logger.debug("等待所有进程结束")
        pool.shutdown(wait=True)
        logger.info("进程池（pool）关闭")
        cleanup_thread.is_running = False
        cleanup_thread.join()
        logger.debug("关闭 CleanupOrcaServerProcessIntermittent 线程")

    engine_keys_list = list(engine_key_results_dic.keys())
    backtest_params_count = len(engine_keys_list)
    logger.info("engine_keys_list %s", engine_keys_list)
    logger.info("param_name_list %s", param_name_list)
    logger.info("multi_valued_param_name_list %s", multi_valued_param_name_list)
    if backtest_params_count == 0:
        result_df = None
        result_available_df = None
    else:
        # 根据 engine_keys_list 单独生成每一个结果集文件
        df_list = [
            pd.DataFrame(
                engine_key_results_dic[_]
            ).rename(
                columns=statistic_item_dic
            ).drop_duplicates() for _ in engine_keys_list if _ in engine_key_results_dic]

        keys = ['_'.join([
            f"{_.value}{_.name}" if isinstance(_, CrossLimitMethod) else str(_) for _ in k
        ]) for k in engine_keys_list]
        for key, df in zip(keys, df_list):
            csv_file_path = get_output_file_path(
                f'{strategy_class_name}_{key}_{date_2_str(date.today())}.csv', root_folder_name=root_folder_name)
            xls_file_path = get_output_file_path(
                f'{strategy_class_name}_{key}_{date_2_str(date.today())}.xlsx', root_folder_name=root_folder_name)
            df['backtest_status'] = StrategyBacktestStatusEnum.Unavailable.value
            df.insert(df.shape[1] - 1, 'short_name', '')
            df.insert(df.shape[1] - 1, 'shown_name', '')
            available_df = df[df['available']]
            if available_df.shape[0] > 0:
                available_df.to_csv(csv_file_path, encoding='GBK', index=False)
                available_df.to_excel(xls_file_path, index=False)

        if backtest_params_count == 1:
            result_df = pd.DataFrame(engine_key_results_dic[engine_keys_list[0]]).rename(columns=statistic_item_dic)
            # result_df.reset_index(inplace=True)
            result_available_df = result_df[result_df['available']]
        else:
            # is_available 取交集
            is_available_s = df_list[0]['available']
            for df in df_list[1:]:
                is_available_s = is_available_s | df['available']

            # 根据 keys 横向连接 DataFrame 便于进行比较
            try:
                result_df = pd.concat(
                    df_list,
                    keys=keys,
                    axis=1,
                )
                result_available_df = result_df[is_available_s]  # .reset_index()
                # result_df.reset_index(inplace=True)
            except ValueError:
                logger.exception("合并 DataFrame 异常")
                df_list = []
                for key, df in zip(keys, df_list):
                    df['key'] = key
                    df_list.append(df)

                result_df = pd.concat(
                    df_list,
                )  # .reset_index()
                result_available_df = pd.concat(
                    [df[df['available']] for df in df_list],
                )  # .reset_index()

    if result_df is not None and result_df.shape[0] > 0:
        result_df.drop_duplicates(inplace=True)
        csv_file_path = get_output_file_path(
            f'result_{strategy_class_name}_{output_path_vt_symbol}_{date_2_str(date.today())}.csv',
            root_folder_name=root_folder_name)
        result_df.to_csv(csv_file_path, index=False, encoding='GBK')
        logger.info("总计 %d 条测试记录被保存到 %s", result_df.shape[0], csv_file_path)
        csv_file_path = get_output_file_path(
            f'result_{strategy_class_name}_{output_path_vt_symbol}_{date_2_str(date.today())}.xlsx',
            root_folder_name=root_folder_name)
        # Writing to Excel with MultiIndex columns and no index ('index'=False) is not yet implemented.
        result_df.to_excel(csv_file_path,
                           # index=isinstance(result_df.columns, pd.MultiIndex)
                           )

    if result_available_df is not None and result_available_df.shape[0] > 0:
        result_available_df.drop_duplicates(inplace=True)
        csv_file_path = get_output_file_path(
            f'available_{strategy_class_name}_{output_path_vt_symbol}_{date_2_str(date.today())}.csv',
            root_folder_name=root_folder_name)
        result_available_df.to_csv(csv_file_path, index=False, encoding='GBK')
        csv_file_path = get_output_file_path(
            f'available_{strategy_class_name}_{output_path_vt_symbol}_{date_2_str(date.today())}.xlsx',
            root_folder_name=root_folder_name)
        # Writing to Excel with MultiIndex columns and no index ('index'=False) is not yet implemented.
        result_available_df.to_excel(csv_file_path,
                                     # index=isinstance(result_available_df.columns, pd.MultiIndex)
                                     )

    # enable_join_collector
    if trade_data_collector.is_alive():
        trade_data_collector.join_queue()
    if order_data_collector.is_alive():
        order_data_collector.join_queue()

    return result_df
