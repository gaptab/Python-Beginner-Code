from tkinter import *
from time import strftime
root=Tk()
root.title("Digital Clock")
def clock():
    tick=strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000,clock)

label=Label(root,font=("segoe",60),foreground='yellow',background='black')

label.pack(anchor='center')
clock()
mainloop()