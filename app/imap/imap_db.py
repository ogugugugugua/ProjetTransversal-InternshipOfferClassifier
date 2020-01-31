from sqlite_connector import SQLiteConnector
from utils import abs_path


class StoreMails(SQLiteConnector):
    def __init__(self, db_path):
        super(StoreMails, self).__init__(db_path)
        if self.sqliteConnection and self.cursor:
            try:
                query = '''CREATE TABLE IF NOT EXISTS mail_offer (
                            id	INTEGER PRIMARY KEY AUTOINCREMENT,
                            sender	TEXT,
                            subject	TEXT,
                            date	TEXT,
                            body    BLOB,
                            attachment BLOB
                        )'''
                self.cursor.execute(query)
                self.sqliteConnection.commit()
            except Exception as error:
                print(error)
