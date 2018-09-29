from tkinter import *
from tkinter.ttk import *
from testing_scirpt import *
import operator

root = Tk()
frame = Frame(root)
frame.grid(row = 0 ,column = 0)
root.geometry("600x700")
tree = Treeview(frame,columns = ("dir","size"))
tree.heading('dir',text = 'Directory')
tree.heading('size',text = 'Size of Diretory')

tree["show"] = "headings"
#tree.grid(row= 0 , column = 1)
count = 0

sortedic = {}
sorted_d = sorted(folders.items(), key=operator.itemgetter(1),reverse=True)
print type(sorted_d)

for list in sorted_d:
    tree.insert('','end',values =(list[0],convert_bytes(list[1])) )
    count += 1
ysb = Scrollbar(orient='vertical', command=tree.yview)
tree.grid(row=0, column=0, sticky='nsew')
ysb.grid(row=0, column=1, sticky='ns')
tree.configure(yscroll=ysb.set) 
root.mainloop()

