# -*- coding: utf-8 -*-

# 用例  ID: 
# 用例标题: 
# 预置条件:
# 测试步骤:
#
# 预期结果:

# 脚本作者: 林德浩
# 写作日期: 2021/10/28 10:40 AM
import os.path
import logging


class Logger:
    str_message = f'[%(asctime)s] [%(process)d] [%(pathname)s] [%(levelname)s]: [%(message)s]'

    def __init__(self):
        self.log_dir = os.path.join(os.path.dirname(__file__), '../logs')
        self.log_path = os.path.join(self.log_dir, 'qx.log')
        self.format_str = self.str_message
        self.format_end = logging.Formatter(self.format_str)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        self.set_console_logger()
        self.set_file_logger()

    def set_console_logger(self):
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(self.format_end)
        self.logger.addHandler(consoleHandler)

    def set_file_logger(self):
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
        fileHandler = logging.FileHandler(self.log_path, mode='a', encoding='utf-8')
        fileHandler.setFormatter(self.format_end)
        fileHandler.setLevel(logging.DEBUG)
        self.logger.addHandler(fileHandler)

    def set_input(self, message):
        return self.logger.info(message)


# if __name__ == '__main__':
#     # log = Logger()
#     # log.set_input('你好')
#     pass
