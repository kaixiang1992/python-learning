'''
@description 2019/09/11 22:53
'''

# 什么是元祖：
# 元祖的使用与列表相似。不同之处在于元祖是不可修改的，元祖使用圆括号，而列表使用中括号。

# 定义元祖

# 1.使用逗号的方法：

# a_tuple = 1,2,3
# print(a_tuple) # (1, 2, 3)
# print(type(a_tuple)) # tuple

# 2.使用圆括号的方式

# a_tuple = (1,2,3)
# print(a_tuple) # (1, 2, 3)
# print(type(a_tuple)) # tuple

# 3.使用tuple函数
# list  => tuple

# a_list = [1,2,3]
# a_tuple = tuple(a_list)
# print(a_tuple) # (1, 2, 3)
# print(type(a_tuple)) # tuple

# 4.定义只有一个元素的元祖

# a_tuple = 12,
# b_tuple = (13,)
# print(a_tuple) # (12,)
# print(type(a_tuple)) # tuple
# print(b_tuple) # (13,)
# print(type(b_tuple)) # tuple

'''
@description 2019/09/11 23:26
'''

# 1.下标操作

# a_tuple = ('a','b','c')
# a = a_tuple[0]
# print(a) # a

# 2.切片操作：跟列表和字符串的切片操作一样。

# a_tuple = ('zhiliao',18,'python')
# reverse_a_tuple = a_tuple[::-1]
# print(reverse_a_tuple) # ('python', 18, 'zhiliao')

# 3.解组操作：
# 注意事项：有些时候我们只想要元祖中的某个值，不需要所有的值，那么我们通过_来作为省略
# 和`JavaScript解构赋值`类似

# a_tuple = ('zhiliao',18,'python')
# username = a_tuple[0]
# userage = a_tuple[1]
# classname = a_tuple[2]
# username,userage,classname = a_tuple
# print(username) # zhiliao
# print(userage) # 18
# print(classname) # python

# a_tuple = ('zhiliao',18,'长沙')

# ValueError：too many values to unpack (expected 2)，未使用_匿名赋值
# username,userage = a_tuple

# username,userage,_ = a_tuple
# print(username) # zhiliao
# print(userage) # 18

# 4. count方法：获取元素中某个值出现的次数，和列表中的用法相同。

# a_tuple = ('zhiliao',18,'长沙')
# result = a_tuple.count('长沙') # 1
# result = a_tuple.count('杭州') # 0
# print(result) 

# 5.index方法：获取元祖中某个值的下标，和列表中的用法相同。获取不到抛出异常

a_tuple = ('zhiliao',18,'长沙')
position = a_tuple.index('长沙') # 2

# ValueError：tuple.index(x): x not in tuple
# position = a_tuple.index('西湖')
print(position) # 2


# 元祖存在的意义和应用场景：
# 1.元祖在字典中可以当做key来使用，而列表是不可以的。
# 2.在函数中有时候要返回多个值，一般采用元祖的方式。

def response():
    return 'zhiliao',18,'长沙'

response_data = response()
print(response_data) # ('zhiliao', 18, '长沙')
print(type(response_data)) # tuple

# 3.在一些不希望用户修改值的场景下使用元祖来代替列表。