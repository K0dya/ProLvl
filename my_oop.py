import tkinter as tk
from PIL import Image, ImageTk
import cv2


class App:
    def __init__(self, source, n):
        self.source = source
        self.n = n
        self.cap = cv2.VideoCapture(self.source)
        self.delay = 20

    def call_video(self):
        ret, self.frame = self.cap.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.img = Image.fromarray(self.frame)
        imgTk = ImageTk.PhotoImage(image=self.img)
        self.label.imgTk = imgTk
        self.label.configure(image = imgTk)
        self.label.after(self.delay, self.call_video)
        # cv2.imshow("frame", self.frame)
        # cv2.waitKey(0)

    def call_window(self):
        self.window = tk.Tk()
        self.window.geometry("650x450")
        self.label = tk.Label(self.window)
        self.label.grid(row=0, column=0)
        self.call_video()
        # self.window.mainloop()

    def multi(self):
        for i in range(self.n):
            self.call_window()
        self.window.mainloop()



# app = App(0) 1
# app.call_window()
