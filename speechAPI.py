import settings
import pygst
import gst
import time
import os
from mutagen.mp3 import MP3
from gtts import gTTS


class SpeachSynth(object):

    """
    """

    google_speech_link = "http://translate.google.com/translate_tts?ie=UTF-8&tl=en&q="
    google_speech_language = "en"
    google_speech_text_coding = "ie=" + "UTF-8"
    speech_filename = "datoteka.mp3"
    speech_error_text = "Sorry, i have problem with speaking"

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

        tts = gTTS(
            text=input_text,
            lang=self.google_speech_language
        )
        tts.save(self.speech_filename)
        player.set_state(gst.STATE_PLAYING)
        audio = MP3(self.speech_filename)

        time.sleep(audio.info.length + 0.2)
