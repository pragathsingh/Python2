from os import *
from convert import *

#It will return a list consist of Parent path at index = 0
#and files or folders path in the later indexes
def MakeList(dirname):
    pnchilds = []        
    pnchilds = [dirname]
    for x in listdir(dirname):                            
        pnchilds.append(dirname + "/" + x)               

    return pnchilds


def IterateThroughList(alldir, dirname,files):
    
    try:
        #If files exits
        if(path.exists(dirname)):        
            #If it is a Directory(folder)
            if(path.isdir(dirname)):            
                #If the directory is not empty then only it will be added to 
                #find further files or folders in it
                if(len(listdir(dirname)) > 0):
                    alldir.append(MakeList(dirname))
            else:
                files.append(dirname)
    except TypeError:
        print('Type Error')
    except WindowsError:
        print("Window Error")
    return alldir,files

def test(dirname):
       
    alldir = []
    files = []
    allinone = {}
    alldir,files = IterateThroughList(alldir, dirname,files)
    for a in alldir:
        for dindex in range(1,len(a)):
            dir = a[dindex]
            alldir,files = IterateThroughList(alldir, dir,files)

    for a in alldir:
        allinone[a[0]] = [a[index] for index in range(1,len(a) )]

    return allinone,files
    print('Done Calculating')

