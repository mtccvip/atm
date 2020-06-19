'''
逻辑接口
'''
import os
from db import db_handler
from lib import common


shop_logger=common.get_logger('shop')

def resister_interface(user_name,password,balance=15000):
    user_dic=db_handler.select(user_name)
    if user_dic:
        return False,'用户名已存在'
    password=common.get_pwd_md5(password)
    user_dic = {
        'username': user_name,
        'password': password,
        'balance': balance,
        'flow': [],
        'shop_car': {},
        'locaked': False
    }
    db_handler.save(user_dic)
    shop_logger.info(f'{user_name}注册成功')
    return True,f'{user_name}注册成功'

def login_interface(user_name,password):
    user_dic=db_handler.select(user_name)
    if user_dic['locaked']:
        shop_logger.info(f'{user_name}已经被锁定')
        return False,'当前用户已被锁定'
    password=common.get_pwd_md5(password)
    if user_dic:
        if password == user_dic['password']:
            return True,f'{user_name}登录成功'
        else:
            return False,'用户名或者密码错误'
    else:
        return False,'用户不存在'

def check_balance_interface(user_name):
    user_dic=db_handler.select(user_name)
    balance=user_dic['balance']
    return balance



