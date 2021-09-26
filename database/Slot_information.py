from .Mysql_connection import MysqlConnection


class SlotInformation(MysqlConnection):
    # すべての情報を取得する
    def getAll(self):
        try:

            sql = 'SELECT * FROM slot_information WHERE enabled = 1 ORDER BY id;'
            self.mysql_cursor.execute(sql)

            return self.mysql_cursor.fetchall()
        except Exception as e:
            print(e)
