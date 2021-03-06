'''
@description 2019/09/09 23:06
'''

# 列表的基本操作

# 1. 列表嵌套：列表中可以存储任何数据类型，当然也包括列表自身类型。
# 也即：列表中可以存储列表

print('列表嵌套 '*4)
'''
1
2
3
a
b
c
'''
test_list = [1, 2, 3, ['a', 'b', 'c']]
for x in test_list:
    if type(x) == list:
        for sub_x in x:
            print(sub_x)
    else:
        print(x)


# 2.列表相加：列表相加，相当于把后面一个列表的数据追加到第一个列表后面。
print('列表相加 '*4)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # [1, 2, 3, 4, 5, 6]


# 列表的切片操作：跟字符串的切片操作是一样的
# [start:end:step]
# start开始位置：包括开始位置，不写默认从0开始
# end结束位置：会取到结束位置前一个元素。不写默认到最后位置。
# step步长：默认为1，如果步长为负数，则从右到左。如果步长正数，则从左边到右边。
# 切片可以赋值。
# 逆序：list[-1::-1]

print('切片操作 '*4)

d = c[0:3]
print(d) # [1,2,3]

# e = c[0::2] # 获取奇数
e = c[::2]
print(e) # [1, 3, 5]

# [1, 2, 3, 4, 5, 6]
# -6 -5 -4 -3 -2 -1
#          end    start
# 默认步长为1，从左向右切片，从-1位置即6开始往左切片无后续元素即为空[]
f = c[-1:-4]
print(f) #  []

g = c[-2:]
print(g) # [5, 6]

# 逆序数组
reverse_list = c[-1::-1]
print(reverse_list) # [6, 5, 4, 3, 2, 1]