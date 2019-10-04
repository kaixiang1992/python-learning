'''
@description 【Python模块和包】模块和包介绍 2019/10/04 20:26
'''

#TODO:导入my_file
# TODO: 绝对路径
# from tools import my_file
# my_file.save_data('1234...')
# TODO: 相对路径
# from . import my_file
# my_file.save_data('1234...')
# from .my_file import save_data
# save_data('1234...')

#TODO:导入b.py
from .subtools import b

def get_request(url):
    print('get请求数据已经下载下来：%s...'%(url,))

def post_request(url):
    print('post请求数据已经下载下来：%s...'%(url,))