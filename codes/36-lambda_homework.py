'''
@description 2019/09/16 22:52
'''

# 函数式编程练习：
# list()函数：强制转换为list列表

# 1.使用filter函数过滤掉小于3的数。
# filter函数的用法：
# filter(函数，列表)

filter_a = [1,2,3,4,5,6,7,8,9]
filter_result = filter(lambda x:True if x>2 else False, filter_a)
print(filter_result)
print(type(filter_result)) # filter
print(list(filter_result)) # [3, 4, 5, 6, 7, 8, 9]
print('='*20)


# 2.使用map函数将以下数组中的数扩大10倍
# map函数的用法：
# map(函数,列表)

map_a = [1,2,3,4,5,6,7,8,9]
map_result = map(lambda x: x*10, map_a)
print(map_result)
print(type(map_result)) # map
print(list(map_result)) # [10, 20, 30, 40, 50, 60, 70, 80, 90]
print('='*20)

# 3.使用reduce函数求以下列表中数值之和
# reduce函数的用法：
# reduce(函数，列表)

from functools import reduce

reduce_a = [1,2,3,4,5,6,7,8,9]
reduce_result = reduce(lambda x,y: x+y, reduce_a)
print(reduce_result) # 45
print(type(reduce_result)) # int