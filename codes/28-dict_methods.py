'''
@description 2019/09/14 13:38
'''

# 字典常用方法：

# 1.clear：清除字典所有的项。

person1 = {'username': 'zhiliao', 'age': 18, 'weight': 160, 'height': 180}
person2 = person1
print(person1) # {'username': 'zhiliao', 'age': 18}
print(person2) # {'username': 'zhiliao', 'age': 18}

# 使用clear清除了，person1和person2的引用
# person1.clear()
# print(person1) # {}
# print(person2) # {}

person1 = {}
print(person1) # {}
print(person2) # {'username': 'zhiliao', 'age': 18}
print('='*20)

'''
@description 2019/09/14 14:10
'''

# 2.get：访问字典中那个键对应的那个值。不会像dict[key]那样抛出异常

username = person2.get('username') 

# userlikes = person2.get('likes')
# print(userlikes) # None none

# 指定一个默认值，在没有获取到值的时候
userlikes = person2.get('likes', 'develop')

print(username) # zhiliao
print(userlikes) # develop have
if userlikes: 
    print('have')
else: 
    print('none')
print('='*20) 

# 3.pop：用来获得对应于给定键的值，然后将这个键盘和值的项从字典中删除。
# 会返回这个值

test_dict = {'username': 'zhiliao', 'age': 18, 'weight': 160, 'height': 180, 'type': 'school', 'classname': 'develop'}
# test_username = test_dict.pop('username')

# 没有pop的键时，会抛出异常
# KeyError:'userlikes'
# test_userlikes = test_dict.pop('userlikes')

# print(test_dict) # {'age': 18, 'weight': 160, 'height': 180, 'type': 'school', 'classname': 'develop'}
# print(test_username) # zhiliao

# 4.popitem：随机的移除字典中的一项。因为字典是无序的，所有是随机的。
# 会返回这个弹出项，类型为元祖 tuple

randomitem = test_dict.popitem()
print(randomitem) # ('classname', 'develop')
print(type(randomitem)) # tuple
print(test_dict) # {'username': 'zhiliao', 'age': 18, 'weight': 160, 'height': 180, 'type': 'school'}
print('='*20)

# 5.update：用一个字典去更新另一个字典，如果碰到相同的键，则会覆盖。

a = {'url': 'https://www.baidu.com'}
b = {'url': 'https://www.jd.com/', 'title': '京东', 'address': 'beijing'}

a.update(b)
print(a) # {'url': 'https://www.jd.com/', 'title': '京东', 'address': 'beijing'}
print(b) # {'url': 'https://www.jd.com/', 'title': '京东'}
print('='*20)

# 6.setdefault: 如果字典中包含给定键，则返回该键的值。
# 如果字典中不包含给定键，则返回为该键设置的值，并且会设置值到字典中。

str_dict = {'username': 'zhiliao', 'age': 18}
str_username = str_dict.setdefault('username', 'kaixiang')
print(str_username) # zhiliao
print(str_dict) # {'username': 'zhiliao', 'age': 18}
# str_classname = str_dict.setdefault('classname') # None
str_classname = str_dict.setdefault('classname', 'python') # python
print(str_classname) # python
print(str_dict) # {'username': 'zhiliao', 'age': 18, 'classname': 'python'}