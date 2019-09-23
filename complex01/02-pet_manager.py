'''
@description 2019/09/23 23:52
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

# 添加宠物
def add_pet():
    pass

# 查找宠物
def search_pet():
    pass

# 删除宠物
def delete_pet():
    pass

# 所有宠物
def list_pet():
    pass

# 退出程序
def exit_system():
    pass

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
        else:
            continue

if __name__ == '__main__':
    main()