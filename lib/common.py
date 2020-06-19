'''
存放公共信息
'''
from conf import settings
import logging.config


import hashlib
def get_pwd_md5(password):
        md5_obj=hashlib.md5()
        md5_obj.update(password.encode('utf8'))
        salt='fklfkevjdkklwdkjjlvfrjvnvfn,znz,fn'
        md5_obj.update(salt.encode('utf8'))
        return md5_obj.hexdigest()

def login_auth(func):
    from core import src
    def inner(*args,**kwargs):
        if src.login_user:
            res=func(*args,**kwargs)
            return res
        else:
            print('用户未登录')
            src.login()
    return inner


def get_logger(log_type):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger=logging.getLogger(log_type)
    return logger


