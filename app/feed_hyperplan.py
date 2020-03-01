from mlbackend.project import Project
from algorithms.tf_idf_heuristic.classifier import predict as simple_heuristic
from algorithms.multinomial_nb_sklearn.classifier import predict as mnb_clf
from store_result import StoreResult
from utils import abs_path
from datetime import datetime

class FeedHyperplan:

    def __init__(self):
        self.project = Project(
            "offer_classifier",
            prediction_functions=[
                mnb_clf
            ]
        )

        self.writer = StoreResult(abs_path("databases/offer_classification.db"))
        # self.project.selection_function(self.project.prediction_functions, 0)
        self.project.register_post_hook(self.writer)

        

    def classify(self, offer_id, string_to_feed): 
        result = self.project.predict(string_to_feed, 'string', {'id': offer_id, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        return result