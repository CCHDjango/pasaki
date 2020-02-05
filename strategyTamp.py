# python 策略模板
# python strategy tamplate
from constant import Order

class Strategy:
    def __init__(self,engine):
        self.engine=engine
        self.pos=0
        self.order=Order()

    def onBar(self,bar):
        raise NotImplementedError
    
    def onTick(self,tick):
        raise NotImplementedError

    def onTrade(self,trade):
        pass
    
    def onOrder(self,order):
        pass
    
    def init(self):
        pass

    def start(self):
        pass

    def buy(self,symbol,price,volume,market=''):
        # 类型判断 type judge
        try:
            assert isinstance(symbol,str)
            assert isinstance(price,float)
            assert isinstance(volume,float)
        except AssertionError:
            raise ValueError('your strategy buy(...) function has type error,argument 1 : string, 2 : float ,3 : float. ERROR CODE : 100')
        
        # 数值判断 number judge
        try:
            assert price>0
            assert volume>0
        except AssertionError:
            raise ValueError('your strategy buy(...) function has number error,order`s price and volume must > 0. ERROR CODE : 101')
        self.sendOrder('buy',symbol,price,volume,market)

    def sell(self,symbol,price,volume,market=''):
        try:
            assert isinstance(symbol,str)
            assert isinstance(price,float)
            assert isinstance(volume,float)
        except AssertionError:
            raise ValueError('your strategy sell(...) function has error input type,argument 1 : string, 2 : float ,3 : float. ERROR CODE : 100')

        # 数值判断 number judge
        try:
            assert price>0
            assert volume>0
        except AssertionError:
            raise ValueError('your strategy sell(...) function has number error,order`s price and volume must > 0. ERROR CODE : 101')
        self.sendOrder('sell',symbol,price,volume,market)

    def cancel(self,orderID):
        pass
    
    def cancelAll(self):
        pass

    def sendOrder(self,direction,symbol,price,volume,market):
        '''生成订单并发向交易所'''
        self.order.symbol=symbol
        self.order.price=price
        self.order.volume=volume
        self.order.market=market
        self.order.direction=direction
        self.engine.sendOrder(self.order)
