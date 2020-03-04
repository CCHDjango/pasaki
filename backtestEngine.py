# pasaki backtest engine
# 回测引擎读取的数据是轮询指定的文件夹，每个历史数据都回测一次
# 尽管股票不能做空，但是策略也是能做空的
from constant import Bar

class Backtest:
    def __init__(self):
        self.capital=0      # 总资产
        self.cash=0         # 账户余额，一定是大于等于0
        self.position=0     # 策略持仓，小于零则是做空的仓位，大于零则是做多的仓位
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
        ''' 成交撮合，虽然用户下单函数的时候是需要价格的，但是回测的时候是指定价格成交的,
        先判断下单的方向，以买单为例，先判断原本策略是否有持仓，如果是空仓，再下多单是要先平掉原来
        的空仓再开多仓，但是如果下单的价格乘以数量大于空仓的价值加上账户余额，那么该单直接拒绝掉
        如果是原本持有多仓，则直接判断账户余额是否足够即可，卖单同理。
        '''
        buyCrossPrice=(self.bar.open+self.bar.high)/2 # 以当根K线的最高价和开盘价作为买单的成交价
        sellCrossPrice=(self.bar.open+self.bar.low)/2 # 以当根K线的最低价和开盘价作为卖单的成交价
        for order in self.orderList:
            if order.direction=='buy':
                if self.position<0:
                    if abs(self.position) * buyCrossPrice + self.cash < buyCrossPrice * order.volume:
                         # 不够钱的情况
                         return
                    else:
                        # 一定够钱下单的判断分支
                        # 先平掉空仓再开多仓
                        if order.volume>abs(self.position):
                            order.volume+=self.position
                            self.position=0
                            self.cash+=abs(self.position) * buyCrossPrice
                            self.position=order.volume
                            self.cash-=order.volume * buyCrossPrice
                        else:
                            # 只平
                            self.cash+=order.volume*buyCrossPrice
                            self.position+=order.volume
                else:
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
    
    def positionJudgement(self,direction,price,volume):
        '''原本持仓不为0时，坐持仓判断'''
        