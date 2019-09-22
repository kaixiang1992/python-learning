'''
@description 2019/09/22 12:10
'''

# 1.打开文件
# 2.对文件进行相应的操作
# 3.关闭文件

# fp = open('test.txt', 'w', encoding='utf-8')
# fp.write('hello world!')
# fp.close()

with open('test.txt', 'w', encoding='utf-8') as fp:
    fp.write('hello world!')

print('end......')