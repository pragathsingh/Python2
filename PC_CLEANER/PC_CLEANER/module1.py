from __future__ import print_function
import os
import string
from ctypes import windll
from time import *

fileDic = {}
dirDic = {}
notAccessable = []
drives = []
checksize = 0
index = 0

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

if __name__ == '__main__':
    temp = get_drives()
    for a in temp:
        drives.append(a + ':/')

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%0.03f %s " % (num, x)
        num /= 1024.0
        
newdir = {}
info = {}
mainlist = []
checklist = []
filelist = []

def MakeList(dirname):
    global checklist
    global checksize
    global filelist
    tmplist = []
    name = ""
    try:        
       tmplist = [dirname]
       for x in os.listdir(dirname):
           try:
               name = dirname + "/" + x                    
               if  not os.path.isdir(name):
                   if name not in filelist:                       
                       filelist.append(name)
               tmplist.append(name)
           
           except WindowsError:
               notAccessable.append(name)             

    except WindowsError:
        notAccessable.append(name)

    return tmplist

def AddToTotalSpace(size):
    global checksize
    checksize += size    

def CheckInList(name):
    global checklist
    if name in checklist:
        return False
    return True

def AddToData(name):
    global SizeDic
    global checklist 
    global mainlist
    global checksize
    global filelist
    try:
        isdir = os.path.isdir(name)        
        if(isdir):
            if len(os.listdir(name)) != 0:              
                mainlist.append(MakeList(name))
        else:
            if name not in filelist:
                filelist.append(name)
 
    except WindowsError:
        ''

for dr in drives:

    if (os.path.exists(dr)):

        if 'G:/' in dr:
            continue
        if 'C:/' in dr:
            continue
        if 'E:/' in dr:
            continue

        for a in os.listdir(dr):
            name = dr + a
            try:
                if(CheckInList(name)):
                    AddToData(name)
            except WindowsError:
                notAccessable.append(name)
            except KeyError:
                ''
tmpvar = 0
parentindex = 0
childindexstart = 1

     
for item in mainlist:
    #print(item[parentindex])
    for a in range(childindexstart,len(item)):
        AddToData(item[a])
        #print(str(convert_bytes(checksize)),end="\n")
        #print("\b",end="")
        #if os.path.isdir(item[a]):
            #AddToData(item[a])
            # mainlist.append(MakeList(item[a]))
       # else:
          #  checksize += os.stat(item[a]).st_size
          #  checklist = item[a]

print("Data Added Sir....")

try:
    for item in filelist:             
    #if not os.path.isdir(item):
        if(os.path.exists(item)):
            print(name,"   ",convert_bytes(os.stat(item).st_size))
            checksize += os.stat(item).st_size
except WindowsError:
    ''

print(convert_bytes(checksize))
sleep(10)


