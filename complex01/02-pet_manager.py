'''
@description 2019/09/24 23:00
'''

# 宠物寄养管理系统
# 1. 需要使用函数来模块化。
# 2. 宠物的信息包括：宠物编号/宠物名称/宠物种类/一天的价格。
# 3. 需要实现：添加/查找/删除/退出程序的功能。
# 4. 要求使用文件来存储信息，下次打开系统，数据依然存在。

# 宠物列表
pets = []
# 功能列表
support = ['1', '2', '3', '4', '5']

try:
    with open('pet_manager.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            pet_id = line.split('-')[0]
            pet_name = line.split('-')[1]
            pet_category = line.split('-')[2]
            pet_price = line.split('-')[3].strip()
            pets.append({'id': pet_id, 'name': pet_name, 'category': pet_category, 'price': pet_price})
except FileNotFoundError:
    fp = open('pet_manager.txt', 'w', encoding='utf-8')
    fp.close()

# 添加宠物
def add_pet():
    pet_id = input('请输入宠物ID：')
    pet_name = input('请输入宠物名称：')
    pet_category = input('请输入宠物种类：')
    pet_price = input('请输入宠物价格：')
    pet = {'id': pet_id, 'name': pet_name, 'category': pet_category, 'price': pet_price}
    pets.append(pet)
    print('宠物添加成功!....')

# 查找宠物
def search_pet():
    if len(pets) > 0:
        pet_name = input('请输入宠物名称：')
        for pet in pets:
            if pet.get('name') == pet_name:
                text = '编号：{id}，名称：{name}，种类：{category}，价格：{price}'.format(
                    id=pet.get('id'),
                    name=pet.get('name'),
                    category=pet.get('category'),
                    price=pet.get('price')
                )
                print(text)
                break
    else:
        print('系统暂无数据!....')

# 删除宠物
def delete_pet():
    if len(pets) > 0:
        pet_name = input('请输入宠物名称：')
        for pet in pets:
            if pet.get('name') == pet_name:
                pets.remove(pet)
                break
    else:
        print('系统暂无数据!....')

# 所有宠物
def list_pet():
    if len(pets) > 0:
        for pet in pets:
            text = '编号：{id}，名称：{name}，种类：{category}，价格：{price}'.format(
                id=pet.get('id'),
                name=pet.get('name'),
                category=pet.get('category'),
                price=pet.get('price')
            )
            print(text)
    else:
        print('系统暂无数据!....')

# 退出程序
def exit_system():
    if len(pets) > 0:
        write_lines = []
        for pet in pets:
            text = '{id}-{name}-{category}-{price}\n'.format(
                id=pet.get('id'),
                name=pet.get('name'),
                category=pet.get('category'),
                price=pet.get('price')
            )
            write_lines.append(text)
        with open('pet_manager.txt', 'w', encoding='utf-8') as fp:
            fp.writelines(write_lines)
    else:
        with open('pet_manager.txt', 'w', encoding='utf-8') as fp:
            fp.write("")

# 主程序运行
def main():
    while True:
        print('宠物管理系统')
        print('1.添加宠物.')
        print('2.查找宠物.')
        print('3.删除宠物.')
        print('4.所有宠物.')
        print('5.退出系统.')
        print('='*30)
        option = input('请输入系统操作码：')
        if option.isdigit() and option in support:
            if option == '1':
                add_pet()
            elif option == '2':
                search_pet()
            elif option == '3':
                delete_pet()
            elif option == '4':
                list_pet()
            else:
                exit_system()
                break
        else:
            continue

if __name__ == '__main__':
    main()