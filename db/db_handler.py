'''
处理数据接口
'''


import json
import os
from conf import settings

def select(user_name):
    user_path = os.path.join(settings.USER_DATA_PATH, f'{user_name}.json')
    if os.path.exists(user_path) and os.path.getsize(user_path):
        with open(user_path,mode='r',encoding='utf8') as f:
            user_dic=json.load(f)
            return user_dic

def save(user_dic):
    user_name=user_dic['username']
    user_path=os.path.join(settings.USER_DATA_PATH,f'{user_name}.json')
    with open(user_path,mode='wt',encoding='utf8') as f:
        json.dump(user_dic,f,ensure_ascii=False)

