# -*- coding: utf-8 -*-


import config
from common.base_requests import BaseCommon
import random

"""
    封装获取token的方法，return token 作为其他接口的请求头参数
"""

def getToken():
    url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
    body = {
        "phone": config.message['正确且有权限登录后台的手机号码']['phone'],
        "code": config.message['正确且有权限登录后台的手机号码']['code']
    }
    # body = {
    #     "phone": config.message['user']['phone'],
    #     "code": random.randint(1000, 9999)
    # }
    # print(f"请求参数: {body}")
    res = BaseCommon.request(method='get', url=url,timeout=5, params=body)
    token = res.json()['data']['token']
    # print(f'token = {token}')
    return token

getToken()
