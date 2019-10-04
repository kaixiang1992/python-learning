'''
@description 88.【Python面向对象】新式类和旧式类 2019/10/04 11:29
'''

# 旧式类：没有指定任何父类
# 在python2.2版本之前，所有的类都是旧式类
class Personold:
    def __init__(self, name):
        self.name = name

# 在旧式类中，子类不能使用super函数来调用父类的函数
# 不支持__slots__,property等高阶语法
class Studentold(Personold):
    def __init__(self, name):
        print('这是Studentold旧式类的代码...')
        #TODO: 旧式类中，如果想要调用父类的方法，那么必须通过以下方式：
        #TODO: 父类名.方法名(self, 其他的参数)
        Personold.__init__(self, name)

studentold = Studentold('zhiliao')
print(studentold.name) 
print(type(studentold)) # <class '__main__.Studentold'>
print(studentold.__class__) # <class '__main__.Studentold'>
print('='*20)


# 新式类：
class Person(object):
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)

student = Student('zhiliao')
print(student.name)
print(type(student))
print(student.__class__)
