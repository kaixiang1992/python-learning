'''
@description 2019/09/03 21:03
'''

# 1.for循环实现九九乘法表
# 循环行：
for rows in range(1,10):
    # 循环列
    for columns in range(1, rows + 1):
        print('%d * %d = %d'%(columns, rows, rows * columns), end=" ")
    print("")

# 2.实现一个计算体脂率的程序
# 体脂率计算公式如下：
'''
成年女性的体脂率计算公式：
    参数a = 腰围(cm) * 0.74
    参数b = 体重(kg) * 0.082 + 34.89
    体脂肪重量(kg) = a - b
    体脂率 = (身体脂肪总量÷体重) * 100

成年男性的体脂率计算公式：
    参数a = 腰围(cm) * 0.74
    参数b = 体重(kg) * 0.082 + 44.74
    体脂肪重量(kg) = a - b
    体脂率 = (身体脂肪总量÷体重) * 100
'''
# 性别
sex = input('请输入性别man或者women：')
while True:
    if sex == 'man' or sex == 'women':
        break
    else:
        sex = input('请重新输入性别man或者women：')
# 腰围
waistline = float(input('请输入腰围(cm):'))
# 体重
weight = float(input('请输入体重(kg):'))

# 参数a
waistline_result = waistline * 0.74
# 参数b
weight_result = weight * 0.082

if sex == 'man': 
    # 男性
    weight_result += 44.74
else:
    # 女性
    weight_result += 34.89

# 体脂肪重量(kg) = a - b
total_weight = waistline_result - weight_result
# 体脂率 = (身体脂肪总量÷体重) * 100
bodyfaterate = (total_weight / weight) * 100
print('输入性别：%s,腰围：%scm,体重：%skg。计算体脂率结果：%d'%(sex, waistline, weight, bodyfaterate))

# 3.找出(print出来)1000以内的水仙花数
# 什么叫做水仙花数：
# 一个n(n>=3)的正整数，它的每位上的数字的n次幂之和等于他本身。
# 例如：1^3 + 5^3 + 3^3 = 153,那么153就是水仙花数
# 153 = 1^3 + 5^3 + 3^3
# 1 153 370 371 407
'''
# 百位：
# 取整除 250 // 100 = 2
print(253 // 100) 
# 十位：
# 1. 取余 253 % 100 = 53
# 2. 取整除 53 % 10 = 5
print(253 % 100 // 10) 
# 个位：
# 1. 取余 253 % 100 = 53
# 2. 取余 53 % 10 = 3
print(253 % 100 % 10) 
'''

for num in range(1, 1000):
    a = num // 100
    b = num % 100 // 10
    c = num % 100 % 10
    if num == a ** 3 + b ** 3 + c ** 3:
        print('%d^3 + %d^3 + %d^3 = %d'%(a,b,c,num))