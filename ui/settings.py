from Tkinter import *
from appDispatcher import eventDispatcher

def initialize(parent):
    main = Frame(parent, borderwidth=1, relief=SUNKEN)
    Grid.columnconfigure(main, 0, weight=1)
    artnetToggle = ArtnetToggle(main)
    artnetToggle.grid(row=0, column=0, sticky=W)
    return main


class ArtnetToggle(Checkbutton):
    
    def __init__(self, master):
        self.var = IntVar()
        Checkbutton.__init__(self, 
            master, text="Enable Artnet In",
            variable=self.var,
            command=self.cb, 
            justify=LEFT
        )

    def cb(self, event=None):
        eventDispatcher.dispatch({
            'type': 'TOGGLE_ARTNET',
            'value' : self.var.get()
        })
