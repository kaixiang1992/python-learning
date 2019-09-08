'''
@description 2019/09/08 12:57
'''

# 字符串转义：

# 1. \：在行尾--续行符
# 注意事项：书写代码时行尾使用\换行符，输出打印执行时还是为一行字符串

text = 'hello \
world'
print(text) # hello world

# 2. \n：换行符
# 注意事项：\n后的字符串，换行输出

wrap_text = 'hello \n world'
print(wrap_text) 
'''
hello
 world
'''

# 3. \'：转移单引号
odd_quotes_text = 'apple\'s price is $0.5'
print(odd_quotes_text) # apple's price is $0.5

# 4.\"：转义双引号
double_quotes_text = "apple\"s price is $0.5"
print(double_quotes_text) # apple"s price is $0.5

# 5.\t：转义tab制表符
# 注意事项：使用\t转化为一个键盘tab的空格字符 

tab_text = 'hello\tworld'
print(tab_text) # hello   world

# 6. \：转义反斜杠

slash_text = 'hello \\ world'
print(slash_text) # hello \ world

'''
@description 2019/09/08 13:14
'''

# 原生字符串
# 原生字符串不会对字符串中任何字符进行转义，你写了什么，这个字符串就是什么，达到一种所见即所得的效果。
# 语法：r'xxx'

# 未使用原生字符串语法默认转义换行符
escape_text = 'abc\ndef'
print(escape_text)
'''
abc
def
'''

# 使用r'xxx',raw原生字符串
raw_text = r'abc\ndef'
print(raw_text) # abc\ndef