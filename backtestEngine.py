# pasaki backtest engine

class Backtest:
    def __init__(self):
        self.capital=0      # 总资产
        self.cash=0         # 账户余额
        self.position=0     # 策略持仓
        self.order=None     # 最近一次订单
        self.trade=None     # 最近一次成交
        self.orderList=[]   # 订单列表
        self.tradeList=[]   # 成交列表
        self.strategy=None  # 策略指针
    
    def loadData(self,dataPath):
        ''' 加载历史数据'''
        pass
    
    def crossTrade(self):
        ''' 成交撮合'''
        pass

    def updateAccount(self):
        ''' 每次成交计算之后，都更新一次账户信息'''
        pass
    
    def sendOrder(self,order):
        ''' 发送订单'''
        pass

    def run(self):
        ''' 回测循环'''
        pass