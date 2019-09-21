'''
@description 2019/09/21 16:23
'''

# 1.使用read函数：
# 使用read(count)函数可以从文件中读取数据，count表示要从文件中读取的数据的长度。
# 如果count没有传，那么表示读取文件中所有的数据。
# fp = open('test.txt', 'r', encoding='utf-8')
# line = fp.read(5)
'''
hello 
'''
# print(line)

'''
hello world
abc
python
'''
# string = fp.read()
# print(string)

# 2.使用readline()函数：
# 读一行的数据：使用readline可以以行的形式读取文件。

# fp = open('test.txt', 'r', encoding='utf-8')
'''
hello world

abc

python
'''
# line1 = fp.readline()
# print(line1)
# line2 = fp.readline()
# print(line2)
# line3 = fp.readline()
# print(line3)

# 用readline函数读取文件中所有的行数据
# 不能使用for循环去变量readline方法
# fp = open('test.txt', 'r', encoding='utf-8')
# first_line = fp.readline()
# for word in first_line: 
#     print(word, end=" ") # h e l l o   w o r l d

# 如果要用readline方法把文件中所有的行都读出来，只能采用while循环
'''
hello world

abc

python
'''
# while True:
#     line = fp.readline()
#     if not line:
#         break
#     print(line)

# 3.使用readlines函数
# readlines返回一个列表，列表中装的就是文件中每行的数据

# fp = open('test.txt', 'r', encoding='utf-8')
# all_lines = fp.readlines()
# for line in all_lines:
#     print(line)
# fp.close()

'''
@description 2019/09/21 17:06
'''
# 4.遍历文件指针对象
# 针对大小内存文件均有效
fp = open('test.txt', 'r', encoding='utf-8')
'''
hello world

abc

python
'''
for line in fp:
    print(line)

fp.close()