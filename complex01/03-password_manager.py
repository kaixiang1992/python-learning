'''
@description 2019/09/25 22:41
'''
from hashlib import md5

# 密码本功能

# 密码本文件
password_filename = 'password_book.txt' 
# 密码
password = None

# TODO: 是否首次使用密码本
def is_first_use():
    try:
        with open(password_filename, 'r', encoding='utf-8') as fp:
            # 读取首行用户密码行
            login_psd = fp.readline()
            # 有首行密码则非首次使用
            if login_psd:
                return False
            else:
                return True
    # TODO: 读取文件错误处理
    except FileNotFoundError: 
        return True

# TODO: 初始化登录密码
def init_password():
    # 登录密码
    init_psd = None
    while True:
        # 一次密码输入
        password1 = input('请输入登录密码：')
        # 二次密码输入
        password2 = input('请再次输入登录密码：')
        # TODO: 两次输入不一致
        if password1 != password2:
            print('两次密码输入不一致!...')
        else:
            init_psd = password1
            break
    # 写入初始化密码到文件
    with open(password_filename, 'w', encoding='utf-8') as fp:
        hash_psd = md5(init_psd.encode('utf-8')).hexdigest()
        fp.write('%s\n'%(hash_psd))
    print('初始化密码设置成功')

# TODO: 校验登录
def login_check():
    # TODO: 校验密码
    def check_password(psd):
        # md5加密输入密码
        hash_psd = md5(psd.encode('utf-8')).hexdigest()
        init_psd = None
        # 读取密码本首行用户初始化密码
        with open(password_filename, 'r', encoding='utf-8') as fp:
            init_psd = fp.readline().replace('\n','')
        # 输入密码与密码本密码对比
        if hash_psd == init_psd:
            # 赋值全局password变量
            global password
            password = psd
            print('全局密码：%s'%(password))
            return True
        else:
            return False

    while True:
        psd = input('请输入登录密码：')
        # 至少有一个字符并且所有字符都是字母或数字则返回True
        if psd.isalnum():
            # 校验密码
            if check_password(psd):
                return True
        else:
            print('输入密码格式化有误！')

# TODO: 登录成功进入首页
def index_page():
    while True:
        print('1.增加密码.')
        print('2.查看当前所有密码.')
        print('3.退出系统.')
        option = input('请输入选项：')
        if option.isdigit() and option in ['1','2','3']:
            if option == '1': # 增加密码
                add_password()
            elif option == '2': # 查看当前所有密码
                list_password()
            else:
                print('退出系统成功!....')
                break
        else:
            print('暂无该选项，请重新输入!....')

# TODO: 增加密码
def add_password():
    pass

# TODO: 查看当前所有密码
def list_password():
    pass

def main():
    print('=======密码本=======')
    # 是否首次使用密码本
    if is_first_use():
        # 初始化登录密码
        init_password()
    # 校验登录
    if login_check():
        # 登录成功进入首页
        index_page()

if __name__ == '__main__':
    main()