#import pygame
#import os
from tkinter import *
from tkinter import Tk,END,filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


root = Tk()
pesan = Label(None, text='Connectivity_Plot')
pesan.pack()

def openfile():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Connecivity","*.txt"),("all files","*.*")))
    values = root.filename
    for val in values.split("/"):
        judul = str(val)
    with open(root.filename) as fp:
        data = [list(map(float, line.strip().split(' '))) for line in fp]
        y = np.transpose(data)
        a = np.arange(1, 3585, 1)
        x = np.transpose(a)
        
    fig = plt.figure(figsize=(12,5))
    ax = fig.subplots()
    ax.plot(x,y,'k')
    ax.axis([0, 3600, -100, 100])
    plt.xlabel('SS trace')
    plt.ylabel('spec %')
    plt.title(judul)
    plt.grid(True)
    plt.show()

Button(root, text="Open CO *.txt", command=openfile).pack()

mainloop()

#compile by gama.perkasa@elnusa.co.id

