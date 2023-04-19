from tkinter import *

class GUI:
    def __init__(self,window):
        self.label1 = Label(window, text = "Charles Babbage", font = ("Arial", 20), background = "cyan")
        self.label1.place(x = "40", y = "30")

window = Tk()
wind = GUI(window)
window.geometry("300x1000")
window.title("Father of Computer")

window.mainloop()
