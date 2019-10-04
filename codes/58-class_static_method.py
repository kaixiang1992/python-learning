'''
@description 【Python面向对象】类方法和静态方法 2019/10/04 15:45
'''

class Person(object):
    country = 'china'

    def eat(self):
        print('人在吃饭!....')
    
    # TODO: 类方法：第一个参数必须是cls,这个cls代表的是当前这个类
    @classmethod
    def greet(cls):
        print(cls.country)
        cls.country = 'USA'
        # print('zhiliao ketang!....')
        print(cls.country)
    
    # TODO: 静态方法：不需要传递对象或者类
    # 静态方法使用场景：不需要修改类或者对象属性的时候，并且这个方法放在
    # 这个类中可以让代码更加有管理性
    @staticmethod
    def static_methond():
        # print('hello world!...')
        print('hello %s!...'%(Person.country))


# TODO: 实例方法
p1 = Person()
# p1.eat()
# Person.eat(Person)

# TODO: 类方法
# 类方法属于这个类的，可以通过这个类去调用，也可以通过这个类的实例对象调用。
# 调用方式：
# 1.类调用
# Person.greet()
# 2.实例对象调用
# p1.greet()

# TODO: 静态方法：
# 静态方法属于类的，只能通过类名字调用。静态方法中不能调用类属性，
# 如果要调用，只能通过类名来调用。并且不需要传递任何参数
# 1.类调用
Person.static_methond()
# 2.实例对象调用
p1.static_methond()