'''
@description 2019/08/30 22:40
'''

# 字符串与字符串相加为拼接字符串
# a = '1'
# b = '2'
# c = a + b
# print(c) # 12
# print(type(c)) # str

# 任意字符串与数字相加，会发生类型错误提示，如下：
# TypeError：can only concatenate str (not "int") to str
# a = '1'
# b = 2
# c = a + b

a = '1'
b = '2'
c = int(a) + int(b)
print(c) # 3
print(type(c)) # int
print('='*20)

# 转换为整形：`使用int函数`
# 1.将浮点类型个转化为整形：会把小数点后面的干掉，只保留整数部分
float_num = 4.98765
int_num = int(float_num)
print(int_num) # 4
print(type(int_num)) # int
print('='*20)

# 2.将字符串类型转化为整形：字符串中只能为纯数字才能转化成功。
# 注意事项：包含任意非数字的字符串都会转化失败。包括小数点都不行
# str_num = '1234b'
# str_num = '1234.9'
# ValueError：invalid literal for int() with base 10: '1234b'
str_num = '1234'
int_strnum = int(str_num)
print(int_strnum) # 1234
print(type(int_strnum)) # int
print('='*20)

# 转化为字符串类型：`使用str函数`
# 3.将整形、浮点类型转化为字符串：没有任何的约束，直接使用str函数即可
intnum1 = 123
floatnum1 = 100.123
str_intnum1 = str(intnum1)
str_floatnum1 = str(floatnum1)
print(str_intnum1) # 123
print(type(str_intnum1)) # str
print(str_floatnum1) # 100.123
print(type(str_floatnum1)) # str
print('='*20)

# 转化为浮点数类型：`使用float函数`
# 4.将整形转换为浮点类型：没有任何的约束，直接使用float函数即可
num = 1
ft_num = float(num)
print(ft_num) # 1.0 
print(type(ft_num)) # float
print('='*20)

# 5.将字符串转化为浮点类型：在字符串中，不能出现除小数点以外的任意非字符。否则会转化失败。
# str_ftnum = '123.'
# ft_strnum = float(str_ftnum)
# print(ft_strnum) # 123.0

# str_ftnum = '123.a'
# str_ftnum = '123a'
# ft_strnum = float(str_ftnum)
#  ValueError: could not convert string to float: '123.a'

str_ftnum = '123.123'
ft_strnum = float(str_ftnum)
print(ft_strnum) # 123.123
print(type(ft_strnum)) # float
print('='*20)