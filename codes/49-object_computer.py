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
    电脑类: cpu接口，内存数量，硬盘数量
    '''
    def __init__(self, cpu_interface, ram_count, disk_count):
        self.cpu_interface = cpu_interface
        self.ram_count = ram_count
        self.disk_count = disk_count
        # 以下三个是私有属性，因为配件装进去了，用户就不需要关心了
        self.__cpu = None
        self.__rams = []
        self.__disks = []

    '''
    添加cpu
    '''
    def add_cpu(self, cpu):
        if cpu.interface == self.cpu_interface:
            self.__cpu = cpu
        else:
            print('cpu型号不对，不能安装!...')
    
    '''
    添加内存
    '''
    def add_ram(self, ram):
        if len(self.__rams) == self.ram_count:
            print('内存条已经没有位置安装了!....')
        else:
            self.__rams.append(ram)

    '''
    添加硬盘
    '''
    def add_disk(self, disk):
        if len(self.__disks) == self.disk_count:
            print('硬盘已经没有位置安装了!...')
        else:
            self.__disks.append(disk)
    '''
    校验安装程序
    '''
    def run(self):
        # TODO: 没有安装CPU
        if not self.__cpu:
            print('没有cpu电脑不能正常运行!....')
        # TODO: 没有安装内存条或内存条数量超过初始数量
        elif len(self.__rams) == 0 or len(self.__rams) > self.ram_count:
            print('内存条安装失败，电脑不能正常运行!....')
        # TODO: 没有安装硬盘或硬盘数量超过初始数量
        elif len(self.__disks) == 0 or len(self.__disks) > self.disk_count:
            print('硬盘安装失败，电脑不能正常运行!....')
        else:
            print('所有配件均已安装完毕，电脑正常启动!....')

'''
主启动程序
'''
def main(): 
    # 初始化一台电脑
    computer = Computer('1101', 2, 4)

    # 初始化cpu
    cpu = Cpu('英特尔', 8, '1101')

    # 初始化内存
    ram1 = Ram('三星', '4G')
    ram2 = Ram('三星', '4G')
    # ram3 = Ram('三星', '4G')
    
    # 初始化硬盘
    disk1 = Disk('金士顿', '512G')
    disk2 = Disk('金士顿', '512G')
    disk3 = Disk('金士顿', '512G')
    disk4 = Disk('金士顿', '512G')

    # 组装cpn
    computer.add_cpu(cpu)

    # 组装内存
    computer.add_ram(ram1)
    computer.add_ram(ram2)
    # computer.add_ram(ram3)

    # 组装硬盘
    computer.add_disk(disk1)
    computer.add_disk(disk2)
    computer.add_disk(disk3)
    computer.add_disk(disk4)

    # 启动电脑
    computer.run()


if __name__ == '__main__':
    main()

