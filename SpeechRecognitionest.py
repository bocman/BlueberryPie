#!/usr/bin/env python


import pyaudio
import os
import speech_recognition as SpeachRecognizer
import speech_recognition as sr


def excel():
    os.system("start excel.exe")


def internet():
    os.system("start chrome.exe")


def media():
    os.system("start wmplayer.exe")


def mainfunction(source):
    print "sem v metodi"
    audio = r.listen(source)
    user = r.recognize(audio)
    print(user)
    if user == "Excel":
        excel()
    elif user == "Internet":
        internet()
    elif user == "music":
        media()
    else:
        print "not found"

if __name__ == "__main__":
    r = sr.Recognizer()
    r.energy_threshold = 3000
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
