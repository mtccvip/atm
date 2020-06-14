'''
购物功能接口
'''
from interface import bank_interface
from db import db_handler

def shopping_interface(user_name,shopping_car):
    cost=0
    for price_number in shopping_car.values():
        price,number=price_number
        cost+=(price*number)


    flag=bank_interface.pay_interface(user_name,cost)
    if flag:
        return True,'支付成功'
    return False,'余额不足'

def add_shop_car_interface(user_name,shopping_car):
    user_dic=db_handler.select(user_name)
    shop_car=user_dic.get('shop_car')

    for shop_name,price_number in shopping_car.items():
        number=price_number[1]

        if shop_name in shop_car:
            user_dic['shop_car'][shop_name][1]+=number

        else:
            user_dic['shop_car'].update({shop_name:price_number})
    db_handler.save(user_dic)
    return True,'添加购物车成功'


def check_shop_car_interface(user_name):
    user_dic=db_handler.select(user_name)
    return user_dic.get('shop_car')