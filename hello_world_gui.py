#!/usr/bin/python3
#
# python3 gui program
#
# 2019-06-26
#
import numpy as np
import tkinter

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()
label = tkinter.Label(frame)
label["text"] = "Hello, world!"
label.pack(side="top")
frame.mainloop()

