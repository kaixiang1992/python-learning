'''
@description 2019/09/15 18:53
'''

# 函数中变量的作用域：

# 1.局部变量：函数中的变量，不能在外面使用

def greet():
    username = 'zhiliao'
    print('hello %s'%username)

greet()

# NameError:name 'username' is not defined
# print(username)

# 2.全局变量：全局变量是在函数或者某个代码块外面定义的变量，可以在函数中使用

userage = 27

def takeage():
    print('my age is %d'%userage)

takeage()
print(userage)
print('='*20)

'''
@description 2019/09/15 19:24
'''

# global关键字：如果想在函数或者某个代码块中修改全局变量，那么应该使用global关键字。

globalusername = 'zhiliao'

def greetclass():
    # globalusername = 'ketang'
    # print('hello %s'%globalusername) # hello ketang

    global globalusername
    globalusername = 'ketang'
    print('hello %s'%globalusername) # hello ketang
  
greetclass()
# print(globalusername) # zhiliao
print(globalusername) # ketang
print('='*20)

'''
@description 2019/09/15 20:47
'''

# 针对可变数据类型：列表+字典
# 如果在函数中确实想要修改全局变量的persons的指向，那么就要global关键字。
# 如果在函数中只是想要对全局变量中的元素进行增删改查，可以不需要使用global关键字。

persons = ['张三', '李四']
def add_persons(name):
    # persons.append(name)
    global persons
    persons = []
    print(persons)

add_persons('王五') 
# print(persons) # ['张三', '李四', '王五']
print(persons) # []