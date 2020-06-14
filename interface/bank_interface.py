'''
银行相关业务接口
'''
from db import db_handler

def withdraw_interface(user_name,money):
    user_dic=db_handler.select(user_name)
    balance=int(user_dic['balance'])
    money2=money*1.05
    print(money2,balance)
    if balance>=money2:
        balance-=money2
        user_dic['balance']=balance
        flow=f'{user_name}成功提现{money},手续费{money2-money}'
        user_dic['flow'].append(flow)

        db_handler.save(user_dic)
        return True,flow
    else:
        return False,'余额不足'

def repay_interface(user_name,repay_money):
    user_dic=db_handler.select(user_name)
    user_dic['balance']+=repay_money
    flow=f'{user_name}成功还款{repay_money}'
    user_dic['flow'].append(flow)
    db_handler.save(user_dic)
    return True,flow

def transfer_interface(user_name,transfer_account,transfer_money):
    user_dic=db_handler.select(user_name)

    transfer_account_dic=db_handler.select(transfer_account)
    if not transfer_account_dic:
        return False,'转账用户不存在'
    if user_dic['balance']>=transfer_money:
        user_dic['balance']-=transfer_money
        transfer_account_dic['balance']+=transfer_money
        flow=f'{user_name}向{transfer_account}成功转账{transfer_money}'
        user_dic['flow'].append(flow)
        transfer_account_flow=f'{transfer_account}接收了{user_name}转账{transfer_money}'
        transfer_account_dic['flow'].append(transfer_account_flow)
        db_handler.save(user_dic)
        db_handler.save(transfer_account_dic)
        return True,f'{user_name}向{transfer_account}成功转账{transfer_money}'
    else:
        return False,'账户余额不足'



def check_flow_interface(user_name):
    user_dic=db_handler.select(user_name)
    return user_dic['flow']


def pay_interface(user_name,cost):
    user_dic=db_handler.select(user_name)
    if user_dic.get('balance') >= cost:
        user_dic['balance']-=cost
        flow=f'{user_name}消费了{cost}'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        return True
    else:
        return False
