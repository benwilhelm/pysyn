from Tkinter import Tk, Frame, BOTH
import ArtnetToggle

def initialize(parent):
    main = Frame(parent, bg="gray", width=200, height=200)
    toggle = ArtnetToggle.ArtnetToggle(main)
    main.pack()
    return main
