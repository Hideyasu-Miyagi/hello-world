#!/usr/bin/python3
#
# python3 gui program
#
# 2019-06-26
#
import numpy as np
import tkinter
import sys

root = tkinter.Tk()
frame = tkinter.Frame(root, height=80, width=320)
root.geometry('320x80')
frame.pack()
label = tkinter.Label(frame)
label["text"] = "Hello, world!"
label.pack(side="top")
button_close = tkinter.Button(frame)
button_close["text"] = "Close"
def close_win(_event):
    sys.exit()
button_close.bind('<Button-1>', close_win)
button_close.pack(side="bottom")
frame.mainloop()

