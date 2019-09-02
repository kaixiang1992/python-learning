'''
@description 2019/09/02 22:42
'''

# break语句:
# 终止当前循环，跳出循环体

# num累加至5时，退出循环
print('while start.....')
num = 1
while num <= 10:
    print(num)
    if num == 5:
        break
    num += 1
print('while finished.....')


# 猜数字游戏break
print('Game Start....')
value = 70 # 设定中奖值
times = 1 # 参与次数
input_value = float(input('请输入任意数字参与游戏：'))

while True:
    if input_value > value:
        print('你输入的大了')
    elif input_value < value:
        print('你输入的小了')
    else:
        break
    input_value = float(input('继续输入任意数字参与游戏：'))
    times += 1
print('Game Finished, You are Successful, You used %d chances'%times)