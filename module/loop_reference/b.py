'''
@description 【Python模块和包】import语句原理 2019/10/05 09:53
'''
#TODO: import c做的第一件事情就是判断b是否在sys.modules这个字典中存在
# 1.如果存在，就不再去导入c了。也就是说，就不会再去执行c模块中的代码了
# 2.如果不存在，就会导入c。然后执行c这个模块中的代码
# import c

from c import c_method
from d import my_add

print('hello world!...')

my_add(2,3)

print('b end!...')