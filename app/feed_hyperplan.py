from mlbackend.project import Project
from algorithms.tf_idf_heuristic.classifier import predict as simple_heuristic
from store_result import StoreResult
from utils import abs_path
from datetime import datetime

def pre(text):
    return text

class FeedHyperplan:

    def __init__(self):
        self.project = Project(
            "offer_classifier",
            prediction_functions=[
                simple_heuristic
            ]
        )

        self.writer = StoreResult(abs_path("databases/offer_classification.db"))
        # self.project.selection_function(self.project.prediction_functions, 0)
        self.project.register_post_hook(self.writer)

        

    def classify(self, offer_id, string_to_feed): 
        result = self.project.predict(string_to_feed, 'string', {'id': offer_id, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        return result