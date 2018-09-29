from __future__ import print_function
import os
import string
from ctypes import windll
import FindTime
from convert import * 

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
mhr = {'min':60,'hr':60,'day':24,'week':7,'month':12,'year':9}

skiplist = ["Autodesk","Local","Anaconda2","Windows","Microsoft","ProgramData"
                ,"Program Files","Program Files (x86)","Epic Games","AppData","GAMES"
                ,"Setups","UNREAL","Installed Games"]

def MinHourDay(time):
    smh = [60,60,24,7,4,12]
    count = 0
    for a in smh:
        if(time / a == 0):
            return 
        else:
            return

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

        else:        
            files += 1
            size = os.stat(name).st_size
            #If the Key is  in newdir then add the size otherwise add the key with the size
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

    tDur = 0.0
    try:
        for vid in videosList:
            duration = FindTime.VideoDuration(vid)
            print(vid+ "   Time : "  + str(int(duration/60)))
            tDur += duration
    except ZeroDivisionError:
        ''
    print('Duration of all videos in minutes is ',int(tDur / 86400),'days')

def StartAgain():
    global mainlist,parentindex,childindexstart
  
    for item in mainlist:  
        for a in range(childindexstart,len(item)):
            AddToData(item[parentindex],item[a],item[1])
   # FindFoldersSize()
    Print()

def StartCalculating(dr):
    global files,folders

    if (os.path.exists(dr)):    
        for a in os.listdir(dr):   
            name = dr +"/"+ a
            try:
                AddToData(dr,name,a)
            except WindowsError:
                notAccessable.append(name) 
                if(os.path.isdir(name)):
                    folders += 1
        StartAgain()
       

if __name__ == '__main__':
   
    dir =raw_input('enter the location :')
    StartCalculating(dir)
        



