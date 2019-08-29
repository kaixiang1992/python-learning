"""
@description 2019/08/29 23:40:00 
"""

cup = '水'
print(cup)
# 变量是一个容器，用来存储值的

english = 99
math = 98 
chinese = 97

# print(99+98+97) #294
print('英语成绩:',english)
total = english + math + chinese
print(total) #294

# 使用变量替代值，语义更加明确

# 使用变量替代值，以后这个值修改了，我们只要去修改这个变量的值就可以了，后面的代码不用改
# english = 100
# print('英语成绩：', english) #100
# total = english + math + chinese
# print(total) #295

# 如果变量是第一次出现然后赋值，那么就会新建一个变量并且给这个变量赋值

# 如果这个变量之前出现过了，那么以后赋值就不会新建变量，而是重新赋值
# english = 100
# print('英语成绩：', english) #100

# 如果这个变量之前从来没有出现过，而直接使用，那么就会报变量名未定义的错误
# print(country)
# NameError name 'country' is not defined

# 不能使用Python内置关键字作为变量声明，关键字：and、or、def、class、import、print、return等。会报语法错误提示。
# from = '东土大唐而来'
# print(from)
# SyntaxError: invalid syntax