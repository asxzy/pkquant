from rqalpha.api import *


# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    logger.info("init")
    context.s1 = "rb1809.XSGE"
    update_universe(context.s1)
    # 是否已发送了order
    context.fired = False

    d = all_instruments(type='Future')
    print(d)


def before_trading(context):
    pass


# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    # 开始编写你的主要的算法逻辑

    # bar_dict[order_book_id] 可以拿到某个证券的bar信息
    # context.portfolio 可以拿到现在的投资组合状态信息

    # 使用order_shares(id_or_ins, amount)方法进行落单

    # TODO: 开始编写你的算法吧！
    if not context.fired:
        # security: 标的代码
        # amount: 期望的最终数量
        # style: 参见order styles, None代表MarketOrder
        # side: ‘long’/’short’，平空单还是多单，默认为多单。
        # pindex: 在使用set_subportfolios创建了多个仓位时，指定subportfolio 的序号, 从 0 开始, 比如 0为 指定第一个 subportfolio, 1 为指定第二个 subportfolio，默认为0。
        # order_target(context.s1, 1 , style=MarketOrderStyle(), side='long', pindex=0)
        context.fired = True
