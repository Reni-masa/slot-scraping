import MySQLdb
import os
import sys
sys.path.append(os.pardir)
# from .. import config
import config  # noqa


class MysqlConnection(object):

    def __init__(self):
        try:

            if config.DEBUG == 'true':
                conn = MySQLdb.connect(
                    user='root', passwd='root', host='localhost', db='slot_DB')
            else:
                DB_HOSTNAME = config.DB_HOSTNAME
                DB_NAME = config.DB_NAME
                DB_USERNAME = config.DB_USERNAME
                DB_PASSWORD = config.DB_PASSWORD
                conn = MySQLdb.connect(
                    user=DB_USERNAME, passwd=DB_PASSWORD, host=DB_HOSTNAME, db=DB_NAME, charset="utf8")

            self.mysql_conn = conn
            self.mysql_cursor = conn.cursor(
                MySQLdb.cursors.DictCursor)
        except Exception as e:
            print("mysqlの接続に失敗しました。" + str(e))

    def mysql_connection(self):

        try:

            if config.DEBUG == 'true':
                conn = MySQLdb.connect(
                    user='root', passwd='root', host='localhost', db='slot_DB')
            else:
                DB_HOSTNAME = config.DB_HOSTNAME
                DB_NAME = config.DB_NAME
                DB_USERNAME = config.DB_USERNAME
                DB_PASSWORD = config.DB_PASSWORD
                conn = MySQLdb.connect(
                    user=DB_USERNAME, passwd=DB_PASSWORD, host=DB_HOSTNAME, db=DB_NAME, charset="utf8")

            self.mysql_conn = conn
            self.mysql_cursor = conn.cursor(
                MySQLdb.cursors.DictCursor)

        except Exception as e:
            print("mysqlの接続に失敗しました。" + str(e))
