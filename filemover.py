"""Python program to move file from one folder to another folder.
@author : CodePerfectPLus
@language : Python 3
Website : http://codeperfectplus.herokuapp.com/
Github : https://github.com/codePerfectPlus
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  

"""
import os
from os import path
from shutil import move

paths = [
    "Programing File",
    "Compressed",
    "Application","""Python program to move file from one folder to another folder.
@author : CodePerfectPLus
@language : Python 3
Website : http://codeperfectplus.herokuapp.com/
Github : https://github.com/codePerfectPlus
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  

"""
import os
from os import path
from shutil import move

paths = [
    "Programming File",
    "Compressed",
    "Application",
    "Picture",
    "Video",
    "Documents",
    "Music",    
    "Torrents"
]
for root in paths:
    try:
        os.mkdir(root)
    except OSError:
        print("Folder Already Exists")

pic = [".jpeg", ".jpg", ".png", ".gif", ".tiff", ".raw", ".webp", ".jfif", ".ico", ".psd", ".svg", ".ai"]
pytho = [".ipynb", ".java", ".cs", ".js", ".vsix",".jar"]
txt = [".txt", ".pdf", ".doc", ".pdf", ".ppt", ".pps", ".docx", ".pptx"]
music = [".mp3", ".wav", ".wma", ".mpa", ".ram", ".ra", ".aac", ".aif", ".m4a", ".tsa"]
zip = [".zip", ".rar", ".arj", ".gz", ".sit", ".sitx", ".sea", ".ace", ".bz2", ".7z"]
app = [".exe", ".msi"]
vid = [".mp4",".webm",".mkv",".MPG",".MP2",".MPEG",".MPE",".MPV",".OGG",".M4P",".M4V",
    ".WMV",".MOV",".QT",".FLV",".SWF",".AVCHD",".avi",".mpg",".mpe",".mpeg",".asf",
    ".wmv",".mov",".qt",".rm",]
torrents = [".torrent"]

def move(arr,name,ex,file):
    for i in range(len(arr)):
        if ex == arr[i]:
            move(file,name)

def start():
    for files in os.listdir():
        try:
            _, ex = path.splitext(files)
            move(pic,"Picture",ex,files);
            move(vid,"Video",ex,files);
            move(pytho,"Programming File",ex,files);
            move(txt,"Documents",ex,files);
            move(music,"Music",ex,files)
            move(torrents,"Torrents",ex,files);
            move(txt,"Application",ex,files);
            move(zip,"Compressed",ex,files)
        except:
            print("Couldn't move file ", files)

if __name__ == "__main__":
    start()

    "Picture",
    "Video",
    "Documents",
    "Music",    
]
for root in paths:
    try:
        os.mkdir(root)
    except OSError:
        print("Folder Already Exists")

pic = [".jpeg", ".jpg", ".png", ".gif", ".tiff", ".raw"]
pytho = [".ipynb", ".java", ".cs", ".js"]
txt = [".txt", ".pdf", ".doc", ".pdf", ".ppt", ".pps", ".docx", ".pptx"]
music = [".mp3", ".wav", ".wma", ".mpa", ".ram", ".ra", ".aac", ".aif", ".m4a", ".tsa"]
zip = [".zip", ".rar", ".arj", ".gz", ".sit", ".sitx", ".sea", ".ace", ".bz2", ".7z"]
app = [".exe", ".msi"]
vid = [".mp4",".webm",".mkv",".MPG",".MP2",".MPEG",".MPE",".MPV",".OGG",".M4P",".M4V",
    ".WMV",".MOV",".QT",".FLV",".SWF",".AVCHD",".avi",".mpg",".mpe",".mpeg",".asf",
    ".wmv",".mov",".qt",".rm",]


def start():
    for files in os.listdir():
        _, ex = path.splitext(files)
        for i in range(len(pic)):
            if ex == pic[i]:
                move(files, "Picture")
        for i in range(len(vid)):
            if ex == vid[i]:
                move(files, "Video")
        for i in range(len(pytho)):
            if ex == pytho[i]:
                move(files, "Programing File")
        for i in range(len(txt)):
            if ex == txt[i]:
                move(files, "Documents")
        for i in range(len(music)):
            if ex == music[i]:
                move(files, "Music")
        for i in range(len(app)):
            if ex == app[i]:
                move(files, "Application")
        for i in range(len(zip)):
            if ex == zip[i]:
                move(files, "Compressed")

if __name__ == "__main__":
    start()
