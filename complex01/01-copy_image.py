'''
@description 2019/09/23 23:42
'''

# 复制图片功能

# D:\github\python-learning\complex01\3898077.jpg
source_path = input('请输入图片地址：')
# D:\github\python-learning\complex01\3898077.copy.jpg
print_path = input('请输入复制地址：')

with open(source_path, 'rb+') as fp_r:
    with open(print_path, 'wb+') as fp_w:
        fp_w.write(fp_r.read())