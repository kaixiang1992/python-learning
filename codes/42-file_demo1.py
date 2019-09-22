'''
@description 2019/09/22 12:27
'''

# 1.拷贝文件。

# 实现方案一：利用list列表缓存a.txt读取文件内容
# a => [] => a.copy.txt

# text = []
# with open('a.txt', 'r', encoding='utf-8') as fp:
#     text = fp.readlines()

# with open('a.copy.txt', 'w', encoding='utf-8') as fp:
#     fp.writelines(text)

# 实现方案二：直接复制到b文件
# a => b

with open('a.txt', 'r', encoding='utf-8') as fp1:
    with open('a.copy.txt', 'w', encoding='utf-8') as fp2:
        # texts = fp1.readlines()
        # fp2.writelines(texts)

        # 读取大文件操作
        for line in fp1:
            fp2.write(line)