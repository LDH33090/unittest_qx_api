# # -*- coding: utf-8 -*-
#
# # 用例  ID:
# # 用例标题: 商品列表展示
# # 预置条件:
# #        1.登录后台
# #        2.获取token作为接口的请求头参数
# # 测试步骤:
# #   1.调用接口：shopList
# #   2.传入
# #body = {
#             'shopNo': '',
#             'payStatus': '',
#             'existShopOwner': '',
#             'orderType ': '',
#             'pageNo': 1,
#             'pageSize': 20
#         }
# # 预期结果:
# #   1.显示1页包含20条数据的商品列表的页面
# #   2.检查响应码为：200，各字段正确
# # 脚本作者: 林德浩
# # 写作日期: 2021/8/18 2:21 PM
#
# # https://qx-mall-test.belle.net.cn/v2/admin/shop/list?shopNo=&payStatus=&existShopOwner=&orderType=&pageNo=1&pageSize=20
# import json
#
# from common.base_requests import BaseCommon
# from common.token import getToken
#
#
# class StoreList(BaseCommon):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         # cls.gettoken = getToken()
#         global token
#         token = getToken()
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         pass
#
#     @classmethod
#     def test_shoplist(self):
#         """商品列表"""
#
#         url = f'https://qx-mall-test.belle.net.cn/v2/admin/shop/list'
#         body = {
#             'shopNo': '',
#             'payStatus': '',
#             'existShopOwner': '',
#             'orderType ': '',
#             'pageNo': 1,
#             'pageSize': 20
#         }
#         header = {'token': token}
#         # print('token 值----', header)
#         res = self.request(method='get', url=url, headers=header, params=body)
#         # print(res.json())
#         return res.json()
#
#
# if __name__ == '__main__':
#     StoreList.test_shoplist()
