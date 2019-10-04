'''
@description 【Python面向对象】__new__方法 2019/10/04 16:16
'''

# TODO: __new__方法
# __new__方法是用来控制这个类创建对象的执行逻辑。这个方法在对象还没有创建之前就会执行的。
# 而__init__方法是在对象创建完毕后才执行。

class Car(object):
    def __new__(cls, *args, **kwargs):
        print('new method....')
        return super(Car, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print('init method....')

car = Car()
print(car)