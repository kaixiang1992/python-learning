'''
@description 2019/09/21 23:04
'''

# tell函数：在读写的过程中，如果想知道当前文件指针所在的位置，可以通过tell()函数来获取。

# fp = open('test.txt', 'r', encoding='utf-8')
# position = fp.tell()
# print(position)
# text = fp.read(5)
# print(text)
# position = fp.tell()
# print(position)
# fp.close()

'''
@description 2019/09/21 23:20
'''

# seek()函数：定位到某个位置，如果读写的过程中，需要从另一个位置进行操作，可以使用seek()函数。
# seek(offset, from)有2个参数：
# offset: 偏移量。
# 当from为1和2时，offset必须为0. 异常如下：不能执行非零的末端相对查找
# UnsupportedOperation: can't do nonzero end-relative seeks
# from: 相对位置。0：从文件开头。1：当前位置。2：从文件末尾。

fp = open('test.txt', 'r', encoding='utf-8')
position = fp.tell()
print('当前指针位置：%d'%position) # 0 

# demo1：把相对位置设置为从文件开头，并且向后偏移5个字节。
# fp.seek(5, 0) #  world 5

# demo2：把位置设置为：离文件末尾，3个字节处
# fp.seek(0, 2) can't do nonzero end-relative seeks
# 1.先把文件指针移动到文件末尾
end = fp.seek(0, 2)
# 2.再偏移至末尾-3处
end -= 3
fp.seek(end, 0)  # 8 rld
position = fp.tell()
print('seek偏移当前指针位置：%d'%position)
text = fp.read()
print('当前读取文本内容：%s'%text)
fp.close()