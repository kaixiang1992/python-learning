'''
@description 【Python模块和包】__all__变量的作用 2019/10/04 22:01
'''

# __all__ = ['global_zhiliao', 'greet', 'Person']
__all__ = ('global_zhiliao', 'greet', 'Person')

global_zhiliao = 'zhiliao'

def greet():
    print('hello world')

class Person(object):
    def __init__(self):
        print('Person init method...')