from tkinter import *

class GUI:
    def __init__(self,window):
        self.button1 = Button(window, text = "Color", background = "#0000ff", activebackground = "#ffff00", foreground = "#ff0000", activeforeground = "#ff0000")
        self.button1.place(x = "30", y = "70")
        self.button2 = Button(window, text="<---Click to change the color of the button")
        self.button2.place(x="70", y="70")

window = Tk()
wind = GUI(window)
window.geometry("360x120")
window.title("Button")

window.mainloop()
