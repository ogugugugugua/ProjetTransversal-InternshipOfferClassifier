import sqlite3


class SQLiteConnector:
    def __init__(self):
        self.cursor = None
        self.sqliteConnection = None

    def run_script(self, path):
        try:
            with open(path, 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            self.cursor.executescript(sql_script)
            print("Script execute avec succes.")
        except Exception as error:
            print(error)

        
    def connect(self, db_path):
        try:
            self.sqliteConnection = sqlite3.connect(db_path)
            self.cursor = self.sqliteConnection.cursor()
            print("Connexion a la base de donnees avec succes.")
        except Exception as error:
            print(error)
    
    
    def close(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()
