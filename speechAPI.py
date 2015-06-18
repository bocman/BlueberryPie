import pygst
import gst
import time
import os
from mutagen.mp3 import MP3
from gtts import gTTS
from requests import ConnectionError
import wolframalpha
from threading import Thread
import time

import settings

class SpeachSynth(object):

    """
    TODO
    """

    google_speech_language = "en"
    google_speech_text_coding = "UTF-8"
    speech_filename = "datoteka.mp3"
    speech_error_text = "Sorry, i have problem with speaking"
    speech_enabled = True
    time_to_wait=0

    def __init__(self):
        pass

    def speak(self, input_text=None):
        """
        Method is in use to generate speech from text, which is given as argument.
        First we initialize audio player, which will play the output. Then we make
        request on Google TTS api, which return the text converted to speech in mp3 file
        Function use functionality of the Google TTS speech.
        :param input_text: Text which should be converted into speech
        """

        player = gst.element_factory_make("playbin", "player")
        player.set_property(
            'uri', "file://" + os.path.abspath(self.speech_filename)
        )
        if not input_text:
            input_text = self.speech_error_text
        try:
            tts = gTTS(
                text=input_text,
                lang=self.google_speech_language
            )
            tts.save(self.speech_filename)
            audio = MP3(self.speech_filename)
            self.time_to_wait = audio.info.length + 0.4
            player.set_state(gst.STATE_PLAYING)

            time.sleep(audio.info.length + 0.2)

            print "time to wait is - " + str(self.time_to_wait)+ " - seconds"

        except ConnectionError:
            print "Can't speak, because connection is down"

class WolframAlphaAPI(object):
    """
    TODO
    """
    NO_ANSWER = "Sorry, I don't have answer to that"
    threads = []
    
    def __init__(self):
        self.client = wolframalpha.Client(settings.WOLFRAM_ALPHA_ID)
        self.threads.append(Thread(target=self.make_question))


    def make_question(self, question_text):
        
        """
        Use WolframAlpha engine to get answer on the question,
        which is obtained as input argument.
        :param question_text: Question, on which we would like to get answer
        :type question_text: String object
        :return: String object
        """
        start_time = time.time()
        make_query = self.client.query(question_text)
        if len(make_query.pods) > 0:
            data = make_query.pods[1]
            if data.text:
                answer = data.text
            else:
                answer = self.NO_ANSWER
        else:
            answer = "Sorry, I can't give you an answer" 
        print time.time() - start_time         
        return answer
