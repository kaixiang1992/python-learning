'''
@description 2019/9/29 23:19
'''

# CPU/RAM/DISK

class Cpu(object):
    '''
    CPU类：品牌、核、接口
    '''
    def __init__(self, brand, core, interface):
        self.brand = brand
        self.core = core
        self.interface = interface

class Ram(object):
    '''
    内存类：品牌、大小
    '''
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

class Disk(object):
    '''
    硬盘类：品牌、大小
    '''
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

class Computer(object):
    '''
    电脑类
    '''
    def __init__(self):
        pass