'''
@description 【Python知识补充】三目运算符 2019/10/05 14:03
'''

#TODO: 三目运算符：主要用来简化条件判断的，语法为：
# 条件 ？满足条件的结果 : 不满足条件的结果
# 而在`python中不存在三目运算符`，但其实可以通过if..else..模拟这种行为

a = 5
b = 2
# 以下代码的意思：如果a>b，那么返回1，否则返回0
c = 1 if a>b else 0

print(c)