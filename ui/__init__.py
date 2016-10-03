from Tkinter import Tk
import settings

def initialize():
    root = Tk()
    root.geometry("800x600+200+100")
    root.settingspane = settings.initialize(root)
    return root
