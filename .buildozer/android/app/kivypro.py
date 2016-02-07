#!\usr\bin\env python
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.progressbar import ProgressBar
from kivy.garden import ProgressSpinner
from commands import getoutput
from subprocess import check_output

Builder.load_string('''
<myPB>:
    value: 400
    max: 500
    canvas:
        Rectangle:
            source: "kapy-bg.jpg"
            size: self.size
            pos: self.pos

<CoolWidget>:
    orientation: 'vertical'    
    Button:
        size_hint: 1, .2        
        text: 'top!'
        on_press: root.getTop()
   
    ProgressBar:
        id: pb
        max: 1000
        value: 200
       
   
    Label:
        id: top_label
        font_size: root.width / 50
        #pos_hint: {'x': -.7, 'y': .3}
''')
class myPB(ProgressBar):
    def __init__(self, **kwargs):
        super(myPB, self).__init__(**kwargs)
       
        print '\n\n TEST PB CREATED \n\n'
   
class Coolwidget(BoxLayout):
    def __init__(self, **kwargs):
        super(Coolwidget, self).__init__(**kwargs)
        self.top_label =  self.ids['top_label']        
        self.pb = self.ids['pb']
        self.testpb = myPB
    def getTop(self):
        output = getoutput("top -p 1 -n 1 -b ")
        #output = check_output([])
        self.pb.value = 900        
        print str(output)
        output = str(output) # Convert output so that its usable        
        self.add_widget(self.testpb(value=400))        
        #self.top_label.text = output.split()
       
         
class Coolapp(App):
    def build(self):
        return Coolwidget()
       
if __name__ == '__main__':
    Coolapp().run()
