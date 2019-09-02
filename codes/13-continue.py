'''
@description 2019/09/02 23:08
'''

# continue语句：
# 跳出本轮循环并开始下一轮循环
# 注意事项：在开始下一轮循环之前，会先测试循环条件

# 打印1-10，除5外的所有的整数
print('while start.....')

index = 1
while index <= 10:
    if index == 5:
        # 注意：当index = 5满足条件后，continue跳出前，确保一定
        # index += 1，否则陷入index == 5中无限循环
        # print(index)
        index += 1 
        continue
    print(index, end=" ")
    index += 1

print("")
print('while finished....')

# 打印1-20，所有偶数
print('while start....')

num = 1
while num <= 20:
    # if num % 2 == 0:
    #     print(num, end=" ")
    #     num += 2
    # else:
    #     num += 1
    #     continue
    if num % 2 != 0: # 奇数
        num += 1
        continue
    print(num, end=" ")
    # 当找到第一个偶数后，num += 2参与下次循环，减少循环次数
    num += 2

print("")
print('while finished....')