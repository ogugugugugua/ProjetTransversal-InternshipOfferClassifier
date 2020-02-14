import sys
sys.path.append('../../')

from sqlite_connector import SQLiteConnector
from utils import abs_path


class StoreMails(SQLiteConnector):
    def __init__(self, db_path):
        super(StoreMails, self).__init__(db_path)
        if self.sqliteConnection and self.cursor:
            try:
                query = '''CREATE TABLE IF NOT EXISTS mail_offer (
                            id	INTEGER PRIMARY KEY,
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
    
    def write_result(self, mail_id: int, sender: str, subject: str, date: str, body, attachment):
        if self.sqliteConnection and self.cursor:
            try:
                query = "INSERT OR REPLACE INTO mail_offer(id, sender, subject, date, body, attachment) VALUES (%d, '%s', '%s', '%s', '%s', '%s')" % (mail_id, sender, subject, date, body, attachment)
                self.cursor.execute(query)
                self.sqliteConnection.commit()
                print("Mail sauvegarde.")
            except Exception as error:
                print(error)
