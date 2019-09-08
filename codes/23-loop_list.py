'''
@description 2019/09/08 22:32
'''

# 列表的遍历
fruits = ['苹果', '香蕉', '橙子', '菠萝']

'''
苹果
香蕉
橙子
'''
# for循环版本
for x in fruits:
    print(x)

print('='*20)


'''
苹果
香蕉
橙子
'''
# while循环版本
index = 0
length = len(fruits)
while index < length:
    fruit = fruits[index]
    print(fruit)
    index += 1