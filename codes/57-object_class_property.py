'''
@description 【Python面向对象】类属性和实例属性 2019/10/04 15:08
'''

class Person(object):
    #TODO: 类属性
    country = 'china'

    def __init__(self, name):
        #TODO: self这个对象
        self.name = name
        # self.country = country

    def greet(self):
        # TODO: 如果对象上没有country属性，那么通过self.country和Person.country的
        # 效果是一样的，都是访问Person的类属性

        # TODO: 如果给定向绑定了country属性，那么通过self.country访问到的就是这个对象
        # self上的属性，通过Person.country访问到的就是类属性。
        print('hello my name is %s, i am come from %s'%(self.name, self.country))

# 实例属性：
# 绑定到对象上的属性就是实例属性
# 实例属性只有在当前对象上有作用

# p1 = Person('zhiliao')
# p1.age = 18
# print('p1 attribute name is %s, p1 attribute age is %d'%(p1.name, p1.age))

# p2 = Person('zhiliao')
# TODO: AttributeError:'Person' object has no attribute 'age'
# print('p2 attribute name is %s, p2 attribute age is %d'%(p2.name, p2.age))
# print('='*30)


# 类属性：
# 如何在类中定义类属性
# 类属性可以通过对象进行访问
# 如果通过对象修改类属性，那么其实不是修改类属性，而是在这个对象上面重新定义了
# 一个名字相同的实例属性。

p1 = Person('zhiliao')
# TODO: 实例属性，并没有修改类属性

# TODO: 实例属性
# p1.country = 'earth'
# TODO: hello my name is zhiliao, i am come from earth
# print(p1.country)

# 类属性
# hello my name is zhiliao, i am come from china
p1.greet()

p2 = Person('ketang')
# TODO: 实例属性，并没有修改类属性

# TODO: 实例属性
# p2.country = 'USA'
# TODO: hello my name is ketang, i am come from USA
# print(p2.country)

# 类属性
# hello my name is ketang, i am come from china
p2.greet()


# 要正确修改类属性，只能通过类名的方式修改
# 类名.xxxx属性名
# Person.country = 'abc'
# print(Person.country)