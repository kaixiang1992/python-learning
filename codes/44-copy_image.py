'''
@description 2019/09/22 18:51
'''

# 根据用户输入图片地址，输出图片地址进行复制操作

source_path = input('请输入需要复制的图片地址：')
dest_path = input('请输入复制的目的地：')

with open(source_path, 'rb') as fp_r:
    with open(dest_path, 'wb') as fp_w:
        fp_w.write(fp_r.read())
    
print('恭喜!文件拷贝成功!')