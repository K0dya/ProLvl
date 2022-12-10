import tkinter as tk
from PIL import Image
from PIL import ImageTk
import numpy as np
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.ttk import Radiobutton
import cv2


class App(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("App_v0.1")
        self.pack(fill=tk.BOTH, expand=1)

        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        self.label1 = tk.Label(self, border=15)
        self.label2 = tk.Label(self, border=15)
        self.label3 = tk.Label(self, border=15)
        self.label1.grid(row=1, column=1)
        self.label2.grid(row=1, column=2)
        self.label3.grid(row=2, column=1)

        fileMenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=fileMenu)

        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Save", command=self.saveImage)

        basicMenu = tk.Menu(menubar)
        menubar.add_cascade(label="Basic", menu=basicMenu)

        basicMenu.add_command(label="Show plot", command=self.showplot)
        basicMenu.add_command(label="Negative", command=self.onNeg)
        basicMenu.add_command(label="Origin", command=self.onPos)
        basicMenu.add_command(label="Gray", command=self.onGray)

    def setImage(self):
        self.img = Image.open(self.fn)
        self.I = np.asarray(self.img)
        self.frame = cv2.imread(self.fn)
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        l, h = self.img.size
        text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
        self.parent.geometry(text)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image=photo)
        self.label1.image = photo  # keep a reference!

    def onOpen(self):
        ftypes = [('Image Files', '*.tif *.jpg *.png')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        filename = dlg.show()
        self.fn = filename
        self.setImage()

    def saveImage(self):
        self.edge = self.im
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not filename:
            return
        self.edge.save(filename)

    def onNeg(self):
        # Image Negative Menu callback
        self.I2 = 255 - self.I
        self.im = Image.fromarray(np.uint8(self.I2))
        photo_neg = ImageTk.PhotoImage(self.im)
        self.label2.configure(image=photo_neg)
        self.label2.image = photo_neg  # keep a reference!

    def onGray(self):
        img = cv2.cvtColor(self.I, cv2.COLOR_BGR2GRAY)
        self.im = Image.fromarray(np.uint8(img))
        photo_gray = ImageTk.PhotoImage(self.im)
        self.label2.configure(image=photo_gray)
        self.label2.image = photo_gray  # keep a reference!

    def onPos(self):
        # Image Negative Menu callback
        I = self.I
        self.im = Image.fromarray(np.uint8(I))
        photo = ImageTk.PhotoImage(self.im)
        self.label2.configure(image=photo)
        self.label2.image = photo
        self.label1.configure(image=photo)
        self.label1.image = photo

    def showplot(self):
        data2 = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
                 'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
                 }
        df2 = pd.DataFrame(data2)
        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, self.label3)
        line2.get_tk_widget().grid(row=2, column=1)
        # self.label3.configure(image=line2)
        df2 = df2[['year', 'unemployment_rate']].groupby('year').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title('Year Vs. Unemployment Rate')

def main():
    root = tk.Tk()
    App(root)
    root.geometry("640x480")
    root.mainloop()


if __name__ == '__main__':
    main()

