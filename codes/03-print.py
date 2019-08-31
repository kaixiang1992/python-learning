'''
@description 2019/08/31 21:45
'''

# print函数：打印字符串和变量
# print函数打印字符串
print('打印字符串')
print('='*20)

# 格式化输出

# 字符串类型变量的格式化：
# 字符串类型：%s
teachername = 'zhiliao'
print('字符串类型变量的格式化：')
print('my tearcher name is %s'%teachername)

# 整形变量的格式化
# 整形：%d
age = 27
print('整型变量的格式化：')
print('my age is %d'%age)

# 浮点类型变量的格式化
# 浮点类型：%f
# 注意事项：浮点类型的格式化默认保留5位精度
price = 18.9123
print('浮点类型变量的格式化(默认5位精度)：')
print('apples\'s price is %f'%price) 
print('浮点类型变量的格式化指定2位精度：')
print('apples\'s price is %.2f'%price)

# 同时打印多个变量
# 注意事项：使用元祖模式传递
username = 'kaixiang'
userage = 27
usergender = 'boy'
print('同时打印多个变量：使用元祖模式传递...')
print('my name is %s,my age is %d,gender is %s'%(username, userage, usergender))

# 字符串末尾打印一个变量
userweight = 60
print('字符串末尾打印一个变量：')
print('my weight is',userweight)

# 注意事项：
# 如果是其他数据类型，使用%s的方式进行格式化
# 那么其实，Python是首先将这个数据转化为字符串
# 再进行格式化。
print("将int类型数据用%s输出："%'%s')
print('my weight is %s'%userweight)
