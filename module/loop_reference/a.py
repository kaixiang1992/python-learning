'''
@description 【Python模块和包】import语句原理 2019/10/05 09:53
'''

import sys

#TODO: 1.执行b模块中的全部代码
# import b

#TODO: 2.将b这个模块添加到sys.modules这个字典中
# sys.modules的作用：用来判断某个模块是否已经被导入到当前文件中
# print(sys.modules)
# print(type(sys.modules)) # dict
# is_in_modules = 'b' in sys.modules
# print(is_in_modules) # True

#TODO: 3.在当前文件中，创建一个变量叫b，引用b这个模块
# total = b.my_add(1,2)
# print(total)


#TODO: 1.执行b模块中所有代码
from b import my_add

#TODO: 2.将b这个模块添加到sys.modules中
# print(sys.modules)
is_in_modules = 'b' in sys.modules
print(is_in_modules)

#TODO: 3.创建一个变量叫my_add，指向了b模块下的my_add函数
total = my_add(2,3)
print(total)