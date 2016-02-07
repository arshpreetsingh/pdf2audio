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
'''
from jnius import autoclass

# Using Pyjnius for wrapping around Java Classes

Locale = autoclass('java.util.Locale')
PythonActivity = autoclass('org.renpy.android.PythonActivity')

TextToSpeech = autoclass('android.speech.tts.TextToSpeech')

tts = TextToSpeech(PythonActivity.mActivity, None)

# right now only English-US language is supported

tts.setLanguage(Locale.US)

'''

class myPB(ProgressBar):
    def __init__(self, **kwargs):
        super(myPB, self).__init__(**kwargs)
       
        print '\n\n TEST PB CREATED \n\n'

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    progress_bar = ObjectProperty(None)
        

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()


# very important function to display  list of files from file system

    def load(self, path,filename):
   # filename):
        
        for i in read_pdf(filename[0]):
			
            for j in split_pdf(i,2000):
#                tts.synthesizeToFile(j,None,'/sdcard1/backup/test'+i[0]+'.ogg')
                 j==m     
        self.text_input.text = m

        self.dismiss_popup()




            # here we have to create Option by user to choose location to save file         
          
          # may be we need write to system permission?
          
            #

        # Self.text_input.text has the valuse of show the text on the screen 
       
            
        
       # we used POP-up to "load file" now we are destroying it.
        
        


class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    Editor().run()
