import requests
import json
import sched
import time
from requests.auth import HTTPBasicAuth
from threading import Thread

import settings
from utils import RepeatedTimer


class StrawberryApi(object):

    """
    TODO
    """
    username = settings.USERNAME
    password = settings.PASSWORD
    threads = []

    links = {
        "clients": settings.BASE_LINK + "/webservice/clients/",
        "update_client": settings.BASE_LINK + "/webservice/clients/" + str(settings.CLIENT_ID) + "/"
    }

    def __init__(self, username=None, password=None):
        if username and password:
            self.username = username
            self.password = password

        self.login(username, password)

        self.threads.append(Thread(target=self.update_client))

        client_update_timer = RepeatedTimer(60, self.update_client)

    def login(self, username, password):
        self.connection = requests.Session()
        self.connection.auth = (self.username, self.password)

    def update_client(self, data=None):
        test_data = {
            'name': 'Janez',
            'description': 'Jerebica',
            'status': True,
            'port': 123
        }

        test_data = json.dumps(test_data)
        headers = {'Content-type': 'application/json'}

        self.connection.patch(
            url=self.links['update_client'],
            data=test_data,
            headers=headers
        )
