import persistqueue
from store_result import StoreResult
import os
from utils import abs_path

class Consumer:
    def __init__(self, feed_hyperplan):
        self.feeder = feed_hyperplan
        self.q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), abs_path('queue')), auto_commit=True)

        # self.writer = StoreResult()
        # self.writer.connect(os.path.join(os.path.dirname(__file__), "classification_db/offer_classification.db"))


    def consume(self):
        print("En attente d'offres...")
        while True:
            offer_data = self.q.get()
            print(offer_data)
            # self.feeder.classify(offer_data["id"], offer_data["clean_text"])
