import json
from threading import Timer


class RepeatedTimer(object):

    """
    TODO
    """

    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj


def send_data(self, url, action_type, data=None):
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
        print "update opravljen"
        data = json.dumps(data, default=date_handler)
        headers = {'Content-type': 'application/json'}
        try:
            if action_type == "GET":
                print self.connection.get(url=url)

            elif action_type == "PATCH":
                self.connection.patch(url=url, data=data, headers=headers)
        except:
            print "Communication failure on url: "+str(url)
            pass
