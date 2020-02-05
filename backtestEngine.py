# pasaki backtest engine
from constant import Bar

class Backtest:
    def __init__(self):
        self.capital=0      # 总资产
        self.cash=0         # 账户余额
        self.position=0     # 策略持仓
        self.order=None     # 最近一次订单
        self.orderID=0      # 回测用的订单id
        self.trade=None     # 最近一次成交
        self.orderList=[]   # 订单列表
        self.tradeList=[]   # 成交列表
        self.strategy=None  # 策略指针
        self.bar=Bar()      # 最新一条K线
    
    def run(self):
        ''' 回测循环'''
        pass
    
    def loadData(self,dataPath):
        ''' 加载历史数据'''
        pass

    def loadStrategy(self,strategy):
        '''从外部获取策略对象的引用'''
        self.strategy=strategy
    
    def crossTrade(self):
        ''' 成交撮合'''
        buyCrossPrice=(self.bar.open+self.bar.high)/2 # 以当根K线的最高价和开盘价作为买单的成交价
        sellCrossPrice=(self.bar.open+self.bar.low)/2 # 以当根K线的最低价和开盘价作为卖单的成交价
        for order in self.orderList:
            if order.direction=='buy':
                pass
            else:
                pass

    def updateAccount(self):
        ''' 每次成交计算之后，都更新一次账户信息'''
        pass
    
    def sendOrder(self,order):
        ''' 发送订单'''
        self.orderID+=1
        order.id=str(self.orderID)
        self.orderList.append(order)
    
    def cashJudgement(self,price,vloume):
        '''买单时判断余额是否足够,如果够则返回True 否则False'''
        pass
    
    def positionJudgement(self,volume):
        '''原本持仓不为0时，坐持仓判断'''
        pass