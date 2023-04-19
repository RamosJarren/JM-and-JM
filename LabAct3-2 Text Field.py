from tkinter import *

class GUI:
    def __init__(self,window):
        self.txtfld1 = Entry(window, border = "2", width = "24")
        self.txtfld1.place(x = "80", y = "20", height = "40")
        self.txtfld1.insert(0, "This is where I type my text")



window = Tk()
wind = GUI(window)
window.geometry("300x100")
window.title("Text Field")

window.mainloop()
