'''
@description 2019/09/17 23:09
'''

# 文件操作三部曲：
# 1.以指定的方式，打开文件。
# 2.做相关的操作(读数据、写数据)。
# 3.关闭文件

# fp = open('xxx.txt', 'w')
# fp.write('abc')
# fp.close()

'''
@description 2019/09/17 23:38
'''

# read方法：
# 以只读的方式打开。文件的指针将会放在文件的开头。这是默认的模式。
# python3打开一个文件的时候，要指定文件的编码为utf-8 

# fp = open('xxx.txt', 'r', encoding='utf-8')
# string = fp.read()
# print(string) # 我爱你中国，亲爱的母亲！
# fp.close()

# write方法：

# python2和python3默认打开文件的编码。
# python2操作文件的时候，默认使用的是utf-8的编码。
# python3操作文件的时候，如果没有指定编码，默认将使用系统自带的编码
# python3打开一个文件的时候，要指定文件的编码为utf-8 

# fp = open('file_wirte.txt', 'w', encoding='utf-8')
# fp.write('我爱你中国，亲爱的母亲！')
# fp.close()

'''
@description 2019/09/21 13:00
'''

# r读方式打开文件，不能用于写入
# fp = open('file_wirte.txt', 'r', encoding='utf-8')
# text = fp.read()
# print(text) # 我爱你中国，亲爱的母亲！
# fp.write('我爱你中国，亲爱的母亲！') # not writable


# w写方式打开文件，不能用于读，并且会覆盖掉原来的数据
# fp = open('file_wirte.txt', 'w', encoding='utf-8')
# fp.write('hello world!')
# text = fp.read() # UnsupportedOperation:not readable

# a追加方式打开文件，不能用于读，不会覆盖原来的数据
# fp = open('file_wirte.txt', 'a', encoding='utf-8')
# fp.write('我爱你中国，亲爱的母亲!')
# fp.read() # UnsupportedOperation:not readable

# r+读写方式打开文件(r的基因)，在读的基础上，增加了写的功能
# fp = open('file_wirte.txt', 'r+', encoding='utf-8')
# text = fp.read()
# fp.write('1231213435356')
# print(text)

# w+读写方式打开文件(w的基因)
# w+：不管你是去读还是去写，只要以w+的方式打开文件
# 那么就会把原来文件删掉，重新创建一个新的文件,
# 所以如果去读，那么读到的永远是空字符串。
fp = open('file_wirte.txt', 'w+', encoding='utf-8')
fp.write('hello world!')
text = fp.read()
print('='*20)
print(text)
print('='*20)

fp.close()