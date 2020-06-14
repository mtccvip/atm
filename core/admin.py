'''
管理员功能视图
'''
from core import src
from interface import admin_interface

def add_user():
    src.register()

def change_balance():
    while True:
        change_balance_account=input('请输入要修改账户余额的用户名:').strip()
        change_balance_money=input('请输入修改金额').strip()
        if not change_balance_money.isdigit():
            print('金额必须为数字')
            continue
        change_balance_money=int(change_balance_money)
        if change_balance_money<0:
            print('金额必须大于等于0')
            continue
        flag,msg=admin_interface.change_balance_interface(change_balance_account,change_balance_money)

        if flag:
            print(msg)
            break
        else:
            print(msg)

def locked_user():
    while True:
        locked_user=input('请输入要锁定的账户名:').strip()
        flag,msg=admin_interface.locked_interface(locked_user)
        if flag:
            print(msg)
            break
        else:
            print(msg)



fun_dic={
            '1':add_user,
            '2':change_balance,
            '3':locked_user
        }

def run():
    while True:
        print('''
              1.添加用户
              2.修改余额
              3.锁定用户
              'q'.退出
        
        ''')
        chioce=input('请输入你的选择:').strip()
        if chioce=='q':
            break
        if chioce in fun_dic:
            fun_dic[chioce]()
        else:
            print('请输入正确的编号')
            continue

