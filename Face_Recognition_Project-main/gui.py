from tkinter import *
import random
import os


def btn_clicked():
   # print("lol1")
   os.system('cmd /c "attendance.csv')


def btn_clicked1():
    #print("lol2")
    os.system('cmd /c "python attendance.py')



window = Tk()

window.geometry("1268x704")
window.configure(bg = "#02f6e8")
canvas = Canvas(
    window,
    bg = "#02f6e8",
    height = 704,
    width = 1268,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    636.5, 425.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 560, y = 453,
    width = 629,
    height = 125)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 552, y = 308,
    width = 629,
    height = 125)

window.resizable(False, False)
window.mainloop()
