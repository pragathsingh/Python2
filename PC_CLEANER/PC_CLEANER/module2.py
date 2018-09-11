from __future__ import print_function
import os
import string
from pymediainfo import MediaInfo
from ctypes import windll
import time
import subprocess
import json

drives = []
def Find(filename):
    media_info = MediaInfo.parse(filename)
    #duration in milliseconds
    print('finding')
    print(duration_in_ms = media_info.tracks[0].duration)

def final(name):
    from subprocess import check_output
    
    file_name = name
    
    #For Windows
    a = str(check_output('ffprobe -i  "'+file_name+'" 2>&1 |findstr "Duration"',shell=True)) 
    
    #For Linux
    #a = str(check_output('ffprobe -i  "'+file_name+'" 2>&1 |grep "Duration"',shell=True)) 
    
    a = a.split(",")[0].split("Duration:")[1].strip()
    
    h, m, s = a.split(':')
    duration = int(h) * 3600 + int(m) * 60 + float(s)
    
    print(duration)
    return duration

#a, check_output, duration, file_name = final()


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
        location = raw_input('enter the location')
        dirs = os.listdir(location)
        for a in dirs:
            print(a)
            if not os.path.isdir(a):
                if(a.endswith('.mp4')):
                    #name = 'G:/TUTORIALS/[FreeTutorials.Us] unrealcourse/05-testing-grounds-fps/'+a
                    print (name)
                    #print(Find(name))
                    #print(os.stat('G:/TUTORIALS/[FreeTutorials.Us] unrealcourse/05-testing-grounds-fps/'+a))
   
    except WindowsError:
        ''

def probe(vid_file_path):
    ''' Give a json from ffprobe command line

    @vid_file_path : The absolute (full) path of the video file, string.
    '''
    if type(vid_file_path) != str:
        raise Exception('Gvie ffprobe a full file path of the video')
        return

    command = ["ffprobe",
            "-loglevel",  "quiet",
            "-print_format", "json",
             "-show_format",
             "-show_streams",
             vid_file_path
             ]

    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)
    out, err = pipe.communicate()
    return json.loads(out)


def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]

