import requests
import json
import sched
import time
import psutil
from requests.auth import HTTPBasicAuth
from threading import Thread
import datetime

import settings
from utils import RepeatedTimer

import logging

log = logging.getLogger(__name__)


class StrawberryAPI(object):

    """
    TODO
    """
    username = settings.USERNAME
    password = settings.PASSWORD
    threads = []
    timers = []

    links = {
        "clients": settings.BASE_LINK + "/webservice/clients/",
        "update_client": settings.BASE_LINK + "/webservice/clients/" + str(settings.CLIENT_KEY) + "/",
        "client": settings.BASE_LINK + "/webservice/clients/" + str(settings.CLIENT_KEY) + "/"
    }

    def __init__(self, username=None, password=None):
        if username and password:
            self.username = username
            self.password = password

        self.login(username, password)
        self.update_client_status()

        self.initialize_threads()
        self.initialize_event_timers()

    def login(self, username, password):
        self.connection = requests.Session()
        self.connection.auth = (self.username, self.password)

    def initialize_threads(self):
        self.threads.append(Thread(target=self.update_client))

    def initialize_event_timers(self):
        """
        This method initialize timers for functions. Here we tell how offten and
        after some certain time is some function periodicly called.
        """
        client_status_interval = 60
        self.timers.append(RepeatedTimer(client_status_interval, self.update_client_status))

    def date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    def send_data(self, page_url, action_type, data=None):
        """
        TODO
        Method which is used to communicate with server.
        :param page_url: Url where we want to make connection
        :param action_type: Type of action. Next types are allowed: 'GET', 'PATCH'
        :param data: Information which we wanna send to server.
        :type page_url: String
        :type action_type: String
        :type data: Dictionary
        """
        data = json.dumps(data, default=self.date_handler)
        headers = {'Content-type': 'application/json'}
        if action_type == "GET":
            print self.connection.get(url=page_url)

        elif action_type == "PATCH":
            self.connection.patch(url=page_url, data=data, headers=headers)

    def update_client(self, data=None):
        self.send_data(self.links['update_client'], "PATCH", data)

    def update_client_status(self):
        self.update_client(data={
            'last_active': datetime.datetime.now()
            })

    def get_client(self, data=None):
        self.send_data(self.links['client'], "GET")


class SystemInfoAPI(object):

    """
    Class, which hold all methods about clients ??? TODO
    """

    def cpu_informations(self):
        """
        TODO
        """
