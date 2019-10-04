'''
@description 86.【Python面向对象】重写父类的方法 2019/10/04 10:44
'''

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('人在吃饭!....')


class Student(Person):
    # 1.如果父类的方法不能满足子类的需求，那么可以重写这个方法，以后对象调用同名
    # 方法的时候，就会执行子类的这个方法。
    # 2.虽然父类的方法不能完全满足子类的需求，但是父类的方法的代码还是需要执行，
    # 那么可以通过super这个函数来调用父类的方法。
    # 3.super函数的用法：super(类名,self).方法名([可选参数])
    # 例：super(Student, self).__init__(name, age)
    # 例：super(Student, self).eat()
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)

    # TODO: 重写父类Person的eat方法
    def eat(self):
        # super(Student, self).eat()
        print('学生在吃饭!....')
    
    def greet(self):
        print('hello, my name is %s, my age is %s'%(self.name, self.age))

student = Student('zhiliao', 18)
student.eat()
student.greet()