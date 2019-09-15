'''
@description 2019/09/15 22:00
'''

# sort列表排序

numbers = [21, 13, 35, 17, 5]
# numbers.sort()
# print(numbers) # [5, 13, 17, 21, 35]

numbers.sort(reverse=True)
print(numbers) # [35, 21, 17, 13, 5]
print('='*20)

# sort字典排序
# sort方法：会改变原来列表的排序
# sorted函数：不会改变原来的列表的顺序，而是返回一个排序后的新列表

from functools import cmp_to_key

persons = [
    {"username": "zhangsan", "age": 20},
    {"username": "lisi", "age": 18},
    {"username": "zhaoliu", "age": 21},
    {"username": "wangwu", "age": 20}
]

def cmp(a, b):
    # 如果返回的是一个大于0的值，那么代表 a>b
    # 如果返回的是一个小于0的值，那么代表 a<b
    # 如果返回的是一个等于0的值，那么代表 a=b
    if a.get('age') > b.get('age'):
        return 1
    elif a.get('age') < b.get('age'):
        return -1
    else:
        if a.get('username') > b.get('username'):
            return 1
        else:
            return -1

'''
[
    {'username': 'lisi', 'age': 18}, 
    {'username': 'wangwu', 'age': 20}, 
    {'username': 'zhangsan', 'age': 20}, 
    {'username': 'zhaoliu', 'age': 21}
]
'''
# persons.sort(key = cmp_to_key(cmp)) 
# print(persons)

new_persons = sorted(persons, key = cmp_to_key(cmp))
print(persons)

'''
[
    {'username': 'lisi', 'age': 18}, 
    {'username': 'wangwu', 'age': 20}, 
    {'username': 'zhangsan', 'age': 20}, 
    {'username': 'zhaoliu', 'age': 21}
]
'''
print(new_persons)

print('='*20)