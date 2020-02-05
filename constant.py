# pasaki constants


class Bar:
    def __init__(self):
        self.symbol=''    # K 线的品种代号
        self.frequency='' # K线时间周期
        self.open=0       # 开盘价
        self.high=0       # 收盘价
        self.low=0        # 最低价
        self.close=0      # 最高价
        self.time=''      # K线时间
        self.market=''    # 来自市场

class Tick:
    def __init__(self):
        self.time=''   # 当前tick的时间
        self.price=0   # tick成交价格
        self.volume=0  # tick成交量
        self.symbol='' # 数据品种
        self.market='' # 市场来源

class Order:
    def __init__(self):
        self.symbol=''    # 下单品种
        self.price=''     # 下单价格
        self.volume=''    # 订单数量
        self.market=''    # 下单目标市场
        self.id=''        # 订单id
        self.direction='' # 下单方向

class Trade:
    def __init__(self):
        self.symbol='' # 下单品种
        self.price=''  # 成交价格
        self.volume='' # 成交数量
        self.market='' # 下单目标市场
        self.id=''     # 订单id
        self.time=''   # 成交时间