'''
@description 2019/09/02 22:21
'''

# while循环九九乘法表
'''
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4
1 * 3 = 3  2 * 3 = 6  3 * 3 = 9
.....
'''

print('test....')
print('1 * 2 = 2', end=" ")
print('2 * 2 = 4')
print('test finished....')

# 行
rows = 1
# 列 
columns = 1

print('while start....')
# 第一个循环：行
while rows <= 9:
    while columns <= rows:
        # 在这个地方打印的时候，打印的是同一行的列
        # 因此不需要换行，所以修改end=" "，让其在一行中打印
        print('%d * %d = %d'%(columns, rows, rows * columns), end=" ")
        columns += 1
    # 为了使用换行符，打印完一行就要换行
    print("")
    rows += 1
    columns = 1 # rows每循环迭代一次，重新初始化columns，否则每循环一次rows，columns变+1

print('while finished....')
