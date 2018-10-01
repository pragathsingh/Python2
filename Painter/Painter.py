from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
import win32api
from threading import Thread
import tkinter.messagebox

class Paint():

    def __init__(self):
        self.WIDTH, self.HEIGHT = 1400, 900
        self.LimitX, self.LimitY = 22, 22
        self.verification = False
        self.state_left = win32api.GetKeyState(0x01)
        self.mouseposx, self.mouseposy = win32api.GetCursorPos()

        self.window = Tk()
        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg="#000000")
        self.canvas.pack()
        self.img = PhotoImage(width=self.WIDTH, height=self.HEIGHT)
        self.canvas.create_image((self.WIDTH, self.HEIGHT), image=self.img, state="normal")


        self.mouseposthread = Thread(target=self.MousePosChange)
        self.mouseposthread.start()
        self.window.mainloop()

    def MousePosChange(self):
        while True:
            self.mouseposx, self.mouseposy = win32api.GetCursorPos()
            a = win32api.GetKeyState(0x01)
            if (a != self.state_left):
                print('pressed')
                count = 0
                #for a in range(0,5):
                 #   count += 1
                self.img.put("#ffffff", (self.mouseposx+count, self.mouseposy+count))
                #self.verification = True
                self.state_left = a

            if(a <= -127 ):
                self.img.put("#ffffff", (self.mouseposx, self.mouseposy))

paint = Paint()
