from finddir import *
import convert
from folderssize import *

directories,files = test("G:")
folders = FindFolderSize(files)

for a in folders:
    print(a + "    "+convert_bytes(folders[a]) + "\n")
