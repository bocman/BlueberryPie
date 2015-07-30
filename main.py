#!/usr/bin/python

import atexit
import socket
import time
import re
from threading import Thread
import pyaudio
import speech_recognition as sr

import settings
from webservice import StrawberryAPI
from speechAPI import SpeachSynth, WolframAlphaAPI
if settings.CLIENT_TYPE == "raspberry":
    from gpioAPI import RaspberryGPIO


def initialize_threads(self, thread_list):
    pass
    thread_list.append(Thread(target=self.update_client))


def setDown(self, class_name):
    class_name.stop()


def speech_actions(recognizer, audio):
    question = WolframAlphaAPI()
    if settings.CLIENT_TYPE == "raspberry":
        raspberry_gpio = RaspberryGPIO()

    def compare_second_word(text, searched_word):
        split_text = text.split()
        order_text = "{0} {1}".format(split_text[1], split_text[2])
        if order_text == searched_word:
            return True
        return False

    def __play_song(audio_text):
        re_expression = re.match(r'.* play song (?P<song_name>.*).*', audio_text, re.M | re.I)
        song_name = re_expression.group('song_name')
        print "-->" + song_name

    def __update_client():
        print "sem updateal client"

    try:
        audio_text = recognizer.recognize(audio).lower()
        print audio_text
        print "-----------------------------------------------------------------------"
        print "-----------------------------------------------------------------------"

        if audio_text.startswith(settings.CLIENT_NAME.lower()):
            if compare_second_word(audio_text, "play song"):
                __play_song(audio_text)

            if compare_second_word(audio_text, "update client"):
                __update_client()

            if settings.CLIENT_TYPE == "raspberry":
                if compare_second_word(audio_text, "activate green light"):
                    print "sem notri"
                    raspberry_gpio.activate(7)

                if compare_second_word(audio_text, "deactivate green light"):
                    print "sem notri"
                    raspberry_gpio.deactivate(7)

                if compare_second_word(audio_text, "activate red light"):
                    print "sem notri"
                    raspberry_gpio.activate(7)

                if compare_second_word(audio_text, "deactivate red light"):
                    print "sem notri"
                    raspberry_gpio.deactivate(7)

                if compare_second_word(audio_text, "activate yellow light"):
                    print "sem notri"
                    raspberry_gpio.activate(7)

                if compare_second_word(audio_text, "deactivate yellow light"):
                    print "sem notri"
                    raspberry_gpio.deactivate(7)


        # answer = question.make_question(audio_text)
        # print "malina: Answer is- "+str(audio_text)

        print "-----------------------------------------------------------------------"
        print "-----------------------------------------------------------------------"
        # speech.speak(answer)

    except LookupError:
        print("malina: Oops! Didn't catch that")

if __name__ == '__main__':
    threads = []
    webservice = StrawberryAPI()
    speech = SpeachSynth()

    print "malina: I'm ready"

    def __init__(self):
        webservice.update_client()
        initialize_threads(threads)
        # webservice.get_client()
        # webservice.update_client()


    r = sr.Recognizer()
    r. energy_threshold = 2000
    r.listen_in_background(sr.Microphone(), speech_actions)

    atexit.register(setDown, webservice)
