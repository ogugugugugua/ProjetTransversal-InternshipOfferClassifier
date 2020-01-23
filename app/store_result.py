from sqlite_connector import SQLiteConnector
import os
import json

class StoreResult(SQLiteConnector):
    def __init__(self, db_path):
        super(StoreResult, self).__init__(db_path)
        if self.sqliteConnection and self.cursor:
            try:
                query = '''CREATE TABLE IF NOT EXISTS offer_classification (
                            id	INTEGER PRIMARY KEY AUTOINCREMENT,
                            labels	TEXT,
                            category	TEXT
                        )'''
                self.cursor.execute(query)
                self.sqliteConnection.commit()
            except Exception as error:
                print(error)

    def write_result(self, offer_id: int, labels: str, category: str):
        if self.sqliteConnection and self.cursor:
            try:
                query = "INSERT OR IGNORE INTO offer_classification(id, labels, category) VALUES (%d, '%s', '%s') ON CONFLICT(id) DO UPDATE SET category=excluded.category;" % (offer_id, labels, category)
                self.cursor.execute(query)
                self.sqliteConnection.commit()
                print("Offre classifie sauvegarde.")
            except Exception as error:
                print(error)

        
    def __call__(self, text: list, labels: dict, metadata: dict):
        category = labels['label'][max(labels['probability'], key=labels['probability'].get)]
        labels_json = json.dumps(labels)
        self.write_result(metadata["id"], labels_json, category)
            