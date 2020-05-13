from mlbackend.project import Project
from algorithms.tf_idf_heuristic.classifier import predict as simple_heuristic
from algorithms.multinomial_nb_sklearn.classifier import predict as mnb_clf
from store_result import StoreResult
from utils import abs_path
from datetime import datetime

class FeedHyperplan:
    """Contient le projet Hyperplan, mécanisme de demande de prédiction"""

    def __init__(self):
        self.project = Project(
            "offer_classifier",
            # Ajout du modèle MultinomialNB au projet
            prediction_functions=[
                mnb_clf
            ]
        )

        # Writer qui permet de stocker les résultats de la prédiction
        self.writer = StoreResult(abs_path("databases/offer_classification.db"))
        # Enregistrement de la procédure de stockage en tant que hook de post processing Hyperplan (voir la doc officielle)
        self.project.register_post_hook(self.writer)

        

    def classify(self, offer_id, string_to_feed): 
        """Envoi des textes nettoyés récupérés depuis la pile vers le classifieur du projet Hyperplan
        
        Parametres:
            offer_id (int): Id de l'offre
            string_to_feed (string): "Texte de l'offre nettoyée"

        Retour:
            result (dict): probabilités
        """
        result = self.project.predict(string_to_feed, 'string', {'id': offer_id, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        return result