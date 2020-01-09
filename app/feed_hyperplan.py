from hyperplan_auth import Auth
import requests
import json


class FeedHyperplan:
    def __init__(self):
        self.auth = Auth()
        self.auth.authenticate()
        self.result_file = "result.json"
        self.string_to_feed = ""

    def extract_string_from_file(self, file_path):
        with open(file_path) as file:
            return file.read()

    def classify(self, string_to_feed):        
        url = 'http://localhost:8080/predictions'
        body =  {"projectId" :  "offerClassifier", 
                                "features" : {
                                    "text" : string_to_feed 
                                }
                }

        headers = {'Authorization': 'Bearer {}'.format(self.auth.token),'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=body, headers=headers)
        # Le parametre json permet d'echapper les caracteres spéciaux autoamtiquement

        json_response = r.json()
        labels = json_response['labels']

        # Catégorie avec la plus haute catégorie

        highest_probability = 0
        bestfit_category = ""

        for labels_result in labels:
            # print(labels_result)
            if labels_result['probability'] > highest_probability:
                bestfit_category = labels_result['label']

        return bestfit_category

        # with open(self.result_file, "w+") as file:
        #     json.dump(labels, file, indent=4)
