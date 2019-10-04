'''
@description 【Python面向对象】多态 2019/10/04 14:41
'''

# TODO: 多态：
# 不同的对象，都实现了同一个接口，因此我们不管这个对象是什么，直接调用这个方法就可以了。

class Hero(object):
    def __init__(self):
        pass

    def skill(self):
        pass


class Xiangyu(Hero):
    def skill(self):
        print('项羽的大招：推人!....')

class Chengyaojin(Hero):
    def skill(self):
        print('程咬金的大招：回血!....')

option = input('请输入你要使用的英雄：')
hero = None
if option == '1':
    hero = Chengyaojin()
else:
    hero = Xiangyu()

hero.skill()