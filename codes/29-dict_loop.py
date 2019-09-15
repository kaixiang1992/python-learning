'''
@description 2019/09/15 12:38
'''

# 遍历字典

person = {"username": "zhiliao", "age": 18, "weight": 160, "height": 180, "address": "长沙"}

# 1.遍历字典中所有的key：使用keys方法，这个方法将所有的键以列表的方式返回。

# username age weight height address
for key in person.keys():
    print(key, end=" ") 

print("")
print('='*20)

# 2.遍历字典中所有的value：使用values方法，这个方法将所有的值以列表的方式返回。

# zhiliao 18 160 180 长沙
for value in person.values():
    print(value, end=" ")

print("")
print("="*20)

# 3.遍历字典中所有的键值对：使用items方法，这个方法将所有的键和值以列表的方式返回。

# 返回item类型为tuple元祖，使用元祖解构key和value
# for item in person.items():
#     print(item)
#     print(type(item)) # tuple
#     itemkey,itemval = item
#     print('key is %s, val is %s'%(itemkey, itemval))

'''
key is username, value is zhiliao
key is age, value is 18
key is weight, value is 160
key is height, value is 180
key is address, value is 长沙
'''
for item,val in person.items():
    print('key is {key}, value is {value}'.format(key = item, value = val))

