'''
程序的入口
'''

import sys
import os

# 为项目在解释器中添加环境变量
sys.path.append(os.path.dirname(__file__))


from core import src
# 开始执行项目函数
if __name__ == '__main__':

    src.run()



