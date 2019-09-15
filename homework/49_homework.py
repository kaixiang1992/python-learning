'''
@description 2019/09/15 12:52
'''

# 1.给以下列表做逆序操作：a=[1,2,3,4,5,6,7,8,9]

a = list(range(1, 10)) 
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# reverse反向操作：
# a.reverse()
# print(a) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 切片操作
new_a = a[::-1]
print(new_a) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 2. 实现一个学生管理系统。
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

while True:
    print('='*20)
    print('1.新增学生.')
    print('2.查询所有学生.')
    print('3.根据学号查找学生.')
    print('4.根据学号删除学生.')
    print('5.退出系统.')
    print('='*20)
    opt = input('请输入操作码：')
    # 输入string只包含数字且在可操作系统项中
    if opt.isdigit() and opt in ['1','2','3','4','5']:
        if opt == '1': # 新增学生
            username = input('请输入学生姓名：')
            userage = input('请输入学生年龄：')
            classname = input('请输入学生所属班级：')
            student = dict(id=len(students)+1 , username=username, userage=userage, classname=classname)
            students.append(student)
            print('新增学生成功！')
        elif opt == '2': # 查询所有学生
            if len(students) > 0:
                for item in students:
                    print(item)
            else:
                print('当前系统无任何数据!')
        elif opt == '3': # 根据学号查找学生
            id = input('请输入学生学号：')
            if id.isdigit():
                if len(students) > 0:
                    for item in students:
                        if item.get('id') == int(id):
                            print('学号：{id},姓名：{username},年龄：{userage},班级：{classname}'.format(id=item.get('id'), username=item.get('username'), userage=item.get('userage'), classname=item.get('classname')))
                            break
                else:
                    print('当前系统无任何数据!')
            else:
                print('学号为数字类型！')
        elif opt == '4': # 根据学号删除学生
            id = input('请输入学生学号：')
            if id.isdigit():
                if len(students) > 0:
                    # 5.6. 循环的技巧
                    # https://docs.python.org/zh-cn/3/tutorial/datastructures.html#the-del-statement
                    for index,item in enumerate(students):
                        if item.get('id') == int(id):
                            del students[index]
                else:
                    print('当前系统无任何数据!')
            else:
                print('学号为数字类型！')
        else:
            print('退出系统成功！')
            break
    else:
        print('序号输入不正确！')
        continue