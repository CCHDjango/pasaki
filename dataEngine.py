'''
python 数据处理模块
pasaki data module
1，先遍历data下所有的文件
2，凡是符合命名要求的数据文件遍历进行回测

notice :  数据命名格式 -> 2020-btc-1day.json  year-symbol-frequency.json

默认遍历:json
'''
import os
import sys
import json

class DataEngine:
    def __init__(self):
        self.dataPath=""
    
    def loadJson(self):
        pass

    def setting(self,path=''):
        '''function : data engine init'''
        if path:
            # 如果用户自己设置数据位置的情况
            self.dataPath=path
        else:
            self.dataPath=os.getcwd()+'/data/'
    


