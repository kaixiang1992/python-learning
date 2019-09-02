'''
@description 2019/09/01 13:14
'''

# 猜数字游戏
# 设定游戏结果，记录游戏次数

# if input_value > value:
#     print('大了')
# elif input_value < value:
#     print('小了')
# else:
#     print('猜对了')

print('game start...')
value = 75 # 游戏设定值
times = 1 # 猜的次数
input_value = float(input('开始游戏，请输入数字：'))
while input_value != value:
    if input_value > value:
        print('大了')
    else:
        print('小了')

    times += 1
    input_value = float(input('继续游戏，请输入数字：'))

print('game over,you are successful, you used %d chances...'%times)