'''
@description 【Python模块和包】循环引用 2019/10/05 11:02
'''

#TODO: import b做的第一件事情就是判断b是否在sys.modules这个字典中存在
# 1.如果存在，就不再去导入b了。也就是说，就不会再去执行b模块中的代码了
# 2.如果不存在，就会导入b。然后执行b这个模块中的代码

# import sys
# print('b' in sys.modules)

# import b

from d import my_add

print('c file!...')

total = my_add(4,5)
print(total)

def c_method():
    print('c method!...')