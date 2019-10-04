'''
@description 【Python模块和包】模块查找路径 2019/10/04 21:08
'''

#TODO: 导入my_file
#TODO: 绝对路径
# from tools import my_file
# my_file.save_data('1234...')

#TODO: 相对路径
# from .. import my_file
# my_file.save_data('5678...')

from ..my_file import save_data
save_data('891011...')