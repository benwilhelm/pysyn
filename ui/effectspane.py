from Tkinter import *
from appDispatcher import eventDispatcher
import store.settings as settingsStore

def initialize(parent):
    main = Frame(parent)
    Grid.columnconfigure(main, 0, weight=1)
    # Grid.columnconfigure(main, 0, weight=1)
    
    for i in range(3):
        ep = EffectsProcessor(main)
        ep.grid(column=0, padx=2, pady=4, ipadx=15, ipady=15, sticky=E+W)
    return main



class EffectsProcessor(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent, borderwidth=2,  relief=GROOVE)
        
        self.__enabled = IntVar()
        self.enableButton = Checkbutton(self, variable=self.__enabled)
        self.enableButton.grid(row=0, column=0)
        
        self.label = Entry(self)
        self.label.grid(row=0, column=1, sticky=E+W)
        
        self.sliderFrame = Frame(self)
        self.sliderFrame.grid(row=1, column=2)
        
        self.multiplier = Scale(self.sliderFrame, from_=100, to=-100)
        self.multiplier.grid(row=0, column=1)
        
        self.offset = Scale(self.sliderFrame, from_=100, to=-100)
        self.offset.grid(row=0, column=2)

        self.inertia = Scale(self.sliderFrame, from_=100, to=0)
        self.inertia.grid(row=0, column=3)
        
        self.__pitchtext = StringVar()
        self.pitchLabel = Label(self, text="hllo?", textvariable=self.__pitchtext)
        self.pitchLabel.grid(row=1, column=1, sticky=NW)

        Grid.columnconfigure(self, 1, weight=1)
    
        
