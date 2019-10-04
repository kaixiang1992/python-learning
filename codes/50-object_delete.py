'''
@description 2019/10/02 17:28
'''
import sys

# 1.析构函数，也即__del__方法：
# 只要这个对象在内存中即将被消灭的时候，就会调用这个方法.

class Person(object):
    def __init__(self):
        self.name = 'zhiliao'
        print('构造函数....')
    
    def greet(self):
        print('hello, 我的名字是：%s'%(self.name,))
    
    def __del__(self):
        print('析构函数.....我即将被消灭了....')
    
p = Person()
p.greet()
print(sys.getrefcount(p)) #

p2 = p 
print(sys.getrefcount(p)) # 3
print(sys.getrefcount(p2)) # 3
# 先会打印下面输出文字
print('先打印了这段输出文本，再去执行__del__方法.....')
# 再去执行__del__方法

# 2.引用计数：python中的对象使用引用计数的方式实现的。也即如果没有任何对象引用到一块内存，
# 那么python会把这块内存回收。
# 可以使用sys.getrefcount(object)来获取一个对象的引用次数