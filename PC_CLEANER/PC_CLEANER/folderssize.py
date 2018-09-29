def FamilyTree(parent):
    
    propernames = []
    fmly = parent.split("/")
    for a in range(0 , len(fmly)):
        name = ""
        if(a != len(fmly)-1):
            for b in range(0,a+1):            
                name += fmly[b] + '/'                    
            propernames.append(name)
    return (propernames)

def FindFolderSize(files):
    from os import stat
    folders = {}
    tempdic = {}
    foldersizelist = []
    for f in files:
        size = stat(f).st_size
        tempdic[f] = ([size ,FamilyTree(parent = f)])
    
    for values in tempdic.values():
        it = values[1]
        for dir in it:
            if(dir not in folders):
                folders[dir] = values[0]
            else:
                folders[dir] += values[0]

    return folders


