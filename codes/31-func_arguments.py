'''
@description 2019/09/15 15:53
'''

# 形参：定义函数时指定的参数。
# 例：a,b
def add(a,b):
    result = a + b
    print(result)


# 实参：就是在调用函数的时候传递进去的参数。

# 1.位置参数：按照形参中给定的参数的顺序。
add(1,2) # 3

# 2.关键字参数：在传递参数的时候，可以按照形参的名字给定参数。
add(a=2, b=2) # 4
add(b=3, a=2) # 5

# 3.混合参数：在传递参数的时候，即包括位置参数也包括关键字参数
# 混合参数的注意事项：位置参数必须在关键字参数的前面

add(1, b=2) # 3 
add(3, b=3) # 6
print('='*20)

#  TypeError：add() got multiple values for argument 'a'
# 多值错误
# add(4, a=5)

# 位置参数必须在关键字参数的前面
# SyntaxError: positional argument follows keyword argument
# add(b=5, 1)



'''
@description 2019/09/15 16:47
'''

# *args和**kwargs：缺省的位置参数和关键字参数。

##########缺省的位置参数#############

def plus(*args):
    # print(args) tuple元祖
    result = 0
    for x in args:
        result += x
    print(result)

plus(1,2,3,4,5,6,7,8) # 36
plus(1,2,3,4,5,6,7,8,9,10,11,12) # 78
print('='*20)

##########缺省的关键字参数#############

def keyworddef(**kwargs):
    print(kwargs) # dict字典

keyworddef(a=1, b=2, c=3, d=4) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print('='*20)


# *args,**kwargs：这两个参数组合，可以代表任意的参数
# 注意事项：位置参数必须在关键字参数的前面

def mergeargs(*args, **kwargs):
    print(args) # (1, 2, 3, 4)
    print(kwargs) # {'a': 5, 'b': 6, 'c': 7}

mergeargs(1,2,3,4,a=5,b=6,c=7)
print('='*20)

'''
@description 2019/09/15 17:27
'''
##########默认参数#############
# 注意事项：
# 1.默认参数只能在其他参数后面，但是放在缺省参数的前面
# 2.如果默认参数和缺省的位置参数、关键字参数组合在一起，那么要放在缺省参数的前面

# 错误语法：
# def greet(age=18, username)

# def greet(username, age=18):
#     print(username)
#     print(age)

# greet('zhiliao') # zhiliao 18

# 错误语法：
# def greet(*args, **kwargs, age=19)

def greet(age=19, *args, **kwargs):
    print(age) # 20
    print(args) # ()空元组
    print(kwargs) # {'username': 'zhiliao'}

greet(20, username='zhiliao')