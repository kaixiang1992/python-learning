'''
@description 2019/09/04 23:22
'''

# 字符串的下标
# 下标操作：字符串实际上就是跟一个容器一样，也可以跟列表和元祖一样进行下标操作

username = 'zhiliao'
# print(username[0]) # z
# print(username[1]) # h
# print(username[2]) # i
# print(username[-1]) # o
# print(username[-2]) # a

'''
@description 2019/09/05 23:24
'''

# 切片操作
# 类似于range函数：range(start, end)
# 1.起始位置：切片操作包括开始位置。负数从后面开始，最后一个元素是-1。
# 2.结束位置：切片操作包括的是结束位置前面的一个元素。负数从后面开始，最后一个元素是-1。
# 3.步长：代表每次取值的跨度。如果没有设置，默认为1。正数表示从左到右，负数表示从右到左。
# 逆序：从后面往前开始走。所以起始位置应该是-1，然后要往前面走，那么应该指定步长为-1,然后要取到所有的值，那么结束位置应该离开留空。

numbers = '123456789'
# numbers[start:end:step] #[开始位置:结束位置:步长]

# temp = numbers[0:3] # 123

# temp = numbers[6:9] # 789

# temp = numbers[-9:-6] # 123

# temp = numbers[1:] # 23456789

# temp = numbers[-3:] # 789

# temp = numbers[0::2] # 13579

# 如果步长是正数，那么就是从左到右。如果步长是负数，那么就是从右到左。

# temp = numbers[-1::-1] # 987654321

temp = numbers[-1::-2] # 97531

print(temp)
