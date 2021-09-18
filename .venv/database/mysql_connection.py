import MySQLdb
import os
import sys
sys.path.append(os.pardir)
# from .. import config
import config  # noqa


class MysqlConnection(object):
    mysql_conn = None
    mysql_cursor = None

    def __init__(self):
        MysqlConnection.mysql_connection()

    def __del__(self):
        MysqlConnection.mysql_cursor = None
        MysqlConnection.mysql_conn = None

    @classmethod
    def mysql_connection(cls):

        if MysqlConnection.mysql_conn.__class__.__name__ == "Connection":
            return

        try:
            if config.DEBUG:
                conn = MySQLdb.connect(
                    user='root', passwd='root', host='localhost', db='slot_DB')
            else:
                DB_HOSTNAME = config.DB_HOSTNAME
                DB_NAME = config.DB_NAME
                DB_USERNAME = config.DB_USERNAME
                DB_PASSWORD = config.DB_PASSWORD
                conn = MySQLdb.connect(
                    user=DB_USERNAME, passwd=DB_PASSWORD, host=DB_HOSTNAME, db=DB_NAME, charset="utf8")

            MysqlConnection.mysql_conn = conn
            MysqlConnection.mysql_cursor = conn.cursor()
        except Exception as e:
            print("mysqlの接続に失敗しました。" + str(e))
