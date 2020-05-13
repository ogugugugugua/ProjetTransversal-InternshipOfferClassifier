import sys
sys.path.append('../')

from sqlite_connector import SQLiteConnector
from utils import abs_path

class DBConnector(SQLiteConnector):
    
    def __init__(self, db_path):
        
        super(DBConnector, self).__init__(db_path)
                                          
    def fetch_categories(self):
        
        if self.sqliteConnection and self.cursor:
            try:
                query = "SELECT DISTINCT category FROM offer_classification ORDER BY category"
                self.cursor.execute(query)
                self.sqliteConnection.commit()
    
                return self.cursor.fetchall()
            except Exception as error:
                print(error)
    
    def fetch_offers(self):
        
         if self.sqliteConnection and self.cursor:
            try:
                query = "SELECT id, category FROM offer_classification ORDER BY category"
                self.cursor.execute(query)
                self.sqliteConnection.commit()
    
                return self.cursor.fetchall()
            except Exception as error:
                print(error)
        
