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