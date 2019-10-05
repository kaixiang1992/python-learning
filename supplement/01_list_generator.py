'''
@description 【Python知识补充】列表生成式 2019/10/05 13:46
'''

#TODO: 列表生成式

# 1.生成1-100的列表

# values1 = []
# for x in range(1, 101):
#     values1.append(x)

values1 = [x for x in range(1, 101)]

print(values1)
print('='*30)

# 2.取1-100之间所有的偶数

# values2 = []
# for x in range(1,101):
#     if x%2 == 0:
#         values2.append(x)

values2 = [x for x in range(1, 101) if x%2 == 0]

print(values2)