from hyperplan_auth import Auth
import requests
import json


class FeedHyperplan:
    def __init__(self):
        self.auth = Auth()
        self.auth.authenticate()
        self.result_file = "result.json"

    def classify(self, file_path):
        with open(file_path) as file:
            file_content = file.read()

        file_content
        
        url = 'http://localhost:8080/predictions'
        body =  {"projectId" :  "offerClassifier", 
                                "features" : {
                                    "text" : file_content
                                }
                }

        headers = {'Authorization': 'Bearer {}'.format(self.auth.token),'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=body, headers=headers)
        # Le parametre json permet d'echapper les caracteres spéciaux autoamtiquement

        json_response = r.json()
        labels = json_response['labels']

        with open(self.result_file, "w+") as file:
            json.dump(labels, file, indent=4)
