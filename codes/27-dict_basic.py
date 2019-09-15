'''
@description 2019/09/14 10:14
'''

# 1.创建字典：对象形式创建字典

person = {"username": "kaixiang", "age": 27, "weight": 60, ('skills',): 'python'}
print(person) # {'username': 'kaixiang', 'age': 27, 'weight': 60, ('skills',): 'python'}
print(type(person)) # dict
print('='*20)

# 使用dict函数创建字典

dict_person = dict(username="kaixiang", age=27, weight=60, height=170)
print(dict_person) # {'username': 'kaixiang', 'age': 27, 'weight': 60}
print(type(dict_person)) # dict
print('='*20)


'''
@description 2019/09/14 11:50
'''
# 2.基本操作

# len(dict)：返回字典的长度
print(len(person))
print('='*20) # 4

# dict[key]：获取dict对应key的值

# 注意事项：获取不到key的值报错
# userlike = person['likes']
# KeyError：'likes'

username = person['username'] # kaixiang
skills = person[('skills',)] # python
print(username) # kaixiang
print(skills)
print('='*20)

# dict[key]=value：设置dict中键为key的值value，如果字典中不存在key的这一项，那么自动的添加进去。

person['username'] = 'zhangsan'
person['likes'] = 'game' 
# {'username': 'zhangsan', 'age': 27, 'weight': 60, ('skills',): 'python', 'likes': 'game'}
print(person)
print('='*20)

# del dict[key]：删除dict中键为key的这一项

# 注意事项：获取不到key报错
# del person[('eats',)]
# KeyError：('eats',)

del person['likes']
print(person) # {'username': 'zhangsan', 'age': 27, 'weight': 60, ('skills',): 'python'}
print('='*20)

# key in dict：检查dict中是否包含键为key的这一项

if 'username' in person: # True
    print(True)
else:
    print(False)

if ('foods',) in person: # False
    print(True)
else:
    print(False)

print('='*20)

# 字典中的键可以是任意的不可变类型，比如：浮点类型、整形、字符串或者元祖

new_dict = {123.4: 123.4, 1: 1, 'desc': 'test_dict', ('a','b','c'): 'a,b,c'}
print(new_dict) # {123.4: 123.4, 1: 1, 'desc': 'test_dict', ('a', 'b', 'c'): 'a,b,c'}
print(type(new_dict)) # dict