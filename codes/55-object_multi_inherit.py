'''
@description 89.【Python面向对象】多继承及其注意事项 2019/10/04 11:58
'''

# 在python的面向对象编程中，是支持多继承的，也即一个类可以继承多个父类

class Ma(object):
    def run(self):
        print('马在奔跑!....')
    
    def eat(self):
        print('马在吃草!....')
    
class Lv(object):
    def lamo(self):
        print('驴在拉磨!....')

    def eat(self):
        print('驴再吃麦秆!....')

# TODO: 继承Ma, LV
class Luozi(Ma, Lv):
    # TODO: 重写父类eat方法
    def eat(self):
        # TODO: 如果不想要按照__mro__的顺序执行父类的方法，那么可以通过以下方式执行！
        # TODO: 父类名.方法名(self, 可选参数)
        Lv.eat(self)
        print('骡子在吃稻谷!....')

lz = Luozi()
# lz.run()
# lz.lamo()
# TODO: (<class '__main__.Luozi'>, <class '__main__.Ma'>, <class '__main__.Lv'>, <class 'object'>)
print(Luozi.__mro__) 
# Luozi类没有eat方法，优先执行Ma类的eat方法，依次类推执行顺序直到objet也没有eat方法才返回异常
# TODO: AttributeError：'Luozi' object has no attribute 'eat'
lz.eat()