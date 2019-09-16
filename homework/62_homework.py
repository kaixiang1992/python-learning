'''
@description 2019/09/16 23:22
'''

# 1.实现一个函数，用于求两个数之和。

def num_total(x, y, func):
    result = func(x,y)
    return result

print(num_total(1,2,lambda x,y:x+y)) # 3
print(num_total(10,20,lambda x,y:x+y)) # 30
print('='*20)

# 2.实现一个函数，可以求任意多个数之和
# reduce函数：reduce(函数，列表)

from functools import reduce

def anynum_total(*args):
    result = reduce(lambda x,y:x+y, args)
    return result

print(anynum_total(1,2,3,4,5,6)) # 21
print(anynum_total(11,12,13,14,15,16)) # 81
print('='*20)

# 3.用函数把第四天的学生管理系统模块化(每个功能用一个函数模块)
# 要求如下：
# 1.要求记录学生的学号，姓名，年龄，所属班级信息。
# 2.可以新增学生。
# 3.可以列出所有学生。
# 4.可以根据学号查找学生。
# 5.可以根据学号删除学生。
# 提示：用字典存储一个学生的信息，用列表存储所有学生的字典对象。

print('欢迎来到学生管理系统')

# 学生数组
students = []
# 功能列表
menu_list = ['1','2','3','4','5']

# 系统欢迎界面
def system_welcome():
    print('='*20)
    print('1.新增学生.')
    print('2.查询所有学生.')
    print('3.根据学号查找学生.')
    print('4.根据学号删除学生.')
    print('5.退出系统.')
    print('='*20)

# 新增学生
def add_student():
    username = input('请输入学生姓名：')
    userage = input('请输入学生年龄：')
    classname = input('请输入学生所属班级：')
    student = {'id': len(students)+1, 'username': username, 'userage': userage, 'classname': classname}
    students.append(student)
    print('学生添加成功!')

# 查询所有学生
def all_student():
    if len(students):
        for item in students:
            print(item)
    else:
        print('当前系统无任何数据!')

# 根据学号查找学生
def search_student():
    id = input('请输入学生学号：')
    if id.isdigit():
        if len(students):
            for item in students:
                if item.get('id') == int(id):
                    print(item)
                    break
        else:
            print('当前系统无任何数据!')
    else:
        print('学号为数字类型！')

# 根据序号删除学生
def delete_student():
    id = input('请输入学生学号：')
    if id.isdigit():
        if len(students):
            for index,item in enumerate(students):
                if item.get('id') == int(id):
                    del students[index]
                    break
        else:
            print('当前系统无任何数据!')
    else:
        print('学号为数字类型！')

# 初始化函数
def main():
    while True:
        system_welcome()
        opt = input('请输入系统操作码：')
        if opt.isdigit() and opt in menu_list:
            if opt == '1': # 新增学生
                add_student()
            elif opt == '2': # 查询所有学生
                all_student()
            elif opt == '3': # 根据学号查找学生
                search_student()
            elif opt == '4': # 根据学号删除学生
                delete_student()
            else: # 退出系统
                print('退出系统成功!')
                break
        else:
            print('序号输入不正确！')
            continue

if __name__ == '__main__':
    main()