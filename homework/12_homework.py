'''
@description 2019/08/31 23:01
'''

# 实现一个加法计算器，接收用户输入的两个数据，然后计算其相加的结果
# 使用float类型：转化用户输入整数和浮点数
inputnum1 = input('请输入数字1：')
inputnum2 = input('请输入数字2：')
total = float(inputnum1) + float(inputnum2)
print('用户输入的数值和为：%.2f'%total)
print('='*20)

# 有变量a = '12.3'，想要将其转化为整形，怎么做？
# 先将变量a = '12.3'，使用float转化为浮点数：12.3
# 再将浮点数12.3，使用int函数转化为整形12
a = '12.3'
b = float(a)
c = int(b)
print(c)