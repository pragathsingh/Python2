
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
vidoesize = 0
imagesize = 0
foldersize = []

tmpvar = 0
parentindex = 0
childindexstart = 2


skiplist = ["Autodesk","Local","Anaconda2","Windows","Microsoft","ProgramData"
                ,"Program Files","Program Files (x86)","Epic Games","AppData","GAMES"
                ,"Setups","UNREAL","UNREAL","UNREAL","UNREAL","Installed Games"]

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%0.03f %s " % (num, x)
        num /= 1024.0


def MakeList(dirname,a):
    global checklist
    global videos
    global videosList
    global images
    global imagesList
    global imagesize
    global vidoesize
    
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
                           #foldersize.append([a,os.stat(name).st_size])
                           videosList.append(a)
                           videos +=1
                           vidoesize += os.stat(name).st_size
                   if name not in imagesList:
                       if(name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg") ):
                          # foldersize.append([a,os.stat(name).st_size])
                           images += 1
                           imagesList.append(a)
                           imagesize += os.stat(name).st_size
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
    global vidoesize
    global imagesize
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
                        #foldersize.[a,os.stat(name).st_size])
                        videos += 1
                        vidoesize += os.stat(name).st_size
                        videosList.append(a)
                        
                if name not in imagesList:
                    if(name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg") ):
                        #foldersize.append([a,os.stat(name).st_size])
                        imagesize += os.stat(name).st_size
                        print(a,convert_bytes(os.stat(name).st_size))
                        images += 1
                        imagesList.append(a)
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


def IsInSkipList(name):
    global skiplist
    for skip in skiplist:
        if name == skip:
            return True
    return False


def StartAgain():
    global mainlist
    global parentindex
    global childindexstart
    for item in mainlist:          
        if(IsInSkipList(item[1])):
            continue
        print(item[parentindex])
        for a in range(childindexstart,len(item)):
            if(IsInSkipList(item[a])):        
                continue
            AddToData(item[a],item[1])



def StartCalculating(dr):
    if(dr == 'All'):
        for n in drives:
            print(n)
            if (os.path.exists(n)):
                print(n)
                for a in os.listdir(n):            
                    #lb2.config(text=videos)
                    name = n + a
                    try:
                        if(CheckInList(name)):
                            AddToData(name,a)
                    except WindowsError:
                        notAccessable.append(name)
                    except KeyError:
                        ''
            StartAgain()
    else:       
        print(dr)
        if (os.path.exists(dr)):
            print(dr)
            for a in os.listdir(dr):            
                #lb2.config(text=videos)
                name = dr + a
                try:
                    if(CheckInList(name)):
                        AddToData(name,a)
                except WindowsError:
                    notAccessable.append(name)
                except KeyError:
                    ''
            StartAgain()
       

if __name__ == '__main__':
    temp = get_drives()
    for a in temp:
        drives.append(a + ':/')


    d = ""
    root = Tk()
    root.title("Tk dropdown example")
     
    
    # Add a grid
    mainframe = Frame(root)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)

    SingleDrive = True
    # on change dropdown value
    def test():        
        StartCalculating(cb1.get())
    
    lb1 = Label(mainframe,text="Videos : ")
    lb2 = Label(mainframe,text="")
    ComboBoxValues = []
    ComboBoxValues.append('All')
    for a in drives:
        ComboBoxValues.append(a)

    cb1 = Combobox(mainframe,values=ComboBoxValues,state="readonly")
    cb1.current(0)
    # link function to change dropdown        
    bt1 = Button(mainframe,text="Find Videos and Images",command=test)
    cb1.grid(row=3,column=1) 
    bt1.grid(row=4,column=1)
    lb1.grid(row=1,column=1) 
    lb2.grid(row=1,column=2)
    root.mainloop()
    
def AddToTotalSpace(size):
    global checksize
    checksize += size    

def PrintIt():
    global videosList
    for a in videosList:print(a)
    print('Total .mp4 format videos in the pc are '+str(videos))



def FolderSize():
    global mainlist
    global foldersize

    for a in mainlist:
        dir = a[0]
        name = a[1]


for a in videosList:print(a)
for a in imagesList:print(a)
print('Total .mp4 format videos in the pc are '+str(videos),' and there size is'+str(convert_bytes(vidoesize)) )
print('Total images in the pc are '+str(images),' and there size is'+str(convert_bytes(imagesize)))


