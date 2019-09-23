'''
@description 2019/09/22 22:40
'''

# 实现一个宠物寄养管理系统
# 1. 需要使用函数来模块化。
# 2. 宠物的信息包括：宠物编号/宠物名称/宠物种类/一天的价格。
# 3. 需要实现：添加/查找/删除/退出程序的功能。
# 4. 要求使用文件来存储信息，下次打开系统，数据依然存在。
# PETS.append({'id':ID,'name':name,'category':category,'price':price})

pets = []
filename = 'pets.txt'

try:
    with open(filename, 'r', encoding='utf-8') as fp:
        for line in fp:
            pet = line.split('/')
            ID = pet[0]
            name = pet[1]
            category = pet[2]
            price = pet[3].strip()
            pets.append({'id': ID, 'name': name, 'category': category, 'price': price})
except FileNotFoundError:
    fp = open(filename, 'w', encoding='utf-8')
    fp.close()


# 添加宠物
def add_pet():
    ID = input('请输入宠物ID：')
    name = input('请输入宠物名字：')
    category = input('请输入宠物分类：')
    price = input('请输入宠物寄养价格：')
    pet = {'id': ID, 'name': name, 'category': category, 'price': price}
    pets.append(pet)
    print('恭喜宠物添加成功!')

# 查找宠物
def search_pet():
    name = input('请输入宠物名字：')
    for pet in pets:
        if pet.get('name') == name:
            text = '编号：{}，名字：{}，分类：{}，价格：{}'.format(
                pet.get('id'),
                pet.get('name'),
                pet.get('category'),
                pet.get('price')
            )
            print(text)
            break

# 删除宠物
def delete_pet():
    ID = input('请输入宠物ID：')
    for pet in pets:
        if pet.get('id') == ID:
            pets.remove(pet)
            print('恭喜，宠物删除成功')
            break

# 全部宠物
def list_pet():
    for pet in pets:
        text = '编号：{}，名字：{}，分类：{}，价格：{}'.format(
            pet.get('id'),
            pet.get('name'),
            pet.get('category'),
            pet.get('price')
        )
        print(text)

# 退出系统
def exit_system():
    if len(pets) > 0:
        pets_arr = []
        for pet in pets:
            text = '{id}/{name}/{category}/{price}\n'.format(
                id=pet.get('id'),
                name=pet.get('name'),
                category=pet.get('category'),
                price=pet.get('price')
            )
            pets_arr.append(text)
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.writelines(pets_arr)
    else:
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write("")

# 启动程序
def main():
    while True:
        print('='*30)
        print('1.添加宠物.')
        print('2.查找宠物.')
        print('3.删除宠物.')
        print('4.列出宠物.')
        print('5.退出程序.')
        print('='*30)
        option = input('请输入选项：')
        if option.isdigit() and option in ['1','2','3','4','5']:
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