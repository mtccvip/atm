'''
管理员功能接口
'''

from db import db_handler

def change_balance_interface(user_name,change_balance_money):
    user_dic=db_handler.select(user_name)
    if not user_dic:
        return False,f'{user_name}不存在'
    else:
        user_dic['balance']=change_balance_money
        return True,f'{user_name}账户余额修改成功'

def locked_interface(user_name):
    user_dic=db_handler.select(user_name)
    if not user_dic:
        return False,f'{user_name}不存在'
    else:
        user_dic['locaked']=True
        db_handler.save(user_dic)
        return True,f'{user_name}冻结成功'