'''
@description 【Python】单例设计模式 2019/10/04 16:55
'''

# TODO:单例模式
# 某个类或者模型在整个程序运行中最多只能有个对象被创建
# 我们可以判断，如果User这个类没有创建对象，那么久创建一个对象保存在某个地方
# 以后如果要创建对象，我会去判断，如果之前已经创建了一个对象，那么就不再创建
# 而是直接把之前那个对象返回回去

class User(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name

user1 = User('zhiliao')
user2 = User('ketang')
print(user1.name)
print(user2.name)
print(id(user1))
print(id(user2))