'''
@description 2019/10/02 18:22
'''

# 封装/继承/多态

# 继承
# 父类/基类

# 继承：可以使用其他类作为自己的父类，那么父类中的方法和公有属性都可以被子类调用。
# 继承的好处：可以让子类节省代码，实现更多的功能。

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print('人在吃饭.....')

    def run(self):
        print('人在奔跑.....')

# Student继承自Person类
class Student(Person):
    pass

student = Student('zhiliao', 18)
student.eat()
student.run()
print(student.name)
print(student.age)