'''
@description 2019/09/02 23:44
'''

# range()函数：
# 为指定整数生成一个数字序列（可迭代对象），有如下三种语法：
'''
range(stop) # 默认从0到stop的数字序列
range(start, stop)
range(start, stop, steep)
'''
# 注意事项：无论选择哪一种，它的参数只能是整数

# 1. for循环字符串
userconuntry = 'I am Chinese'
for x in userconuntry:
    print(x, end=" ")

print("")
print('for finished....')


# 2.求1-10之间的和
# for循环版本
fortotal = 0
for i in range(11):
    fortotal += i

print('for result is %d'%fortotal)

# while循环版本
whilenum = 0
whiletotal = 0
while whilenum <= 10:
    whiletotal += whilenum
    whilenum += 1

print('while result is %d'%whiletotal)

# 3.统计'python papijiang papa mama'中p出现的个数
lettertotal = 0
str = 'python papijiang papa mama'
for ecah in str:
    if ecah == 'p':
        lettertotal += 1

print('letter p total times is %d'%lettertotal)

# 4. 九九乘法表

# for循环版本
# 循环行
for rows in range(1, 10):
    # 循环列
    for columns in range(1, rows + 1):
        print('%d * %d = %d'%(columns, rows, rows * columns), end=" ")
    print("")

print('for 9*9 finished....')

# while循环版本
# 行
whilerows = 1
# 列
whilecolumns = 1

# 循环行
while whilerows <= 9:
    # 循环列
    while whilecolumns <= whilerows:
        print('%d * %d = %d'%(whilecolumns, whilerows, whilerows * whilecolumns), end=" ")
        whilecolumns += 1
    print("")
    whilecolumns = 1
    whilerows += 1

print('while 9*9 finished....')