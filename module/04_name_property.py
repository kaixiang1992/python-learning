'''
@description 【Python模块和包】__name__魔术变量 2019/10/05 11:45
'''

# 如果一个python文件或者模块作为被导入来运行的，那么就不是作为主运行文件来执行的

from tools import my_file

print('main: '+ __name__)

# 如果直接通过python a.py，那么a.py就是作为主运行文件来执行的

def main():
    print('hello world!...')

if __name__ == '__main__':
    main()

#TODO: 注意事项：
# 1. 如果在主运行文件中：__name__是等于__main__
# TODO: main: __main__

# 2. 如果在模块中：__name__是等于`模块名`。如果还处于某个包下面等于`包名.模块名`
# TODO: my_file: tools.my_file

# 3.如果在包的__init__文件中，那么等于包的名字。
# TODO: tools __init.py__: tools