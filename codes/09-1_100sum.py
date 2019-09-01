'''
@description 2019/09/01 12:11
'''

# 求1-100整数之和
# 注意事项：
# 确保：index += 1，不然陷入死循环 index每次循环即为1，index <= 100均成立
total = 0
index = 1
while index <= 100:
    total += index
    index += 1

print('print finished....')
print('total is %d'%total) # 5050