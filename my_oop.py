import tkinter as tk
from PIL import Image, ImageTk
import cv2


class App:
    def __init__(self, source, n):
        self.source = source
        self.n = n

    def call_video(self):
        # self.capimg = self.cap.copy()
        # self.frame = cv2.imread("Abc.jpg")
        self.cap = cv2.VideoCapture(self.source)
        # self.cap.set(3, 480)
        # self.cap.set(4, 270)
        self.cap.set(cv2.CAP_PROP_FPS, 100)
        ret, self.frame = self.cap.read()
        self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.resized = cv2.resize(self.frame, (480, 270), interpolation = cv2.INTER_AREA)
        self.img = Image.fromarray(self.resized)
        # self.img = self.img.resize((100,100))
        imgTk = ImageTk.PhotoImage(image=self.img)
        self.label.imgTk = imgTk
        self.label.configure(image = imgTk)
        self.label.after(10, self.call_video)
        # cv2.imshow("frame", self.frame)
        # cv2.waitKey(0)

    def call_window(self):
        self.label = tk.Label(self.window, relief=tk.RAISED)
        self.label.pack(side= tk.LEFT)
        self.call_video()
        # self.window.mainloop()

    def multi(self):
        self.window = tk.Tk()
        self.window.geometry("650x450")
        for i in range(self.n):
            self.call_window()
        self.window.mainloop()



# app = App(0) 1
# app.call_window()
