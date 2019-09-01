'''
@description 2019/09/01 11:46
'''

# 什么是循环：
# 循环是在满足特定条件的情况下，重复执行某段代码。

# 打印1-10所有的整数：
# 注意事项：
# 确保：index += 1，不然陷入死循环 index每次循环即为1，index <= 10均成立
print('print start....')
index = 1
while index <= 10:
    print(index)
    index += 1 

print('print finished....')