'''
@description 【Python模块和包】模块查找路径 2019/10/04 21:08
'''

from tools import my_request
my_request.get_request('https://www.baidu.com')

import sys
print(sys.path)