# -*- coding: utf-8 -*-

# 脚本作者: 林德浩


import unittest
import requests
from common import log_common_class

"""
 封装requests底层请求方法，作为公共请求类
"""


class BaseCommon(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
    #     body = {
    #         "phone": config.message['user']['phone'],
    #         "code": config.message['user']['code']
    #     }
    #     print(f"请求参数: {body}")
    #     res = cls.request(method='get', url=url, params=body)
    #     cls.token = res.json()['data']['token']
    #     print(f'token == {cls.token}')
    #     return cls.token
    #     # print(cls.token)

    @classmethod
    def request(self, method: str, url, params=None, data=None, json=None, **kwargs):  # 自定义发送请求

        """自定义发送请求
        请求方法为字符串格式，params、data、json数据可以为空
        method：请求方法
        url：请求URL
        params：get请求的参数
        data：body中的数据
        json：body中json格式的数据
        kwargs：其它字典参数，允许传入不定长的参数
        """
        method = method.upper()  # 将请求方法转换成大写
        if method == "GET":  # 当请求方法为GET时，调用requests库中的get请求
            res = requests.get(url, params=params, **kwargs)
            # 输出以下日志信息，可以添加更多信息，比如请求头，响应状态等
            if json:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")
            elif params:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{params}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{params}，响应结果：{res.text}")
            elif not params and not json:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{res.url.split('?')[-1]}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{res.url.split('?')[-1]}，响应结果：{res.text}")

            return res  # 返回请求
        elif method == "POST":  # 当请求方法为POST时，调用requests库中的POST请求
            res = requests.post(url, data=data, json=json, **kwargs)
            if data:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{data}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{data}，响应结果：{res.text}")
            elif json:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")

            return res
        elif method == "PUT":  # 当请求方法为PUT时，调用requests库中的PUT请求
            res = requests.put(url, data=data, json=json, **kwargs)
            if data:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{data}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{data}，响应结果：{res.text}")

            elif json:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")

            return res
        elif method == "DELETE":  # 当请求方法为DELETE时，调用requests库中的DELETE请求
            res = requests.delete(url, data=data, json=json, **kwargs)
            if data:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{data}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{data}，响应结果：{res.text}")

            elif json:
                # logger.info(f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")
                log_common_class.Logger.set_input(
                    f"请求方法：{method}，请求地址：{url}，请求参数：{json}，响应结果：{res.text}")
            return res
        else:  # 如果不是以上4种请求方法，则提示"请求方法未定义，请检查！"
            print("请求方法未定义，请检查！")
