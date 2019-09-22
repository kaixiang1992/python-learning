'''
@description 2019/09/22 19:07
'''

# 用函数把第四天的学生管理系统模块化(每个功能用一个函数模块)
# 要求如下：
# 1.要求记录学生的学号，姓名，年龄，所属班级信息。
# 2.可以新增学生。
# 3.可以列出所有学生。
# 4.可以根据学号查找学生。
# 5.可以根据学号删除学生。
# 6.要求使用文件来存储信息，下次打开系统，数据依然存在。
# 提示：用字典存储一个学生的信息，用列表存储所有学生的字典对象。

# 功能列表
menu_list = ['1', '2', '3', '4', '5']
# 学生列表
students = []


# 新增学生
def add_student():
    username = input('请输入学生姓名：')
    userage = input('请输入学生年龄：')
    classname = input('请输入所属班级：')
    student = {'id': len(students) + 1, 'username': username, 'userage': userage, 'classname': classname}
    students.append(student)
    save_student()

# 查询所有学生
def all_student():
    if len(students) > 0:
        for student in students:
            print(student)
    else:
        print('系统暂无数据！')

# 根据学号查找学生：
def search_student():
    if len(students) > 0:
        id = input('请输入学生学号：')
        if id.isdigit():
            for student in students:
                if student.get('id') == int(id):
                    print(student)
                    break
    else:
        print('系统暂无数据！')

# 根据序号删除学生：
def delete_student():
    if len(students) > 0:
        id = input('请输入学生学号：')
        if id.isdigit():
            for index,student in enumerate(students):
                if student.get('id') == int(id):
                    del students[index]
                    save_student()
    else:
        print('系统暂无数据！')

# 系统引导
def greet_system():
    print('='*20)
    print('1.新增学生.')
    print('2.查询所有学生.')
    print('3.根据学号查找学生.')
    print('4.根据学号删除学生.')
    print('5.退出系统.')
    print('='*20)

# 读取系统txt学生数据
def read_studentdata():
    # FileNotFoundError
    try:
        with open('students.txt', 'r', encoding='utf-8') as fp:
            for student in fp:
                if student:
                    studentinfo = student.split('-')
                    classname = studentinfo[3].strip()
                    student = {'id': studentinfo[0], 'username': studentinfo[1], 'userage': studentinfo[2], 'classname': classname }
                    students.append(student)
    except FileNotFoundError:
        print('暂无缓存文件....')

# 保存学生数据至文件
def save_student():
    if len(students) > 0:
        fp = open('students.txt', 'w', encoding='utf-8')
        for student in students:
            id = student.get('id')
            username = student.get('username')
            userage = student.get('userage')
            classname = student.get('classname')
            fp.write('%s-%s-%s-%s\n'%(id, username, userage, classname))
            

print('欢迎来到学生管理系统：')

def main():
    while True:
        greet_system()
        read_studentdata()
        opt = input('请输入系统操作编码：')
        if opt.isdigit() and opt in menu_list:
            if opt == '1':
                add_student()
            elif opt == '2':
                all_student()
            elif opt == '3':
                search_student()
            elif opt == '4':
                delete_student()
            else:
                print('退出系统成功！')
                break
        else:
            continue

if __name__ == '__main__':
    main()