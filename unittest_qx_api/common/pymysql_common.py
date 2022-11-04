# -*- coding: utf-8 -*-

# 用例  ID: 
# 用例标题: 
# 预置条件:
# 测试步骤:
#
# 预期结果:
#
# 脚本作者: 林德浩
# 写作日期: 2021/10/28 2:33 AM

import pymysql

"""
封装mysql数据 增删改查公共方法
"""


class Db_Util():
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.mydb = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=database,
                                    port=port)
        self.cursor = self.mydb.cursor(cursor=pymysql.cursors.DictCursor)

    #关闭数据库链接池
    def __del__(self):
        self.mydb.close()
        self.cursor.close()

    # 查询方法
    def selecttest(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    # 删除方法
    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            print('在删除数据库时发生错误了：{0}'.format(e))

    # 更新方法
    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            print('在更新数据库时发生错误了：{0}'.format(e))

    # 添加方法
    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            print('在插入数据时发生错误了：{0}'.format(e))

# if __name__ == '__main__':
#     db = Db_util()
#     print(db.selecttest('SELECT * from `case` where app = "xxxxx"'))
