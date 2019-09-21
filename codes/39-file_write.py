'''
@description 2019/09/21 17:26
'''

# writelines函数：
# 一次性写入多个数据到文件中，但不会换行。

fp = open('file_write.txt', 'w', encoding='utf-8')
words = ['hello\n', 'world!\n', '你好\n', '世界\n']
fp.writelines(words)
fp.close()