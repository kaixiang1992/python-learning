'''
@description 【Python模块和包】__all__变量的作用 2019/10/04 22:01
'''

#TODO: __all__

# 1.如果实在模块中写了这个变量，将控制from xxx import * 的行为
from zhiliao import *
print(global_zhiliao)
greet()
p1 = Person()

# 2.如果在包中__init__.py文件中，那么它将控制着from 包 import * 的行为。
from tools import * 
my_request.get_request('https://www.baidu.com')
my_file.save_data('1234...')