from tkinter import *

class GUI:
    def __init__(self,window):
        self.label1 = Label(window, text = "Laboratory Activity 3")
        self.label1.place(x = "40", y = "30")
        self.label2 = Label(window, text="Submitted to: Mam Sayo")
        self.label2.place(x="30", y="50")

window = Tk()
wind = GUI(window)
window.geometry("230x80")
window.title("Label")

window.mainloop()