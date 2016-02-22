#!/usr/bin/env python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os
from kivy.uix.progressbar import ProgressBar

# importing Custom Modules

from pdfparsing import read_pdf
from pdfparsing import split_pdf

from jnius import autoclass

# Using Pyjnius for wrapping around Java Classes

Locale = autoclass('java.util.Locale')

PythonActivity = autoclass('org.renpy.android.PythonActivity')

TextToSpeech = autoclass('android.speech.tts.TextToSpeech')

tts = TextToSpeech(PythonActivity.mActivity, None)

# right now only English-US language is supported

#tts.setLanguage(Locale.US)

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
        

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path,filename):
        
        j = """JUST WHAT should a young man or woman know in order to be "in
the know"? Is there, in other words, some inside information, some
special taboo, some real lowdown on life and existence that most
parents and teachers either don't know or won't tell?
In Japan it was once customary to give young people about to be
married a "pillow book." This was a small volume of wood-block prints,
often colored, showing all the details of sexual intercourse. It wasn't just
that, as the Chinese say, "one picture is worth ten thousand words." It
was also that it spared parents the embarrassment of explaining these
intimate matters face-to-face. But today in the West you can get such
information at any newsstand. Sex is no longer a serious taboo.
Teenagers sometimes know more about it than adults.
But if sex is no longer the big taboo, what is? For there is always
something taboo, something repressed, unadmitted, or just glimpsed
quickly out of the corner of one's eye because a direct look is too
unsettling. Taboos lie within taboos, like the skins of an onion. What,
then, would be The Book which fathers might slip to their sons and"""

        tts.synthesizeToFile(j,None,'ok.ogg')
           
        self.text_input.text = 'done'

        self.dismiss_popup()


class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)


if __name__ == '__main__':
    Editor().run()
