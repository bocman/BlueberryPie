import atexit

from webservice import StrawberryApi


def setDown(self, class_to_close):
    class_to_close.stop()

if __name__ == '__main__':

    webservice = StrawberryApi()

    def __init__(self):
        print "test"

    atexit.register(setDown, webservice)
    # api.update_client()
    # api.test()
