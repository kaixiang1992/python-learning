'''
@description 2019/08/31 23:43
'''

# bool类型：真和假，只有两个值，就是True和False

a = True
b = False

if b:
    print('True')
    print('a条件满足')
else:
    print('False')
    print('条件不满足')

print('finished')
print('='*20)

'''
@description 2019/09/01 10:34
'''
# 比较运算符
# 1. ==运算符：是否相等
# 注意事项：2 != '2' 类型不同，即不相等
print('==运算符：是否相等')
num1 = 2
num2 = 2
if num1 == num2:
    print('相等')
else: 
    print('不相等')

# 2. != 不相等：是否不相等
# rootname = input('请输入账号(root):')
print('!=不相等：是否不相等')
rootname = 'admin'
if rootname != 'root':
    print('您不是该站点的管理员')
else:
    print('您可正常使用站点系统')

# 3. >：是否大于
print('>：是否大于')
age = 18
if age > 17:
    print('你可以去网吧上网了')
else:
    print('未成年人不能进网吧上网')

# 4. <: 是否小于
print('<: 是否小于')
personage = 17
if personage < 18:
    print('未成年人不能进网吧上网')
else: 
    print('你可以去网吧上网了')

# 5. >=：是否大等于
print('>=：是否大等于')
personage2 = 19
if personage2 >= 18:
    print('你可以去网吧上网了')
else:
    print('未成年人不能进网吧上网')

# 6. <=：是否小等于
print('<=：是否小等于')
personage3 = 17
if personage3 <= 17:
    print('未成年人不能进网吧上网')
else: 
    print('你可以去网吧上网了')

# 7.条件a and 条件 b：
# 注意事项：自由条件a和条件b都满足才成立
# 类似于JavaScript： && 且功能
print('条件a and 条件b')
userage = 24
if userage >= 18 and userage <= 24:
    print('你是青年人')
else:
    print('你不是青年人')

# 8. 条件a or 条件b:
# 注意事项：只要条件a 或者 条件b 中的一个满足，就成立：
# 类似于JavaScript：|| 或功能
print('条件a or 条件b:')
userage2 = 16
if userage2 < 18 or userage2 > 24:
    print('你不是青年人')
else:
    print('你是青年人')

# 9. not条件a:
# 注意事项：如果条件a为True,那么返回False.如果条件a为False，那么返回True
# 类似于JavaScript： !true即为：false，!false即为：true
print('not条件a:')
person1 = '中国人'
person2 = '南非人'
if not person1 == '南非人':
    print('可以上撤侨战舰')
else:
    print('不可以上撤侨战舰')

'''
@description 2019/09/01 11:34
'''
# 10.elif语句
# 类似于JavaScript else if()
print('='*20)
print('elif语句....')
day = input('请输入今日星期(0-6):') # input输入函数值为str类型
day = float(day)
day = int(day)

if day == 0:
    print('星期日')
elif day == 1:
    print('星期一')
elif day == 2:
    print('星期二')
elif day == 3:
    print('星期三')
elif day == 4:
    print('星期四')
elif day == 5:
    print('星期五')
elif day == 6:
    print('星期六')
else:
    print('你输入的星期不对')