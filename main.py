import atexit
import socket
import re
from threading import Thread
import pyaudio
import speech_recognition as sr

import settings
from webservice import StrawberryAPI
from speechAPI import SpeachSynth, WolframAlphaAPI


def initialize_threads(self, thread_list):
    pass
    thread_list.append(Thread(target=self.update_client))

def setDown(self, class_name):
    class_name.stop()


def speech_actions(source):
    question = WolframAlphaAPI()
    audio = speech_recognizer.listen(source)
    audio_text = speech_recognizer.recognize(audio)

    answer = question.make_question(audio_text)
    speech.speak(answer)
    #speech_recognizer.pause_threshold = speech.time_to_wait

if __name__ == '__main__':
    
    webservice = StrawberryAPI()
    #speech = SpeachSynth()
    
    print "sem naprej v sistemu"
    #speech_recognizer = sr.Recognizer()
    #speech_recognizer.energy_threshold = 3000
    threads = []

    def __init__(self):
        pass
        # webservice.get_client()
        # webservice.update_client()        
        initialize_threads(threads)

    #with sr.Microphone() as source:
     #   while True:
      #      speech_actions(source)
    
    #speech.speak("Thats what she said")

    #atexit.register(setDown, webservice)
