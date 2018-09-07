
import os
import string
from ctypes import windll
import time

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

def MakeList(dirname):
    global checklist
    global checksize
    tmplist = []
    name = ""
    try:        
       tmplist = [dirname]
       for x in os.listdir(dirname):
           try:
               name = dirname + "/" + x                    
               if  not os.path.isdir(name):
                   checksize += os.stat(name).st_size
                   checklist.append(name)
                   #print name,convert_bytes(os.stat(name).st_size) 
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
    try:
        isdir = os.path.isdir(name)        
        if(isdir):
            if len(os.listdir(name)) != 0:              
                mainlist.append(MakeList(name))
                #dirDic[name]= size
                #else:
                    #isdir[name] = 0
        else:
            #fileDic[name] = size
            if name not in checklist:
                checklist.append(name)
                checksize += os.stat(name).st_size 
    except WindowsError:
        print 'WindowError'
for dr in drives:

    if (os.path.exists(dr)):

        if 'D:/' in dr:
            continue
        if 'E:/' in dr:
            continue
        if 'C:/' in dr:
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
   # print item[parentindex]
    for a in range(childindexstart,len(item)):
        AddToData(item[a])
        #if os.path.isdir(item[a]):
            #AddToData(item[a])
            # mainlist.append(MakeList(item[a]))
       # else:
          #  checksize += os.stat(item[a]).st_size
          #  checklist = item[a]


#try:
#    for item in mainlist:
#        for a in range(childindexstart,len(item)):            
#            if not os.path.isdir(item[a]):
#               checksize += os.stat(item[a]).st_size
#except WindowsError:
#    ''
    
#for item in mainlist:
#    print item[parentindex],' :- \n'
#    for a in range(childindexstart,len(item)): 
#        print item[a],'  ',convert_bytes(os.stat(item[a]).st_size)

print '\n'*3
print convert_bytes(checksize)

