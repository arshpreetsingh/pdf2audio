#!/usr/bin/env python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
# importing Custom Modules

from pdfparsing import read_pdf

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    
    #def erro_popup():
		# we have to create Error_POP up with "Ok" button, when Ok button 
		# will b pressend Error_popup will be dismissed 
		   
    def dismiss_popup(self):
		
        # dismissing the popup created for Load Dialog
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        
        # created the POPUP for load Dialog
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path,filename):
    	
        self.text_input.text = read_pdf(filename[0])
        self.dismiss_popup()

class Parser(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)


if __name__ == '__main__':
    Parser().run()
