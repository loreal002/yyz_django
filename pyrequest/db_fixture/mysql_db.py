# import pymysql
# import pymysql.cursors
# import os
# import configparser as cparser
# #读取数据库配置文件
# base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# # base_dir = base_dir.replace("\\",'/')
# # print(base_dir)
# file_path = str(base_dir  + "/db_config.ini")
# print(file_path)
# cf = cparser.ConfigParser()
# cf.read(file_path)
# # host=127.0.0.1
# # user=root
# # password=root
# # port=3308
# # db_name=guest
# host = cf.get("mysqlconf","host")
# user = cf.get("mysqlconf","user")
# password = cf.get("mysqlconf","password")
# port = cf.get("mysqlconf","port")
# db = cf.get("mysqlconf","db_name")
#
# #数据库基本操作
#
# class DB:
#     def __init__(self):
#     # Connect to the database
#         try:
#             self.connection = pymysql.connect(host=host,
#                                            user=user,
#                                            password=password,
#                                            port=int(port),
#                                            db=db,
#                                            charset='utf8mb4',
#                                            cursorclass=pymysql.cursors.DictCursor
#                                            )
#         except pymysql.err.OperationalError as e:
#             print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
#
#     # clear table data
#     def clear(self,table_name):
#         real_sql = "delete from " + table_name + ";"
#         with self.connection.cursor() as cursor:
#             cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
#             cursor.execute(real_sql)
#         self.connection.commit()
#
#     # insert sql statement
#     def insert(self,table_name,table_data):
#         for key in table_data:
#             table_data[key] = "'"+str(table_data[key])+"'"
#             key = ','.join(table_data.keys())
#             print(key)
#             value = ','.join([  str(x) for x in table_data.values()])
#             print(value)
#             real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
#             with self.connection.cursor() as cursor:
#                 cursor.execute(real_sql)
#             self.connection.commit()
#
# # c#close database
#     def close(self):
#         self.connection.close()
#
# if __name__ == '__main__':
#     db = DB()
#     table_name = "sign_guest"
#     #data = {'id':1,'name':'红米','`limit`':2000,'status':1,'address':'北京会展中心',"start_time":'2016-08-20'}
#     table_name2 = "sign_guest"
#     data2 = {'realname':'alen','phone':12312341234,'email':"alen@mail.com",'sign':0,'event_id':1}
#
#     db.clear(table_name)
#     db.insert(table_name, data2)
#     db.close()
#
import pymysql.cursors
from os.path import abspath, dirname
import configparser as cparser


# ======== Reading db_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db   = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ======== MySql base operating ===================
class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':

    db = DB()
    table_name = "sign_event"
    table_name2 = "guest_event"
    data = {'id':1,'name':'红米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2016-08-20 00:25:42'}
    table_name2 = "sign_guest"
    data2 = {'realname':'alen','phone':12312341234,'email':'alen@mail.com','sign':0,'event_id':1}

    db.clear(table_name)
    db.insert(table_name, data)
    db.insert(table_name2, data2)
    db.close()