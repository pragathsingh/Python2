from __future__ import print_function
import os
import string
from ctypes import windll
import time

drives = []


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%0.03f %s " % (num, x)
        num /= 1024.0

if __name__ == '__main__':
    temp = get_drives()
    for a in temp:
        drives.append(a + ':/')
    try:
        for a in drives:
            print(convert_bytes(os.stat(a).st_size))
    except WindowsError:
        ''



