# -*- coding: utf-8 -*-

import logging
import os

def log(message):
    # 设定日志名称
    logger = logging.getLogger('pytest_qx_logs')

    # 指定日志等级
    logger.setLevel(logging.DEBUG)

    # 设定日志 内容显示的格式
    log_message = f'[%(asctime)s] [%(filename)s] [line:%(lineno)d] [%(levelname)s] [%(message)s]'

    # 格式化日志
    formatter = logging.Formatter(log_message)

    # 设定日志显示在控制台输出
    sh = logging.StreamHandler()
    # 控制台暑输出日志格式化
    sh.setFormatter(formatter)
    # 设定 控制台输出日志的级别
    sh.setLevel(logging.DEBUG)
    # 把日志流放入处理器
    logger.addHandler(sh)

    # 设定日志输出的目录位置
    logs_dir = os.path.join(os.path.dirname(__file__), '../logs')
    # 判断目录是否存在，不存在就新建
    if not os.path.exists(logs_dir):
        os.mkdir(logs_dir)
    # 设定日志内容输出到指定的文件
    logfile = os.path.join(logs_dir, 'qx.log')

    # 设定日志输出到文件流的方法
    fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
    # 设定日志格式化
    fh.setFormatter(formatter)
    # 设定日志输出到文件的 日志等级
    fh.setLevel(logging.DEBUG)

    # 添加日志文件流到处理器
    logger.addHandler(fh)

    return logger.info(message)


if __name__ == '__main__':
    log('qx_logs')
