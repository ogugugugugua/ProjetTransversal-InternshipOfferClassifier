import persistqueue
from store_result import StoreResult
import os
from utils import abs_path

class Consumer:
    def __init__(self, feed_hyperplan):
        self.feeder = feed_hyperplan
        self.q = persistqueue.SQLiteQueue(os.path.join(os.path.dirname(__file__), abs_path('queue')), auto_commit=True)


    def consume(self):
        print("En attente d'offres...")
        while True:
            offer_data = self.q.get()
            self.feeder.classify(offer_data["id"], offer_data["clean_text"])
