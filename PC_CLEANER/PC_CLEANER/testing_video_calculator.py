from __future__ import print_function
import os
import string
from ctypes import windll
from threading import Thread 
from tkinter import *
from tkinter.ttk import *
import FindTime


notAccessable = []
drives = []
foldersize = {}
mainlist = []
imagesList = []
videosList = []
newdir = {}
filesize = 0
AllFiles = []
filesSize = []
familyLine = []

videos = 0
images = 0
vidoesize = 0
imagesize = 0
files = 0
folders = 0
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

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

def FamilyTree(parent,size,filename):
    global familyLine
    fmly = parent.split("/")
    propernames = []
    for a in range(0 , len(fmly)):
        name = ""
        if(a != len(fmly)-1):
            for b in range(0,a+1):            
                name += fmly[b] + '/'    
                #rint(name)
            propernames.append(name)
    
    familyLine.append([filename,size,propernames])

def MakeList(dirname,a):
    global checklist,videos,videosList,images,imagesList,imagesize,vidoesize,files,folders    
    tmplist = []
    
    tmplist = [dirname]
    tmplist.append(a)
    for x in os.listdir(dirname):                            
        tmplist.append(dirname + "/" + x)                  

    return tmplist

def AddToData(dirname,name,a):
    
    global videos,videosList,images,imagesList,mainlist,vidoesize,imagesize,files,folders,filesize,notAccessable
    try:
        isdir = os.path.isdir(name)        
        if(isdir):
            folders += 1
            #If the Key is aldearly in newdir then add the size otherwise add the key with the size
            if len(os.listdir(name)) != 0:              
                mainlist.append(MakeList(name,a))  
                if(dirname not in newdir):
                    newdir.update({dirname:0})

            elif(dirname not in newdir):
                newdir.update({dirname:0})

        else:        
            files += 1
            size = os.stat(name).st_size
            filesize += size
            FamilyTree(name,size,a)
           # filesSize.update({dirname:size})
            #If the Key is  in newdir then add the size otherwise add the key with the size
            if(dirname not in newdir):
                newdir.update({dirname:size})
            if(dirname in newdir):
                newdir[dirname] += size

            if(name.endswith(".mp4") or name.endswith(".avi") or name.endswith(".flv") or name.endswith(".mov") or name.endswith(".wmv")):
                videos += 1
                videosList.append(name)
                vidoesize += size               
            
            if(name.endswith(".png") or name.endswith(".jpg") or name.endswith(".jpeg") ):
                images += 1
                imagesList.append(name)
                imagesize += size
    except WindowsError:
        notAccessable.append(name) 
        if(os.path.isdir(name)):
            folders += 1

allisone = {}

def Print():
    global familyLine
    print('Total .mp4 format videos in the pc are '+str(videos),' and there size is '+str(convert_bytes(vidoesize)) )
    print('Total images in the pc are '+str(images),' and there size is '+str(convert_bytes(imagesize)))
    print('Total files are '+str(files)+' and folders are '+str(folders)+' of size '+str(convert_bytes(filesize))+'\n\n')
    print('Files not accessable are : \n')
    count = 1
    for a in notAccessable:
        print(str(count)+'. '+a)
        count += 1  
        
    print('Folders with size : \n\n')
    count = 1
    mycheck = 0

    FolderSize()

    tDur = 0.0
    for a in allisone:
        print(a,' : ',convert_bytes(allisone[a]),'\n')
    #for vid in videosList:
    #    tDur += FindTime.VideoDuration(vid)

    ask = raw_input('find any folder : ')
        
    print('Duration of all videos in minutes is ',int(tDur / 60),'min')

    if( ask in allisone):
        print(convert_bytes(allisone[ask]))
    else:
        print('srry')
    print(convert_bytes(mycheck))



def FolderSize():
    global familyLine
    for a in familyLine:        
        for b in a[2]:
            if(b not in allisone):
                allisone[b] = a[1]
            else:
                allisone[b] += a[1]

def FindFoldersSize():
    
    for fold in newdir:
        dirname = str(fold)        
        parrchild = dirname.split('/')
        parrent = ""
        count = 0
        for a in range(0,len(parrchild)-1):
            if(count==0):
                parrent +=  parrchild[a]
            if(count != 0):
                parrent += ('/' + parrchild[a])
            count += 1
        try:
            newdir[parrent] += newdir[fold]
        except KeyError:
            print('sorry this ' +dirname+' was not founded ')
 


def StartAgain():
    global mainlist,parentindex,childindexstart
  
    for item in mainlist:  
        for a in range(childindexstart,len(item)):
            AddToData(item[parentindex],item[a],item[1])
    FindFoldersSize()
    Print()

def StartCalculating(dr):
    global files,folders

    if(dr == 'All'):

        for n in drives:
            if (os.path.exists(n)):                
                for a in os.listdir(n):            
                    name = n + a
                    try:
                        AddToData(n,name,a)
                    except WindowsError:
                        notAccessable.append(name)
                        if(os.path.isdir(name)):
                            folders += 1
                StartAgain()
    else:       
        if (os.path.exists(dr)):
        
            for a in os.listdir(dr):     
                name = dr + a
                try:
                    AddToData(dr,name,a)
                except WindowsError:
                    notAccessable.append(name) 
                    if(os.path.isdir(name)):
                        folders += 1
            StartAgain()
       

if __name__ == '__main__':
    os.system("@echo off")
    temp = get_drives()
    for a in temp:
        drives.append(a + ':/')

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
    cb1.current(5)
    # link function to change dropdown        
    bt1 = Button(mainframe,text="Find Videos and Images",command=test)
    cb1.grid(row=3,column=1) 
    bt1.grid(row=4,column=1)
    lb1.grid(row=1,column=1) 
    lb2.grid(row=1,column=2)
    root.mainloop()


    



