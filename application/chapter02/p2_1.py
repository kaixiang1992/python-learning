'''
@description 文字游戏 2019/09/15 23:23 page:5
'''

temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("你是小甲鱼心里的蛔虫吗?!")
    print("哼，猜中了也没有奖励!")
else:
    print("猜错了，小甲鱼心里现在想的是8!")

print("游戏结束，不玩了!")