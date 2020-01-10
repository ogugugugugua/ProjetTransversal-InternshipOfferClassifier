import persistqueue
from store_result import StoreResult
import os

class Consumer:
    def __init__(self, feed_hyperplan):
        self.feeder = feed_hyperplan
        self.q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), 'queue'), auto_commit=True)

        self.writer = StoreResult()
        self.writer.connect(os.path.join(os.path.dirname(__file__), "classification_db/offer_classification.db"))


    def consume(self):
        while True:
            offer_data = self.q.get()
            result = self.feeder.classify(offer_data["clean_text"])
            print(offer_data)
            print(result)
            self.writer.write_result(offer_data["id"], result)
