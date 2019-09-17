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

fp = open('file_wirte.txt', 'w', encoding='utf-8')
fp.write('我爱你中国，亲爱的母亲！')
fp.close()