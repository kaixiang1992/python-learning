'''
@description 【Python模块和包】模块和包介绍 2019/10/04 20:26
'''

#TODO: 1. import：导入某个模块。以后要使用模块中的函数或者方法或者变量，则需要通过`模块名.xxx`的形式调用

# import my_request

# my_request.get_request('https://www.baidu.com')

#TODO: 2. from xxx import xxx：从某个模块中导入对象或者方法等。

# from my_request import get_request

# get_request('https://www.baidu.com')

#TODO: 3. from xxx import *：从某个模块中一次性导入所有的对象或者方法等。不推荐使用
# from my_request import *

# get_request('https://www.baidu.com')
# post_request('https://www.baidu.com')

#TODO: 4. from a import b as c：从a中导入b并命名为c。以后在代码中引用b,通过c来引用。
# from my_request import get_request as get
# get('https://www.baidu.com')


'''
@description 包
'''

#TODO: 包：
# 包其实本质上是一个文件夹，将一些相关联的模块放在一起。但是如果一个文件夹要让python识别为一个包，
# 则必须在这个文件夹中创建一个叫做__init__.py的文件。一个文件夹中只有拥有了__init__.py这个文件，
# 才能被视为一个包

from tools import my_request
my_request.post_request('https://www.baidu.com')