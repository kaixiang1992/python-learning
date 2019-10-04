'''
@description 【Python异常】异常及其处理（2） 2019/10/04 19:31
'''

# TODO: 自定义异常需要继承自`Exception`类
class ArgumentError(Exception):
    def __init__(self, *args, **kwargs):
        temp_args = args + ('参数错误',)
        super(ArgumentError, self).__init__(*temp_args, **kwargs)

def greet(username, age):
    if not isinstance(username, str):
        # raise TypeError('username must be a string')
        raise ArgumentError('username must be a string')
    
    if not isinstance(age, int):
        # raise TypeError('age must be a int')
        raise ArgumentError('age must be a int')

    print('my name is %s, my age is %d'%(username, age))

# greet('zhiliao', 18)

try:
    greet(18, '18')
except Exception as error:
    print(error.args)