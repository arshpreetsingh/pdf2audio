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

tts.setLanguage(Locale.US)

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
        
        for i in read_pdf(filename[0]):
			
            for j in split_pdf(i,2000):
                tts.synthesizeToFile(j,None,'/sdcard0/backup/test'+i[0]+'.ogg')
           
        self.text_input.text = 'done'

        self.dismiss_popup()


class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    Editor().run()
