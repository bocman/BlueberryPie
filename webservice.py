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
    timers = []

    links = {
        "clients": settings.BASE_LINK + "/webservice/clients/",
        "update_client": settings.BASE_LINK + "/webservice/clients/" + str(settings.CLIENT_ID) + "/"
    }

    def __init__(self, username=None, password=None):
        if username and password:
            self.username = username
            self.password = password

        self.login(username, password)

        self.initialize_threads()
        self.initialize_event_timers()

    def login(self, username, password):
        self.connection = requests.Session()
        self.connection.auth = (self.username, self.password)

    def initialize_threads(self):
        self.threads.append(Thread(target=self.update_client))

    def initialize_event_timers(self):
        self.timers.append(RepeatedTimer(1, self.update_client))

    def send_data(self, page_url, data):
        data = json.dumps(data)
        headers = {'Content-type': 'application/json'}
        a = self.connection.patch(
            url=page_url,
            data=data,
            headers=headers
        )

    def update_client(self, data=None):
        print "sem notri"
        test_data = {
            'name': 'Janez',
            'description': 'Jerebica',
            'status': True,
            'port': 1991
        }
        self.send_data(self.links['update_client'], test_data)
