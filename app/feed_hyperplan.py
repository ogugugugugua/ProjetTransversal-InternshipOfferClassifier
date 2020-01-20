from mlbackend.project import Project
from algorithms.tf_idf_heuristic.classifier import predict as simple_heuristic

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


    def classify(self, string_to_feed): 
        d = self.project.predict(string_to_feed, 'string', {})
        return d