'''
@description 2019/09/03 23:34
'''

# 1.使用单引号或者双引号括起来的。(在python中，双引号和单引号都可以用来生成字符串)
# 2.但是如果你开头使用的是单引号，那么结尾必须使用单引号。就是前后要一致。

text = 'hello world'
print(text) 
print(type(text)) # str

# 3.如果想要存储多行的字符串，那么可以使用六个单引号或者六个双引号。
# 4.如果想要在写代码的时候将一行字符串放到多行中显示，但是真正生成字符串的时候，不需要换行，那么可以在每一行的末尾加上\。

# break_text = '''hello 
# world'''
break_text = '''hello \
world'''
print(break_text)
print(type(break_text)) # str

# 5.在python3中，字符串分为两种类型：
# 1）str：unicode字符串
# 2）bytes：经过编码后的字符串，是一种字节码。适用于保存在磁盘上或者网络上传输。

bytes_text = b'hello world'
print(bytes_text) # b'hello world'
print(type(bytes_text)) # bytes