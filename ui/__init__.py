from Tkinter import *
import settings, effectspane

root = Tk()
__initialized = False

Grid.columnconfigure(root, 0, weight=3, minsize=450)
Grid.columnconfigure(root, 1, weight=1, minsize=150)

def initialize():
    global __initialized
    assert (__initialized == False), "UI already initialized"

    root.effectspane = effectspane.initialize(root)
    root.effectspane.grid(row=0, column=0, padx=2, pady=2, sticky=N+E+W)
    
    root.settingspane = settings.initialize(root)
    root.settingspane.grid(row=0, column=1, padx=2, pady=2, sticky=EW)
    
    __initialized = True
    return root
