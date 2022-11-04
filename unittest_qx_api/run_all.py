# -*- coding: utf-8 -*-

"""
   执行测试用例，以及生成测试报告的三种方式，采用了HtmltestRunner，BeautifulReport
"""
import os
import time
import unittest

import BeautifulReport

import testcase.shopmanagement.test_storelist_ddt
from common.base_requests import BaseCommon
from testcase.shopmanagement import test_storelist_ddt
import HTMLTestRunner

"""HtmlTestRunner测试报告展示"""


class ReportTest:

    def report01(self):
        # 1.定义时间戳，防止每次测试报告覆盖
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # 定义要跑用例的路径
        case_path = os.path.split(os.path.abspath(__file__))[0] + "/testcase"
        print(case_path)
        # 生成的html测试报告存放的目录
        report_path = os.path.split(os.path.abspath(__file__))[0] + "/report"
        print(report_path)

        # # 生成的html测试报告存放的目录
        report_file = report_path + '/result_' + str(now)
        print(report_file)

        if not os.path.exists(report_file):
            os.mkdir(report_file)

        # 定义用于存放html报告的路径
        report_html = os.path.join(report_file, str(now) + ".html")

        # 定义测试集 ,把需要跑用的用例的.py文件放到测试集里面
        suite = unittest.defaultTestLoader.discover(case_path, pattern='*.py')

        # # 进入目录
        # os.chdir(report_file)

        if not os.path.exists(report_html):
            os.system(r"sudo touch {}".format(report_html))

        write_report = open(report_html, 'wb')

        runner = HTMLTestRunner.HTMLTestRunner(stream=write_report, verbosity=2, title='千选接口自动化测试报告',
                                               description='测试用例如下',
                                               tester='林德浩')
        runner.run(suite)

        time.sleep(5)

        write_report.close()

    def report02(self):
        now = time.strftime('%Y%m%d%H%M%S', time.localtime())
        report_dir_path = os.path.split(os.path.abspath(__file__))[0] + '/report'

        report_file_html = os.path.join(report_dir_path + '/result', str(now) + ".html")

        suit = unittest.TestSuite()
        loader_case = unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=test_storelist_ddt.StoreList)
        suit.addTests(loader_case)

        if not os.path.exists(report_dir_path):
            os.mkdir(report_dir_path)

        if not os.path.exists(report_file_html):
            os.system(r"sudo touch {}".format(report_file_html))

        run_result = BeautifulReport.BeautifulReport(suit)
        run_result.report(description='千选接口自动化测试', report_dir=report_file_html)

    """BeautifulReport展示测试报告"""

    def report03(self):
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        report_dir_path = os.path.split(os.path.abspath(__file__))[0] + '/report'
        report_file_html = os.path.join(report_dir_path + '/result', str(now) + '.hml')

        if not os.path.exists(report_dir_path):
            os.mkdir(report_dir_path)

        if not os.path.exists(report_file_html):
            os.system(r'sudo touch {}'.format(report_file_html))

        testcase_path = os.path.split(os.path.abspath(__file__))[0] + '/testcase'
        suite = unittest.defaultTestLoader.discover(start_dir=testcase_path, pattern='*.py')
        result = BeautifulReport.BeautifulReport(suite)

        """ 
                   生成测试报告,并放在当前运行路径下
               :param report_dir: 生成report的文件存储路径
               :param filename: 生成文件的filename
               :param description: 生成文件的注释
               :param theme: 报告主题名 theme_default theme_cyan theme_candy theme_memories
               :return:
        """
        result.report(description='千选接口自动化测试', filename='自动化测试报告',
                      report_dir=report_file_html)


if __name__ == '__main__':
    r = ReportTest()
    r.report03()
