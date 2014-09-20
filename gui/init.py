from Tkinter import *

class App:

    def __init__(self, master):
        
        master.minsize(width=500, height=500)
        
        frame = Frame(master)
        frame.pack()

        score = Label(master, text="Score: ", anchor=NE)
        score.pack(side=RIGHT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below