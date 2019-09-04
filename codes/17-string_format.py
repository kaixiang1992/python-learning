'''
@description 2019/09/04 22:51
'''

# 使用%方式进行字符串格式化：
# 字符串：使用%s
# 整形：使用%d
# 浮点类型：使用%f。默认6位精度
# 如果想要指定小数点后的位数。可以使用%.nf来表示。n为1表示一位小数，2表示两位小数，依次类推。

age = 18
text = 'my age is %d'%age
print(text)

price = 10.4
banana_price = 'banana price is %.2f'% price
print(banana_price)

# 使用format函数的形式：
# 1.使用位置参数占位符
course = 'python'
school = 'zhiliao'
greet_placehoolder = 'i love {}, i study in {}'.format(course, school) # i love python, i study in zhiliao
print(greet_placehoolder)

# 2.使用关键字参数占位符
# 注意事项：关键字参数亦可变量名重名。

# i love python, i study in zhiliao
# greet = 'i love {arg1}, i study in {arg2}'.format(arg1 = course, arg2 = school) 

greet = 'i love {course}, i study in {school}'.format(course = course, school = school) 

print(greet)
