'''
@description 【Python知识补充】宠物寄养系统_面向对象版 2019/10/05 19:24
'''

class Pet(object):
    '''
    宠物类
    '''
    def __init__(self, pet_id, pet_name, pet_type, pet_price):
        self.id = pet_id
        self.name = pet_name
        self.type = pet_type
        self.price = pet_price

    #TODO:格式化读取文件宠物数据
    @classmethod
    def pet_with_line(cls, line):
        pet_id, pet_name, pet_type, pet_price = line.replace('\n', '').split('-')
        pet = Pet(pet_id, pet_name, pet_type, pet_price)
        return pet

    #TODO:格式化写入文件数据
    def get_line(self):
        return '{id}-{name}-{type}-{price}\n'.format(id=self.id, name=self.name, type=self.type, price=self.price)


class PetManager(object):
    '''
    宠物管理
    '''
    __instance = None
    __filename = 'pet_book.txt'

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    #TODO: 新增宠物
    def add_pet(self, pet_id, pet_name, pet_type, pet_price):
        pet = Pet(pet_id, pet_name, pet_type, pet_price)

        #TODO: 追加方式添加宠物
        with open(PetManager.__filename, 'a', encoding='utf-8') as fp:
            fp.write(pet.get_line())

    #TODO: 全部宠物
    def list_all_pets(self):
        all_pets = []
        try:
            # TODO:以读方式打开文件
            with open(PetManager.__filename, 'r', encoding='utf-8') as fp:
                for line in fp:
                    all_pets.append(Pet.pet_with_line(line))
        except FileNotFoundError:
            pass
        return all_pets


class Application(object):
    '''
    程序运行流程控制
    '''
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    #TODO: 新增宠物
    def __input_pet_info(self):
        pet_id = input('请输入宠物编号：')
        pet_name = input('请输入宠物名字：')
        pet_type = input('请输入宠物类型：')
        pet_price = input('请输入寄养价格：')
        manager.add_pet(pet_id, pet_name, pet_type, pet_price)
        print('恭喜!宠物添加成功!...')

    #TODO: 显示所有宠物
    def __print_all_pets(self):
        all_pets = manager.list_all_pets()
        print('id\tname\ttype\tprice')
        for pet in all_pets:
            print('{id}\t{name}\t{type}\t{price}'.format(id=pet.id, name=pet.name, type=pet.type, price=pet.price))

    def run(self):
        while True:
            print("宠物寄养系统")
            print('0. 退出程序')
            print("1. 添加新宠物")
            print("2. 显示所有宠物")
            option = input('请输入操作序号：')
            if option.isdigit() and option in ['0', '1', '2']:
                if option == '1':
                    self.__input_pet_info()
                elif option == '2':
                    self.__print_all_pets()
                else:
                    break
            else:
                print('输入错误，请重新输入操作序号!...')


manager = PetManager()
app = Application()
def main():
    app.run()

if __name__ == '__main__':
    main()