import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror
from tkinter import filedialog
import DataManagement as dm

OTHERS = ['other', 'refused', 'dont know', "don't know", 'unsure', 'no difference', 'ref', 'neutral', 'no diff.', 'neutral']
NORSZR = ['', ';NOR SZR']
INDENT = ['', '&AI2 ']

def updateGui(frame):
    return 0

def destroyFrame(frame):
    frame.destroy()

def buildGui(frame):
    upload_button = tk.Button(frame, text="Upload Layout", anchor="w", command=lambda: dm.getFilePath()).grid(row=0, column=0, sticky='w')
    print(upload_button)
    return 0


root = tk.Tk()
info_frame = tk.Frame(root, width=1280, height=720, highlightbackground='black', highlightthickness='1')
info_frame.pack(side='left', anchor='n')
buildGui(info_frame)
root.mainloop()
