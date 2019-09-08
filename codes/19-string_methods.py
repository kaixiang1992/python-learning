'''
@description 2019/09/06 22:29
'''

# 字符串常用方法：

# 1. find方法：返回查找字符串的下标操作。如果返回的是-1，代表的是没有查到该字符串。从0开始。
# rfind方法：从右到左，和find方法类似。

# text = 'hello zhiliao'
# position = text.find('zhiliao') # 6
# position = text.find('python') # -1
# position = text.rfind('zhiliao') # 6
# position = text.rfind('python') # -1

# 2. index方法：和find非常类似。只不过当查不到这个字符的时候，不是返回-1，而是抛出一个异常。
# rindex方法：从右到左开始查找
# ValueError: substring not found

# text = 'hello zhiliao'
# position = text.index('zhiliao') # 6
# position = text.index('python') # 6
# position = text.rindex('zhiliao') # 6
# position = text.rindex('python') # 6
# print(position)


# 3. len方法：获取字符串的长度

# text = 'hello world' # 11
# print(len(text))

# 4. count方法：用来获取子字符串在原来字符串中出现的次数。
# 存在即返回大于0的次数，不存在返回0

# text = 'hello python python'
# times = text.count('python') # 2
# times = text.count('javascript') # 2
# print(times) 

# 5. replace方法：新创建一个字符串，把原来字符串中的某个字符串替换为你想要的字符串。
# replace(oldstr, newstr, count)
# 注意事项：新创建的一个字符串，不会改变原字符串
# 不指定count参数默认替换全部，如需替换一个oldstr请传入count
# count <= 0 替换全部，大于0替换指定个数

# text = 'hello python python'
# new_text = text.replace('python', 'javascript')
# print(text) # hello python python
# print(new_text) # hello javascript javascript

# new_text = text.replace('python', 'javascript', 1)
# print(text) # hello python python
# print(new_text) # hello javascript python

# 6. split方法：按照给定的字符串进行分割。返回的是一个列表。

# text = 'hello python python'
# text_arr = text.split(" ") 
# print(text_arr) # ['hello', 'python', 'python']
# print(type(text_arr)) # list类型
# for item in text_arr:
#     print(item)


'''
@description 2019/09/08 11:02
'''

# 7. startswith: 判断一个字符串是否以某个字符串开始

# text = 'hello python'
# print(text.startswith('h')) #True
# print(text.startswith('hello')) #True
# print(text.startswith('ell')) # False

# 8. endswith：判断一个字符串是否以某个字符串结尾

# text = 'hello python'
# print(text.endswith('n')) # True
# print(text.endswith('python')) # True
# print(text.endswith('hello')) # False

# 9.lower：将全部字符串转为小写
# 注意事项：不改变原字符串

# text = 'HELLO PYTHON'
# new_text = text.lower()
# print(text) # HELLO PYTHON
# print(new_text) # hello python

# 10.upper：将字符串全部改成大写
# 注意事项：不改变原字符串

# text = 'hello python'
# new_text = text.upper()
# print(text) # hello python
# print(new_text) # HELLO PYTHON

# 11. strip：将字符串左右的空格全部去掉
# 注意事项：不改变原字符串
# 类似于JavaScript： trim()

# text = '   python    '
# new_text = text.strip()
# print(text) #    python    
# print(new_text) # python


# 12.lstrip：删除字符串左边的空格
# 注意事项：不改变原字符串

# text = '   python    '
# new_text = text.lstrip()
# print(text) #    python    
# print(new_text) # python    

# 13.rstrip：删除字符串右边的空格

# text = '   python    '
# new_text = text.rstrip()
# print(text) #    python    
# print(new_text) #    python

'''
@description 2019/09/08 12:05
'''

# 14.partition：从str(字符串)出现的第一个位置起
# 包含str字符串：把字符串string分成一个3元素的元祖(string_pre_str, str, string_post_str)
# 如果string中不包含str(字符串)则string_pre_str = string,固定返回3个元素的元祖
# 不包含str字符串：(string, '', '')
# 注意事项：不改变原字符串

# text = 'hello python, hello javascript'
# text_tuple = text.partition('python')
# print(text) # hello python, hello javascript
# print(text_tuple) # ('hello ', 'python', ', hello javascript')

# text_tuple = text.partition('c++')
# print(text) # hello python, hello javascript
# print(text_tuple) # ('hello python, hello javascript', '', '')
# print(type(text_tuple)) # tuple

# 15.isalnum：如果string至少一个字符或所有字符，都是字母或数字，则返回True，否则返回False
# 注意事项：检验字符串是否为：字母或数字构成

# text = '1' # True
# text = '123abcdefg' # True
# text = '////?1213' # False
# print(text.isalnum()) 

# 16.isalpha：如果string至少一个字符并且所有字符都是字母，则返回True，否则返回False
# 注意事项：校验字符串是否为：大写或小写字母构成

# text = 'a' # True
# text = 'Abc' # True
# text = 'Abc123' # False
# print(text.isalpha()) 

# 17.isdigit：如果string只包含数字，则返回True，否则返回False
# 注意事项：校验字符串是否为：大等于0的正整数

# text = '123.133' # False
# text = '123' # True
# text = '-123' # False
# text = '0' # True
# print(text.isdigit())

# 18.isspace：如果string中只包含空格，则返回True，否则返回False
# 注意事项：检查字符串是否全部由空格组成

# text = '   hello' # False
# text = '   ' # True
# text = '   hello   ' # False
# print(text.isspace()) 

# 19.format：格式化字符串

country = '中国'
province = '浙江'
city = '杭州'
# 当前居住地：中国,浙江,杭州
print('当前居住地：{},{},{}'.format(country, province, city))
print('当前居住地：{country},{province},{city}'.format(country = country, province = province, city = city))