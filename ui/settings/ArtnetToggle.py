from Tkinter import *

class ArtnetToggle(Checkbutton):
    
    def __init__(self, master):
        self.enabled = IntVar()
        btn = Checkbutton(master, text="Enable Artnet In", 
                          variable=self.enabled, command=self.cb)
    
    def cb(self, event):
        if (self.enabled.get()):
            print "Artnet Enabled"
        else:
            print "Artnet Disabled"
            
