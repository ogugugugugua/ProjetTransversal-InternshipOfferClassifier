import requests
from http.client import RemoteDisconnected
from requests.exceptions import ConnectionError

class Auth:

    def __init__(self):
        self.root_url = "http://localhost:8080"
        self.login = "admin"
        self.password = "admin"
        self.token = None
    

    def authenticate(self):
        try:
            response = requests.post(
                '{}/authentication'.format(self.root_url),
                json = { 
                    "username": self.login,
                    "password": self.password
                }
            )
            if response.status_code == 200:
                self.token = response.json()['token']
                # print(self.token)
            elif response.status_code == 401:
                print('Authentication failed')

        except (RemoteDisconnected, ConnectionError):
            pass
        except Exception as err:
            print(err)

        return response