import tkinter as tk
from PIL import Image, ImageTk
import cv2

window = tk.Tk()
window.geometry("600x400")
label = tk.Label(window)
label.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frames():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgTk = ImageTk.PhotoImage(image=img)
    label.imgTk = imgTk
    label.configure(image=imgTk)
    label.after(20, show_frames)
show_frames()

window.mainloop()
#1





