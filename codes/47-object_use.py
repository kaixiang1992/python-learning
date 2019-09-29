'''
@description 2019/9/29 22:03
'''

# id函数：返回对象在内存中存储的标识值。


# 1.定义类必须使用class关键字，然后继承自object类
# 2.在类中定义方法，第一个参数必须是self，self代表的是当前这个对象

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('*'*30)
        print(id(self))
        print('*'*30)
    
    def eat(self):
        print('人这个对象在吃饭！....')

# 3.使用类创建一个对象：类名()
p1 = Person('zhiliao', 18)
print(p1.name)
print(p1.age)
# 调用方法
p1.eat()
print('='*30)
print(id(p1))
print('='*30)

# p2 = Person('ketang', 20)
# print(p2.name)
# print(p2.age)