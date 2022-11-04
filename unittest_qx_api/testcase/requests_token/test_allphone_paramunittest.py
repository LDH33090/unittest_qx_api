# # -*- coding: utf-8 -*-
#
# # 用例  ID:
# # 用例标题: 登录接口手机号边界值，以及等价类校验，响应结果的验证
# # 预置条件: 可用白名单和不可用的手机号，正确的验证码
# # 测试步骤:
# #   1.调用接口：sigin
# #   2.传入账号，验证码，请求url，header发起get请求
# # 预期结果:
# #   1.登录成功，
# #   2.检查响应码为：200，{"code":0,"message":"success"}
# # 脚本作者: 林德浩
# # 写作日期: 2021/8/25 10:41 PM
# import unittest
#
# import paramunittest
# from ddt import ddt, file_data, data
#
# import config
# from common.base_requests import BaseCommon
# import os
# import random
#
# """@paramunittest.parametrized()参数化 ， 写死在代码中不好维护"""
#
#
# @paramunittest.parametrized(
#     {"phone": '13530633090', "code": random.randint(0, 10000)},
#     {"phone": '1353063309', "code": random.randint(0, 10000)},
#     {"phone": '135306330901', "code": random.randint(0, 10000)},
#     {"phone": '13500059020', "code": random.randint(0, 10000)},
#     {"phone": '13923729611', "code": random.randint(0, 10000)}
# )
# class PhoneForToken(BaseCommon):
#
#     def setParameters(self, phone, code):
#         self.phone = phone
#         self.code = code
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         pass
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         pass
#
#     def test_phone01(self):
#         """【登录接口】判断响应结果是否包含字段code==0"""
#         url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
#         body = {
#             "phone": self.phone,
#             "code": self.code
#         }
#         # body = {
#         #     "phone": config.message['user']['phone'],
#         #     "code": random.randint(1000, 9999)
#         # }
#         # print(f"请求参数: {body}")
#         res = BaseCommon.request(method='get', url=url, params=body)
#         token = res.json()['data']['token']
#         # print(f'token = {token}')
#         self.assertEqual(0, res.json()['code'])
#
#         return token
#
#     def test_phone02(self):
#         """【登录接口】判断响应结果是否包含字 success字段值"""
#
#         url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
#         body = {
#             "phone": self.phone,
#             "code": self.code
#         }
#         # body = {
#         #     "phone": config.message['user']['phone'],
#         #     "code": random.randint(1000, 9999)
#         # }
#         # print(f"请求参数: {body}")
#         try:
#             res = BaseCommon.request(method='get', url=url, params=body)
#             # token = res.json()['data']['token']
#             # print(f'token = {token}')
#             self.assertEqual("success", res.json()['message'])
#         except Exception:
#             raise Exception
#
#
# if __name__ == '__main__':
#     # test_dir = os.path.dirname(__file__)
#     # testcase_path = os.path.join(test_dir,'/*.py')
#     # print(test_dir)
#     # print(testcase_path)
#     # suite = unittest.defaultTestLoader.discover('/Users/lindehao/PycharmProjects/qx_webapi/testcase/requests_token',
#     #                                             pattern='test*.py')
#     # unittest.main(defaultTest=suite)
#
#     # 把需要执行的用例放入列表，然后把列表添加到测试集addTests(testcase)，然后直接执行测试集的用例
#     testcase = [PhoneForToken('test_phone01'), PhoneForToken('test_phone02')]
#     suite = unittest.TestSuite.addTests(testcase)
#     unittest.main(defaultTest=suite)
