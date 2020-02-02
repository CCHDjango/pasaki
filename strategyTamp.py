# python 策略模板
# python strategy tamplate

class Strategy:
    def __init__(self,engine):
        self.engine=engine
        self.pos=0

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

    def buy(self,symbol,price,volume):
        pass

    def sell(self,symbol,price,volume):
        pass

    def cancel(self,orderID):
        pass
    
    def cancelAll(self):
        pass