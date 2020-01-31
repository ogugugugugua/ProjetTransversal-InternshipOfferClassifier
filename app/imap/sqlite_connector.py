import sqlite3


class SQLiteConnector:
    def __init__(self, db_path):
        self.cursor = None
        self.sqliteConnection = None

        try:
            self.sqliteConnection = sqlite3.connect(db_path)
            self.cursor = self.sqliteConnection.cursor()
            print("Connexion a la base de donnees avec succes.")
        except Exception as error:
            print(error)

    def run_script(self, path: str):
        try:
            with open(path, 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            self.cursor.executescript(sql_script)
            print("Script execute avec succes.")
        except Exception as error:
            print(error)      
    
    
    def close(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()
