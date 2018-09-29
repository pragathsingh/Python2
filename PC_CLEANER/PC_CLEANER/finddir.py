from os import *
from convert import *


class finddir(object):
    """finds the directories and files in a given attribute"""

    def test(self,dirname):
        print  convert_bytes(stat(dirname).st_size)

tmp  = finddir()
tmp.test('G:/TUTORIALS/Udemy - Unreal Engine 4 Mastery - Create Multiplayer Games With Cpp [12.2017]/01 Introduction & Set Up/001 Welcome.mp4')
