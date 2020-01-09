from sqlite_connector import SQLiteConnector
import os

class StoreResult(SQLiteConnector):
    def write_result(self, offer_id, category):
        if self.sqliteConnection and self.cursor:
            try:
                query = "INSERT OR IGNORE INTO offer_classification(id, category) VALUES (%d, '%s') ON CONFLICT(id) DO UPDATE SET category=excluded.category;" % (offer_id, category)
                self.cursor.execute(query)
                self.sqliteConnection.commit()
                print("Offre classifie sauvegarde.")
            except Exception as error:
                print(error)

# sr = StoreResult()
# sr.connect(os.path.join(os.path.dirname(__file__), "classification_db/offer_classification.db"))
# # sr.run_script("classification_db/result_tables.sql")
# sr.write_result(0, "Developpement")
# sr.close()
            