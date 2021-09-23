from .Mysql_connection import MysqlConnection


class SlotGameData(MysqlConnection):

    def insertSlotGameData(self, slot_id, bonusDataDict):
        try:

            sql = """
                INSERT INTO slot_game_data(
                    number,
                    BB,
                    RB,
                    BB_average,
                    RB_average,
                    total_game,
                    bonus_average,
                    class,
                    date_time,
                    user_id,
                    store_id,
                    slot_id,
                    guess_class1,
                    guess_class2,
                    guess_class3,
                    guess_class4,
                    guess_class5,
                    guess_class6

                ) VALUE (
                    {id},
                    {BB},
                    {RB},
                    '{BB_ave}',
                    '{RB_ave}',
                    {total_game},
                    '{total_ave}',
                    {class},
                    '{data_time}',
                    {user_id},
                    {store_id},
                    {slot_id},
                    {guess_class1},
                    {guess_class2},
                    {guess_class3},
                    {guess_class4},
                    {guess_class5},
                    {guess_class6}
                )
            """

            sql = sql.format(**bonusDataDict).strip()

            cursor = self.mysql_cursor
            cursor.execute(sql)
            self.mysql_conn.commit()

            cursor.close()
            self.mysql_conn.close()
        except Exception as e:
            print('[heroku][slot_scraping][setting_judgement]データの登録に失敗しました。' + str(e))
