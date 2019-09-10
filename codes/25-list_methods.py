'''
@description 2019/09/09 23:44
'''

# 列表的常用方法：

# 1.append：在列表末尾添加元素
# JavaScript
'''
fruits = ['苹果']
fruits.push('香蕉')
'''

fruits = ['苹果']
fruits.append('香蕉')
print(fruits) # ['苹果', '香蕉']
print('='*20)

# 2.count: 统计某个元素在列表中出现的次数

word_lsit = ['to', 'be', 'or', 'not', 'to', 'be']
word_count = word_lsit.count('be')
print(word_count) # 2
print('='*20) 

# 3.extend：将一个列表中的元素追加到另外一个列表中
# 注意事项：改变原数据
# JavaScript
'''
arr = [1,2,3].concat([4,5,6])
arr = [1,2,3,...[4,5,6]]
'''

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b) 

# 列表相加不改变元数据，产生新数据
# list_c = list_a + list_b
# print(list_a) # [1, 2, 3]
# print(list_b) # [4, 5, 6]
# print(list_c) # [1, 2, 3, 4, 5, 6]

print(list_a) # [1, 2, 3, 4, 5, 6]
print(list_b) # [4, 5, 6]
print('='*20) 


# 4.index: 找出列表中第一个某个值的第一个匹配项的索引位置，如果没有找到，则抛出异常
# JavaScript：找不到 -1
'''
letter_list = ['a', 'b', 'c', 'd', 'e']
letter_position = letter_list.findIndex(item => item =='e') # 4
letter_position = letter_list.findIndex(item => item =='f') # -1
'''

letter_list = ['a', 'b', 'c', 'd', 'e']
letter_position = letter_list.index('e')
# ValueError: 'f' is not in list
# letter_position = letter_list.index('f')
print(letter_position) # 4
print('='*20) 


# 5.insert：将某个值插入到列表的某个位置
# JavaScript
'''
insert_arr = ['hello', 'world']
insert_arr.splice(1, 0, '你好')
insert_arr.splice(insert_arr.length, 0, '世界')
console.log(insert_arr) # ["hello", "你好", "world", "世界"]
'''

insert_arr = ['hello', 'world']
insert_arr.insert(1, '你好') 
insert_arr.insert(len(insert_arr), '世界') 
print(insert_arr) # ['hello', '你好', 'world', '世界']
print(len(insert_arr)) # 4
print('='*20) 

'''
@description 2019/09/10 23:47
'''

# 6.pop方法：移除列表中最后一个元素，并且返回该元素的值。

pop_list = [1, 2, 3, 4]
pop_item = pop_list.pop()
print(pop_item) # 4
print(pop_list) # [1, 2, 3]
print('='*20) 

# 7.remove方法：移除列表中第一个匹配的元素，不会返回这个被移除的元素的值。
# 如果被移除的这个值不存在列表中，则会抛出一个异常。

remove_list = [1, 2, 3, 4, 5, 1, 2]
remove_list.remove(2)
print(remove_list) # [1, 3, 4, 5, 1, 2]
print('='*20)

# 8.reverse：将列表中的元素反向存储。会更改原来列表的值

reverse_list = [1, 2, 3, 4, 5]
reverse_list.reverse() # [5, 4, 3, 2, 1]

# 切片反转list，不会改变原list数据，产生新数据
# new_reverse_list = reverse_list[-1::-1]
# print(reverse_list)  # [1, 2, 3, 4, 5]
# print(new_reverse_list) # [5, 4, 3, 2, 1]

print(reverse_list)  # [5, 4, 3, 2, 1]
print('='*20)

# 9.sort：将列表中的元素进行排序。会改变原来列表中的位置。

sort_arr = [10, 7, 3, 12, 22, 1, 2, 5, 9]
# 从小到大，顺序
# sort_arr.sort() 
# print(sort_arr) # [1, 2, 3, 5, 7, 9, 10, 12, 22]

sort_arr.sort(reverse = True)
print(sort_arr) # [22, 12, 10, 9, 7, 5, 3, 2, 1]
print('='*20)


# 10.del关键字：根据下标删除元素，改变原来列表

del_list = [10, 7, 3, 12, 22, 1, 2, 5, 9]
del del_list[0] 
print(del_list) # [7, 3, 12, 22, 1, 2, 5, 9]
print('='*20)

# 11.in关键字：使用in判断表中是否有某个元素

in_list = [10, 7, 3, 12, 22, 1, 2, 5, 9]
in_item_position = in_list.index(10)
print(in_item_position)
if 10 in in_list:
    print('True')
else:
    print('False')

print('='*20)

# 12. list函数：将其他数据类型转化为列表,不改变原数据，产生新数据

word_str = 'hello world'
new_word_list = list(word_str)
print(word_str) # hello world
print(new_word_list) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(type(new_word_list)) # list
