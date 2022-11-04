# -*- coding: utf-8 -*-

import yaml
import os
import config

"""封装读取yaml文件的方法"""

# yaml_path = '/Users/lindehao/PycharmProjects/unittest_qx_api/config/configdata.yaml'
# yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'config/configdata.yaml')
yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'config/configdata.yaml')
print(yaml_path)


def read_yaml_file():
    with open(yaml_path, mode='r', encoding='utf-8') as f:
        file_message = yaml.load(f, Loader=yaml.FullLoader)
        return file_message


# if __name__ == '__main__':
#     print(read_yaml_file())
