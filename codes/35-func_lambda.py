'''
@description 2019/09/16 21:56
'''

persons = [
    {"username": "zhangsan", "age": 20},
    {"username": "lisi", "age": 18},
    {"username": "zhaoliu", "age": 21},
    {"username": "wangwu", "age": 20}
]

def cmp(x):
    return x.get('age') # 根据年龄进行排序

'''
[
    {'username': 'zhaoliu', 'age': 21}, 
    {'username': 'zhangsan', 'age': 20}, 
    {'username': 'wangwu', 'age': 20}, 
    {'username': 'lisi', 'age':18}
]
'''
# 1.不适用cmp_to_key进行字典排序
# persons.sort(key=cmp, reverse=True)
# print(persons)
# print('='*20)

# 2.lambda表达式
persons.sort(key=lambda x:x.get('age'))
print(persons)
print('='*20)


# 自己手动写一个计算器：可以模仿python自带的sort函数实现一个做计算器运算的函数。

a = 10
b = 20

def calculate(x, y, func):
    result = func(x, y)
    return result

total = calculate(a, b, lambda x,y:x+y)
minus = calculate(a, b, lambda x,y:x-y)
print(total) # 30
print(minus) # -10