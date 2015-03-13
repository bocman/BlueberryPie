import atexit

# from webservice import StrawberryApi
from speechAPI import SpeachSynth


def setDown(self, class_to_close):
    class_to_close.stop()

if __name__ == '__main__':

    speech = SpeachSynth()
    speech.speak()
    # def __init__(self):
    #    print "test"
    # print "sem ja"
    # webservice = StrawberryAPI()
    # webservice.get_client()
    # print "vseeno naprej"

    # atexit.register(setDown, webservice)
    # api.update_client()
    # api.test()
