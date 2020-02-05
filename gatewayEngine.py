# python 对接交易所接口抽象
# pasaki -> exchange

try:
    from websocket import create_connection
except ModuleNotFoundError:
    raise ModuleNotFoundError('Please install websocket-client package')

class Gateway:
    def __init__(self):
        pass