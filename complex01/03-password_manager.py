'''
@description 2019/09/25 22:41
'''
from hashlib import md5
from functools import reduce

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

# 将当前密码进行ascii码转换并进行求和
def ord_password():
    # TODO: 将密码中所有的字符全部转换为ascii码对应的值，并且求他们的和
    # 没有密码返回None
    if not password:
        return None
    # 1.将password密码每一项转为ascill码
    # ord_map = map(lambda x:ord(x),password)
    # print(list(ord_map)) # [49, 50, 51, 52, 53, 54, 55, 56]
    # 2.将ascill码进行reduce求和
    # ord_reduce = reduce(lambda x,y:int(x)+int(y), ord_map)
    # print(ord_reduce) # 420
    return reduce(lambda x,y:int(x)+int(y), map(lambda x:ord(x), password))
    

# TODO: 增加密码
def add_password():
    product = input('请输入产品名称：')
    username = input('请输入用户名：')
    password = input('请输入密码：')
    # 密码转ascii码求和值
    ord_psd = ord_password()
    
    # 将产品名称每个字符转ascill码后+ord_pasd后返回的map，转化为字符串使用_拼接
    product_hashed = '_'.join(map(lambda x:str(ord(x)+ord_psd), product)) # 518_517_525_520_537
    username_hashed = '_'.join(map(lambda x:str(ord(x)+ord_psd), username))
    password_hashed = '_'.join(map(lambda x:str(ord(x)+ord_psd), password))

    # 将输入的密码信息追加到文件中
    with open(password_filename, 'a', encoding='utf-8') as fp:
        fp.write('%s:%s:%s\n'%(product_hashed, username_hashed, password_hashed))
    
    print('恭喜，密码存储成功!')

# TODO: 查看当前所有密码
def list_password():
    with open(password_filename, 'r', encoding='utf-8') as fp:
        for index,line in enumerate(fp):
            # TODO: 初始密码项调过
            if index == 0:
                continue
            # 结构产品名，用户名，密码ascill码项
            product_hashed,username_hashed,password_hashed = line.split(':')
            
            product_hashed_list = product_hashed.split('_')
            # TODO: 将ascill码每项-ord_pasd得到未相加前ascill码，再将未相加前ascill码，转化为输入前字符串后
            # 返回map集合，再用join将列表转为字符串，使用''空，则返回加密前ascill码
            del_product = ''.join(map(lambda x:chr(int(x) - ord_password()), product_hashed_list))

            username_hashed_list = username_hashed.split('_')
            del_username = ''.join(map(lambda x:chr(int(x) - ord_password()), username_hashed_list))

            password_hashed_list = password_hashed.split('_')
            del_password = ''.join(map(lambda x:chr(int(x) - ord_password()), password_hashed_list))

            print('产品名：%s，账号名：%s，密码：%s'%(del_product, del_username, del_password))

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