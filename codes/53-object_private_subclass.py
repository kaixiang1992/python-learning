'''
@description 87.【Python面向对象】子类不能继承父类的私有变量 2019/10/04 11:03
'''

# 重点：在类的继承中，私有属性和私有方法不能被子类继承的

class Person(object):
    def __init__(self, name):
        # TODO: 私有属性
        self.__name = name
        # TODO: 保护属性
        self._age = 18

    def greet(self):
        print('hello, my name is %s'%(self.__name, ))

    def __run(self):
        print('Person class is running....')


class Student(Person):
    # TODO: 重写方法
    def greet(self):
        # TODO:  AttributeError：'Student' object has no attribute '_Student__name'
        print('hello, my name is %s'%(self.__name, ))
        # print('hello, my age is %d'%(self._age, ))

# p1 = Person('zhiliao')
# p1.greet()

student = Student('zhiliao')
student.greet()