# -*- coding: utf-8 -*-

# 用例  ID:
# 用例标题: 登录接口手机号边界值，以及等价类校验
# 预置条件: 可用白名单和不可用的手机号，正确的验证码
# 测试步骤:
#   1.调用接口：sigin
#   2.传入账号，验证码，请求url，header发起get请求
# 预期结果:
#   1.登录成功，
#   2.检查响应码为：200，{"code":0,"message":"success"}
# 脚本作者: 林德浩
# 写作日期: 2021/8/25 12:41 PM
import unittest

from ddt import ddt, file_data, data

import config
from common.base_requests import BaseCommon
import os
import random


@ddt
class PhoneForToken(BaseCommon):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # @file_data("../../config/configdata.yaml")
    # def test_phone01(self, phone, code):
    #     """判断响应结果是否包含字段code==0"""
    #     url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
    #     body = {
    #         "phone": phone,
    #         "code": code
    #     }
    #     # body = {
    #     #     "phone": config.message['user']['phone'],
    #     #     "code": random.randint(1000, 9999)
    #     # }
    #     # print(f"请求参数: {body}")
    #     res = BaseCommon.request(method='get', url=url, params=body)
    #     token = res.json()['data']['token']
    #     # print(f'token = {token}')
    #     self.assertEqual(0, res.json()['code'])
    #     return token

    @file_data("../../config/configdata.yaml")
    def test_phone02(self, phone, code):
        """判断响应结果是否包含字 success字段值"""

        url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
        body = {
            "phone": phone,
            "code": code
        }
        # body = {
        #     "phone": config.message['user']['phone'],
        #     "code": random.randint(1000, 9999)
        # }
        # print(f"请求参数: {body}")
        try:
            res = BaseCommon.request(method='get', url=url, params=body)
            # token = res.json()['data']['token']
            # print(f'token = {token}')
            self.assertEqual("success", res.json()['message'])
        except TypeError:
            raise '手机号码有误'


if __name__ == '__main__':
    # test_dir = os.path.dirname(__file__)
    # testcase_path = os.path.join(test_dir,'/*.py')
    # print(test_dir)
    # print(testcase_path)
    # suite = unittest.defaultTestLoader.discover('/Users/lindehao/PycharmProjects/qx_webapi/testcase/requests_token',
    #                                             pattern='test*.py')
    # unittest.main(defaultTest=suite)

    # 把需要执行的用例放入列表，然后把列表添加到测试集addTests(testcase)，然后直接执行测试集的用例
    testcase = [PhoneForToken('test_phone01'), PhoneForToken('test_phone02')]
    suite = unittest.TestSuite.addTests(testcase)
    unittest.main(defaultTest=suite)
