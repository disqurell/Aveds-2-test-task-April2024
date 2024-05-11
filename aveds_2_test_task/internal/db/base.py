from settings.db import db


class DbBaseController:
    def __init__(self):
        self.conn = None
        self.cur = None

    def establish_connection(self):
        db.connect()
        self.conn = db.get_connection()
        self.cur = self.conn.cursor()

    def select_from_table_with_condition(
        self, table_name: str, condition: str, value: str
    ):
        try:
            select = f"""SELECT * FROM {table_name} WHERE {condition}='{value}';"""
            self.cur.execute(select)
        except Exception:
            self.establish_connection()
            self.cur.execute(select)
        return self.cur.fetchall()


DbController = DbBaseController()
