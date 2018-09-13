from  tkinter.ttk import *
from tkinter import *

def test():
    print(cb1.get())


options = ['paras','abhi','pragath']
root = Tk()
root.geometry("300x300")
drives = ["C:/","D:/","E:/"]
cb1 = Combobox(root,values=drives,state="readonly")
cb1.grid(row=0,column=1)

bt1 = Button(root,text="Find",command=test)
bt1.grid(row=1,column=1)

#root.geometry("500x500")
#var = StringVar(root)
#var.set(options[0])

#menu = OptionMenu(root,var,*options)
#menu.grid(row=1,column=1)

root.mainloop()



