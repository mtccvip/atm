'''
用户视图
'''

from interface import user_interface
from lib import common
from interface import bank_interface
from interface import shop_interface

login_user=None

# 1.注册功能
def register():
    while True:
        user_name=input('请输入用户名:').strip()
        password=input('请输入密码:').strip()
        re_password=input('请确认密码:').strip()

        if password==re_password:
            flag,msg=user_interface.resister_interface(user_name,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
            # import json
            # import os
            # from conf import settings
            # user_path=os.path.join(settings.USER_DATA_PATH,f'{user_name}.json')
            # if not os.path.getsize(user_path):
            #     os.remove(user_path)
            # if os.path.exists(user_path):
            #     with open(user_path,mode='r',encoding='utf8') as f:
            #         user_dic=json.load(f)
            #     if user_dic:
            #         print('用户已经存在，请重新输入')
            #         continue
            # else:
            #     user_dic={
            #         'username': user_name,
            #         'password': password,
            #         'balance': 15000,
            #         'flow': [],
            #         'shop_cat': {},
            #         'locaked': False
            #     }
            #
            #
            #     user_path=os.path.join(settings.USER_DATA_PATH,f'{user_name}.json')
            #     with open(user_path,mode='w',encoding='utf-8') as f:
            #         json.dump(user_dic,f,ensure_ascii=False)
            #         f.flush()
        else:
            print('两次输入的密码不一致')

# 2.登录功能
def login():
    while True:
        user_name=input('请输入用户名:').strip()
        password=input('请输入密码:').strip()
        flag,msg=user_interface.login_interface(user_name,password)
        if flag:
            print(msg)
            global login_user
            login_user=user_name
            break

        else:
            print(msg)


# 3.查看余额
@common.login_auth
def check_balance():
    balance=user_interface.check_balance_interface(login_user)
    print(f'用户{login_user}账户余额为{balance}')

# 4.提现功能
@common.login_auth
def withdraw():
    while True:
        money=input('请输入体现金额:').strip()
        if not money.isdigit():
            print('请重新输入')
            continue
        else:
            money=int(money)
        flag,msg=bank_interface.withdraw_interface(login_user,money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5.还款功能
@common.login_auth
def repay():
    while True:
        repay_money=input('请输入还款金额:').strip()
        if not repay_money.isdigit():
            print('请输入正确的金额')
            continue
        repay_money=int(repay_money)
        if repay_money<=0:
            print('还款金额必须大于0')
            continue
        else:
            flag,msg=bank_interface.repay_interface(login_user,repay_money)
            if flag:
                print(msg)
                break

# 6.转账功能
@common.login_auth
def transfer():
    while True:
        transfer_account=input('请输入要转账的账户名:').strip()
        transfer_money=input('请输入转账金额:').strip()
        if not transfer_money.isdigit():
            print('请输入正确的转账金额')
            continue
        transfer_money=int(transfer_money)
        if transfer_money<=0:
            print('转账金额必须大于0')
        else:
            flag,msg=bank_interface.transfer_interface(login_user,transfer_account,transfer_money)
            if flag:
                print(msg)
                break
            else:
                print(msg)





# 7.查看流水
@common.login_auth
def check_flow():
    flow=bank_interface.check_flow_interface(login_user)
    if flow:
        for n in flow:
            print(n)
    else:
        print('当前用户没有流失')



# 8.购物功能
@common.login_auth
def shopping():
    shop_list=[
        ['电脑',5998],
        ['衣服',877],
        ['零食',556],
        ['机票',887],
    ]

    shopping_car={}

    while True:
        for index,shop in enumerate(shop_list):
            shop_name,price=shop
            print(f'商品名称:{shop_name}',
                  f'商品编号:{index}',
                  f'商品价格:{price}'
                  )
        chioce=input('请输入商品编号or结账y/n/q:').strip()
        if chioce == 'q':
            break
        if chioce =='y':
            if not shopping_car:
                print('购物车是空的，不能结算')
                continue
            flag,msg=shop_interface.shopping_interface(login_user,shopping_car)
            if flag:
                print(msg)
                continue
            else:
                print(msg)

        elif chioce=='n':
            if not shopping_car:
                print('购物车是空的,请重新输入')
                continue
            flag,msg=shop_interface.add_shop_car_interface(login_user,shopping_car)
            if flag:
                print(msg)
                continue
            else:
                print(msg)


        if not chioce.isdigit():
            print('请输入数字')
            continue

        chioce=int(chioce)
        if chioce not in range(len(shop_list)):
            print('请输入正确的编号')
            continue

        shop_name,shop_price=shop_list[chioce]

        if shop_name in shopping_car:
            shopping_car[shop_name][1]+=1
        else:
            shopping_car[shop_name]=[shop_price,1]
        print(shopping_car)



# 9.查看购物车
@common.login_auth
def check_shop_car():
    res=shop_interface.check_shop_car_interface(login_user)
    if res:
        print(res)
    else:
        print('购物车为空')


# 10.管理员功能
@common.login_auth
def admin():
    from core import admin
    admin.run()



# 创建函数功能字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin

}



def run():
    while True:
        print('''
        ==========welcome==========
            1.注册功能
            2.登录功能
            3.查看余额
            4.提现功能
            5.还款功能
            6.转账功能
            7.查看流水
            8.购物功能
            9.查看购物车
            10.管理员功能
            q.退出
        ==========welcome==========
        
        ''')
        chioce=input('input your choice:').strip()
        if chioce == 'q':
            break
        elif chioce not in func_dic:
            print('请输入正确的功能编号!')
            continue
        else:
            func_dic.get(chioce)()