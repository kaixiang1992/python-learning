'''
@description 2019/9/29 22:50
'''

# 1.受保护的属性和方法：
# 有时候类中的属性或者方法不想被外界掉用，但还是可以被外界调用，那么就叫做受保护的属性或者方法。
# 受保护的属性或者方法，使用一个下划线开头。

class Women(object):
    def __init__(self, age):
        self._age = age

women1 = Women(19) 
# 以下代码可以打印出_age，但这样做是违背开发者意愿的。
print(women1._age) # 19
print('='*30)


# 2.私有属性和方法：
# 有时候类中的属性或者方法不想被外界调用，那么就可以使用定义成私用属性或者私有方法。
# 私有属性或者方法使用两个下划线开头。

class Account(object):
    def __init__(self, a_id, password):
        # TODO: 私有变量
        self.__a_id = a_id
        self.__password = password
    
    # TODO: 私有方法
    def __account_list(self):
        print('我是一个私有方法!....')
        return [11, -11, 22, -22]
    # TODO: 公共方法
    def get_account_list(self, password):
        if self.__password == password:
            return self.__account_list()
        else:
            return None

account1 = Account('baidu.com', '123456')
# AttributeError:'Account' object has no attribute 'password'
# print(account1.password)
# print(account1.__password)
# account1.__account_list()
account1_result = account1.get_account_list('123456')
print(account1_result)

# 注意事项：
# 私有方法或属性不是100%不能访问，以上方式，可以通过_ClassName__password来访问，但这样做不推荐.
print('不推荐直接访问私有属性或者方法!....')
print(account1._Account__password) # 123456
account1._Account__account_list()