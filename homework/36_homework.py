'''
@description 2019/09/08 14:23
'''

# 第一大题
text = """I am xiaoxiao, I have over 8 years of experience in marketing. I am the team manager of marketing for HP since 2013"""
print(text)
# 1. 把以上字符串的所有空格删掉，并保存在另外一个新的字符串中。 
# replace替换空格
not_space_text = text.replace(" ", "")
print(not_space_text)

# 2. 判断以上单词的个数
# split切割空格转list，读取list长度
word_arr = text.split(" ")
word_count = len(word_arr)
print(word_count)

# 3. 把以上所有包含t(不区分大小写)的单词都找出来。
# 循环切割的list，循环项转小写后，判断find大等于能找到t字母的
for word in word_arr:
    lower_word = word.lower()
    if lower_word.find('t') >= 0:
        print(word, end=" ")

print("")
# 4.把以上所有的数字都查出来
# replace替换, . 为空，转为新数组，循环判断isdigit字符串为正整数
all_letter_text = text.replace(",", "").replace(".", "")
all_letter_list = all_letter_text.split(" ")
for letter in all_letter_list:
    if letter.isdigit():
        print(letter, end=" ")

print("")
print("="*30)

# 第二大题：

# 把以下变量用format函数写一个连接数据库的语句。
# 连接数据的格式如下：
# mysql+pymysql://用户名:密码@主机:端口号/数据库名字?charset=utf8

# 用户名
DB_USERNAME = 'root'
# 密码
DB_PASSWORD = 'root'
# 主机
DB_HOST = '127.0.0.1'
# 端口号
DB_PORT = 3306
# 数据库名字
DB_NAME = 'zhiliao'

db_client_url = 'mysql+pymysql://{db_username}:{db_psd}@{db_host}:{db_port}/{db_name}?charset=utf8'.format(db_username = DB_USERNAME, db_psd = DB_PASSWORD, db_host = DB_HOST, db_port = DB_PORT, db_name = DB_NAME)
print(db_client_url) # mysql+pymysql://root:root@127.0.0.1:3306/zhiliao?charset=utf8