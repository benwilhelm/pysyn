from Tkinter import *
from appDispatcher import eventDispatcher
import store.settings as settingsStore

def initialize(parent):
    main = Frame(parent, 
        bg='#EEEEEE', borderwidth=1, relief=RIDGE
    )
    pitchLabel = PitchLabel(main)
    pitchLabel.grid(row=0, column=0, padx=1, pady=1, sticky=E+W)
    return main


class PitchLabel(Label):
    def __init__(self, parent):
        self.labelVar = StringVar()
        self.labelVar.set("Random Text")
        Label.__init__(self, parent, textvariable=self.labelVar)
        settingsStore.store.on('change', self.__render)
    
    def __render(self):
        
        artnetEnabled = settingsStore.get_artnet_enabled()
        if (artnetEnabled):
            self.labelVar.set("Artnet Enabled")
        else:
            self.labelVar.set("Artnet Disabled")

    
