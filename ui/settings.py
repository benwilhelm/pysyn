from Tkinter import *
from appDispatcher import eventDispatcher

def initialize(parent):
    main = Frame(parent, borderwidth=1, width=150, height=600)
    main.place(relx=1, anchor='ne')
    artnetToggle = ArtnetToggle(main)
    main.pack()
    return main




class ArtnetToggle(Checkbutton):
    
    def __init__(self, master):
        self.var = IntVar()
        c = Checkbutton(
            master, text="Enable Artnet In",
            variable=self.var,
            command=self.cb)
        c.pack()

    def cb(self, event=None):
        eventDispatcher.dispatch({
            'type': 'TOGGLE_ARTNET',
            'value' : self.var.get()
        })
