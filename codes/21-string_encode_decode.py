'''
@description 2019/09/08 13:58
'''

# 字符串编码和解码
# 在Python3中，默认写的字符串都是unicode类型，unicode是一个万能的字符集，可以存储任意的字符，
# 但是unicode字符串只能在内存中存在，不能在磁盘和网络间传输数据，如果要在文件或者网络间传输数据，
# 必须要将unicode转换为bytes类型的字符串，因此我们在写代码的时候有时候要对unicode和bytes类型字符串进行转换

# 1.encode('utf-8')：将unicode编码成bytes类型，并且编码方式采用的是utf-8
# unicode => bytes
text = 'hello world'
text_encode = text.encode('utf-8')
print(text) # hello world
print(type(text)) # str
print(text_encode) # b'hello world'
print(type(text_encode)) # bytes
print('='*30)

# 2.decode('utf-8')：将bytes解码成unicode类型，并且解码方式采用utf-8
# bytes => unicode

bytes_text = b'hello world'
str_text = bytes_text.decode('utf-8')
print(bytes_text) # b'hello world'
print(type(bytes_text)) # bytes
print(str_text) # hello world
print(type(str_text)) # str
print('='*30)

# md5加密密码，bytes数据类型的使用

from hashlib import md5
psd = 'admin123'

# TypeError：Unicode-objects must be encoded before hashing
# 必须先encode编码为bytes类型
# md5_psd = md5(psd).hexdigest()

md5_psd = md5(psd.encode('utf-8')).hexdigest()
print(md5_psd) # 0192023a7bbd73250516f069df18b500
print('='*30)

# unicode使用案例：写入hello world到txt文件

with open('abc.txt', 'w') as fp:
    # TypeError: write() argument must be str, not bytes
    # 写入数据是str类型，不能为bytes类型
    # fp.write('hello world'.encode('utf-8'))

    fp.write('hello world')
