'''
@description 【Python异常】异常及其处理（1） 2019/10/04 18:51
'''

try:
    # TODO: 感觉可能会崩溃的代码
    a = 1
    b = 0
    # c = a/float(b)
    # print(c)
    print(d)
# except Exception as error: # 接收所有异常
#     print(error)
except ZeroDivisionError: # 除0错误
    print('除以0错误!...')
except NameError as error:
    print('变量声明错误!...')
    print(error)
else:
    print('try中执行的代码没有抛出异常!...')
finally:
    print('不管程序有没有抛出异常，都会执行的代码!...')