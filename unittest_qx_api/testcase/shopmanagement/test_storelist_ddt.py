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

# https://qx-mall-test.belle.net.cn/v2/admin/shop/list?shopNo=&payStatus=&existShopOwner=&orderType=&pageNo=1&pageSize=20
import json
import unittest

import paramunittest
from ddt import ddt, data, file_data

from common.base_requests import BaseCommon
from common.token_common import getToken

from common.pymysql_common import Db_Util

"""类加载之前的参数化"""


@paramunittest.parametrized(
    {
        "shopNo": "",
        "payStatus": "",
        "existShopOwner": "",
        "orderType": "",
        "pageNo": 1,
        "pageSize": 20
    }
)
@ddt
class StoreList(BaseCommon):
    host = ''
    user = ''
    password = ''
    database = ''
    port = ''
    sql = 'delete/insert语句'

    @classmethod
    def setUpClass(cls) -> None:
        # cls.gettoken = getToken()
        global token
        token = getToken()
        cls.url = f'https://qx-mall-test.belle.net.cn/v2/admin/shop/list?shopNo=&payStatus=&existShopOwner=&orderType=&pageNo=1&pageSize=20'
        cls.headers = {'token': token}

    # 增加删除数据的 接口的数据库清理数据
    @classmethod
    def tearDownClass(cls) -> None:
        # host = ''
        # user = ''
        # password = ''
        # database = ''
        # port = ''
        # sql = 'delete/insert语句'
        Db_Util(cls.host, cls.user, cls.password, cls.database, cls.port).delete(cls.sql)
        Db_Util(cls.host, cls.user, cls.password, cls.database, cls.port).insert(cls.sql)

    def setParameters(self, shopNo, payStatus, existShopOwner, orderType, pageNo, pageSize):
        self.shopNo = shopNo
        self.payStatus = payStatus
        self.existShopOwner = existShopOwner
        self.orderType = orderType
        self.pageNo = pageNo
        self.pageSize = pageSize

    @file_data('../../testdatas/shopmanagement_data/store.json')
    def test_shoplist01(self, shopNo, payStatus, existShopOwner, orderType, pageNo, pageSize):
        """【店铺列表接口】请求参数非填，必填校验"""
        body = {
            'shopNo': shopNo,
            'payStatus': payStatus,
            'existShopOwner': existShopOwner,
            'orderType ': orderType,
            'pageNo': pageNo,
            'pageSize': pageSize
        }

        # print('token 值----', header)
        res = self.request(method='get', url=self.url, headers=self.headers, json=body)
        # print(res.json())
        return res.json()

    @file_data('../../testdatas/shopmanagement_data/store.json')
    def test_shoplist02(self, shopNo, payStatus, existShopOwner, orderType, pageNo, pageSize):
        """【店铺列表接口】断言接口响应结果code的值是否==0"""
        body = {
            'shopNo': shopNo,
            'payStatus': payStatus,
            'existShopOwner': existShopOwner,
            'orderType ': orderType,
            'pageNo': pageNo,
            'pageSize': pageSize
        }
        res = self.request(method='get', url=self.url, headers=self.headers, json=body)
        self.assertEqual(0, res.json()['code'])

    @file_data('../../testdatas/shopmanagement_data/store.json')
    def test_shoplist03(self, shopNo, payStatus, existShopOwner, orderType, pageNo, pageSize):
        """【店铺列表接口】断言响应结果 success==响应字段message的value"""
        body = {
            'shopNo': shopNo,
            'payStatus': payStatus,
            'existShopOwner': existShopOwner,
            'orderType ': orderType,
            'pageNo': pageNo,
            'pageSize': pageSize
        }
        res = self.request(method='get', url=self.url, headers=self.headers, json=body)
        self.assertEqual('success', res.json()['message'])

    def test_shoplist04(self):
        # 使用@paramunittest.parametrized 参数化
        """【店铺列表接口】断言 请求参数 pageSize==响应参数pageSize"""
        # print(getToken())
        # body = {
        #     'shopNo': self.shopNo,
        #     'payStatus': self.payStatus,
        #     'existShopOwner': self.existShopOwner,
        #     'orderType ': self.orderType,
        #     'pageNo': self.pageNo,
        #     'pageSize': self.pageSize
        # }

        res = self.request(method='get', url=self.url, headers=self.headers)
        self.assertEqual(self.pageSize, int(res.json()['data']['pageResp']['pageSize']))

    def test_shoplist05(self):
        # 使用@paramunittest.parametrized 参数化
        """【店铺列表接口】断言 请求参数pageNo==响应参数pageNo"""
        res = self.request(method='get', url=self.url, headers=self.headers)
        self.assertEqual(self.pageNo, res.json()['data']['pageResp']['pageNo'])

    def test_shoplist06(self):
        """ 断言响应结果中是否包含了success """
        res = self.request(method='get', url=self.url, headers=self.headers)
        self.assertIn('success', res.text)


# if __name__ == '__main__':
#     testCases = [StoreList('test_shoplist01'), StoreList('test_shoplist02'), StoreList('test_shoplist03'),
#                  StoreList('test_shoplist04'), StoreList('test_shoplist05'), StoreList('test_shoplist06')]
#     suite = unittest.TestSuite()
#     suite.addTests(testCases)
#     unittest.main(defaultTest=suite)

    """单个方法测试用例执行"""
    # suite = unittest.TestSuite()
    # suite.addTest(StoreList('test_shoplist05'))
    # unittest.main(defaultTest=suite)
