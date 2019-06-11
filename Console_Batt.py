import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from tkinter import filedialog
from tkinter import *

root = Tk()
pesan = Label(None, text='Plot_Status_Battery_Digi')
pesan.pack()

def openfile():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("BatteryLog","*.blx"),("all files","*.*")))
    values = root.filename
    for val in values.split("/"):
            judul = str(val)

    df = pd.read_csv(root.filename, header=None, sep='\s+')

    df.head()
    x = df[6]
    y = df[7]
    z = df[3]-1    
    fig = plt.figure(figsize=(12,3))
    ax = fig.subplots()
    plt.gcf().canvas.set_window_title('DIGIBIRD BATTERY')
    ax.plot(x,'ro', label = 'A')
    ax.plot(y,'bo', label = 'B')
    ax.set_ylabel('Volt')
    ax.set_title(judul)
    plt.grid(True)
    ax.set_xticks((z))
    ax.set_xticklabels((z+1))
    ax.legend()
    plt.axis([0, 43, 0, 8])
    plt.show()
 
Button(root, text="Open *.blx", command=openfile).pack()

mainloop()
#compile by gama.perkasa@elnusa.co.id



