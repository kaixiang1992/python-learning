'''
@description 2019/09/15 18:34
'''

# 函数返回值

def greet(username,age):
    # result = [username, age]
    # return result
    return username,age

# value = greet('zhiliao', 18)
# print(value) # ['zhiliao', 18]

# value = greet('zhiliao', 18)
# print(value) # ('zhiliao', 18)
# print(type(value)) # tuple元祖

username,age = greet('zhiliao', 18)
print(username) # zhiliao
print(age) # age