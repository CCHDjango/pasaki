# pasaki trade engine

class TradeEngine:
    def __init__(self):
        self.capital=0
        self.cash=0
        self.position=0
        self.order=None
        self.trade=None
        self.orderList=[]
        self.tradeList=[]
        self.strategy=None
    
    