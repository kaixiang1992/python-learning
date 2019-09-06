'''
@description 2019/09/06 22:29
'''

# 字符串常用方法：

# 1. find方法：返回查找字符串的下标操作。如果返回的是-1，代表的是没有查到该字符串。从0开始。
# rfind方法：从右到左，和find方法类似。

# text = 'hello zhiliao'
# position = text.find('zhiliao') # 6
# position = text.find('python') # -1
# position = text.rfind('zhiliao') # 6
# position = text.rfind('python') # -1

# 2. index方法：和find非常类似。只不过当查不到这个字符的时候，不是返回-1，而是抛出一个异常。
# rindex方法：从右到左开始查找
# ValueError: substring not found

# text = 'hello zhiliao'
# position = text.index('zhiliao') # 6
# position = text.index('python') # 6
# position = text.rindex('zhiliao') # 6
# position = text.rindex('python') # 6
# print(position)


# 3. len方法：获取字符串的长度

# text = 'hello world' # 11
# print(len(text))

# 4. count方法：用来获取子字符串在原来字符串中出现的次数。
# 存在即返回大于0的次数，不存在返回0

# text = 'hello python python'
# times = text.count('python') # 2
# times = text.count('javascript') # 2
# print(times) 

# 5. replace方法：新创建一个字符串，把原来字符串中的某个字符串替换为你想要的字符串。
# replace(oldstr, newstr, count)
# 注意事项：新创建的一个字符串，不会改变原字符串
# 不指定count参数默认替换全部，如需替换一个oldstr请传入count
# count <= 0 替换全部，大于0替换指定个数

# text = 'hello python python'
# new_text = text.replace('python', 'javascript')
# print(text) # hello python python
# print(new_text) # hello javascript javascript

# new_text = text.replace('python', 'javascript', 1)
# print(text) # hello python python
# print(new_text) # hello javascript python

# 6. split方法：按照给定的字符串进行分割。返回的是一个列表。

# text = 'hello python python'
# text_arr = text.split(" ") 
# print(text_arr) # ['hello', 'python', 'python']
# print(type(text_arr)) # list类型
# for item in text_arr:
#     print(item)