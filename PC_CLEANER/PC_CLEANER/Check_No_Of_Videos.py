from __future__ import print_function
import os
import string
from ctypes import windll
from threading import Thread 
from tkinter import *
from tkinter.ttk import *


notAccessable = []
drives = []
index = 0
newdir = {}
info = {}
mainlist = []
checklist = []
videosList = []
imagesList = []
videos = 0
images = 0


tmpvar = 0
parentindex = 0
childindexstart = 2


skiplist = ["Autodesk","Local","Anaconda2","Windows","Microsoft","ProgramData"
                ,"Program Files","Program Files (x86)","Epic Games","AppData","GAMES"
                ,"Setups","UNREAL","UNREAL","UNREAL","UNREAL","Installed Games"]


def MakeList(dirname,a):
    global checklist
    global videos
    global videosList
    global images
    global imagesList

    tmplist = []
    name = ""
    try:        
       tmplist = [dirname]
       tmplist.append(a)
       for x in os.listdir(dirname):
           try:
               name = dirname + "/" + x                    
               if  not os.path.isdir(name):
                   if x not in videosList:
                       if(name.endswith(".mp4") or name.endswith(".avi") or name.endswith(".flv") or name.endswith(".mov") or name.endswith(".wmv")):
                           checklist.append(name)
                           videosList.append(x)
                           videos +=1
                   if name not in imagesList:
                       if(name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg") ):
                           images += 1
                           imagesList.append(name)
                   #print name,convert_bytes(os.stat(name).st_size) 
               tmplist.append(name)
           
           except WindowsError:
               notAccessable.append(name)             

    except WindowsError:
        notAccessable.append(name)

    return tmplist


def AddToData(name,a):
    global videos
    global videosList
    global images
    global imagesList
    global SizeDic
    global checklist 
    global mainlist
    global checksize
    try:
        isdir = os.path.isdir(name)        
        if(isdir):
            if len(os.listdir(name)) != 0:              
                mainlist.append(MakeList(name,a))  
        else:
            if name not in checklist:
                checklist.append(name)
                if name not in videosList:
                    if(name.endswith(".mp4") or name.endswith(".avi") or name.endswith(".flv") or name.endswith(".mov") or name.endswith(".wmv")):
                        videos += 1
                        videosList.append(name)
                if name not in imagesList:
                    if(name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg") ):
                        images += 1
                        imagesList.append(name)
    except WindowsError:
        ''

def CheckInList(name):
    global checklist
    if name in checklist:
        return False
    return True

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

def StartAgain():
    for item in mainlist:
    #print(item[parentindex])
        for a in range(childindexstart,len(item)):
            AddToData(item[a])

def StartCalculating(dr):
    if (os.path.exists(dr)):
        for a in os.listdir(dr):
            name = dr + a
            try:
                if(CheckInList(name)):
                    AddToData(name)

            except WindowsError:
                notAccessable.append(name)
            except KeyError:
                ''
        StartAgain()
def Yo(m):
    print(m)
 
if __name__ == '__main__':
    m = 0
    temp = get_drives()
    for a in temp:
        drives.append(a + ':/')

    root = Tk()
    root.geometry("300x300")

    bt1 = Button(root,text=drives[m])
    m += 1
    bt2 = Button(root,text=drives[m])
    m += 1
    bt3 = Button(root,text=drives[m])
    m += 1
    bt4 = Button(root,text=drives[m])
    m += 1
    bt5 = Button(root,text=drives[m])

    #,command=StartCalculating(drives[m])
    
    #,command=StartCalculating(drives[m])
    
    #,command=StartCalculating(drives[m])
    
    #,command=StartCalculating(drives[m])
    
    #,command=StartCalculating(drives[m])

    bt1.grid(row=0,column=0,command=Yo(drives[m]))
    bt2.grid(row=0,column=1)
    bt3.grid(row=0,column=2)
    bt4.grid(row=0,column=3)
    bt5.grid(row=0,column=4)

    root.mainloop()
        



def AddToTotalSpace(size):
    global checksize
    checksize += size    

def PrintIt():
    global videosList
    for a in videosList:print(a)
    print('Total .mp4 format videos in the pc are '+str(videos))


def IsInSkipList(name):
    global skiplist
    for skip in skiplist:
        if name == skip:
            return True
    return False

for dr in drives:
       
    #if 'D:/' in dr:
    #    continue
    #if 'C:/' in dr:
    #    continue
    #if 'E:/' in dr:
    #    continue  
    #if 'J:/' in dr:
    #    continue

    if (os.path.exists(dr)):
        for a in os.listdir(dr):
            
            if(IsInSkipList(a)):
                continue
            name = dr + a

            try:
                if(CheckInList(name)):
                    AddToData(name,a)

            except WindowsError:
                notAccessable.append(name)
            except KeyError:
                ''

    


for item in mainlist:          
    if(IsInSkipList(item[1])):
        continue
    print(item[parentindex])
    for a in range(childindexstart,len(item)):
        if(IsInSkipList(item[a])):        
            continue
        AddToData(item[a])

for a in videosList:print(a)
print('Total .mp4 format videos in the pc are '+str(videos))


