import requests, json
from requests.auth import HTTPBasicAuth

class StrawberryApi(object):
    """
    """
    username = "bostjan"
    password = "bostjanNovak1"
    domain = "http://localhost"
    port = "8000"
    base_link = "{domain}:{port}".format(domain=domain, port=port)
    
    links = { 
        "clients": base_link + "/webservice/clients/",
        "clients_detail": base_link + "/webservice/clients/12"
    }
    def __init__(self, username=None, password=None):
        if username and password:
            self.username = username
            self.password = password

        self.login(username, password)

    def login(self, username, password):
        self.connection = requests.Session()
        self.connection.auth = (self.username, self.password)


  

