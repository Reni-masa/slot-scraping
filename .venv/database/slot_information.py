from .Mysql_connection import MysqlConnection


class SlotInformation(MysqlConnection):
    # すべての情報を取得する
    def getAll(self):
        try:
            cursor = MysqlConnection.mysql_cursor
            sql = 'SELECT * FROM slot_information WHERE enabled = 1 ORDER BY id;'
            cursor.execute(sql)

            return cursor.fetchall()
        except Exception as e:
            print(e)
