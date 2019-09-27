'''
@description 2019/9/27 23:30
'''

# 人物class类
class Person(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age
    def greet(self):
        print('我是%s，我今年%s岁了....'%(self.username, self.age))

p1 = Person('zhangsan', 18)
p1.greet()


# 汽车class类
class Car(object):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def travel(self):
        print('%s汽车正在行驶，当前速度：%sKm/h'%(self.brand, self.speed))

car1 = Car('宝马', 100)
car1.travel()

