import os
import importlib.util
import time
print("Checking Dependencies")
if importlib.util.find_spec("tkinter") is None:
    print("tkinter NOT INSTALLED,RUN pip install tkinter")
    os.system("pause")
    exit()

print("Dependencies OK")
time.sleep(5.5)

from os import path
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()

print("Select Source Folder")
Source_Path = filedialog.askdirectory()
print("Source Path : ",Source_Path) 

print("Select Destination Path")
Destination = filedialog.askdirectory()
print("Destination Path : ",Destination)

fileprfx = input("File Prefix :")
filetype = input("File Type (ex .doc .exe .png) :")

def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        dst =  fileprfx + " " + str(count) + filetype

        # rename all the files
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))

# Driver Code
if __name__ == '__main__':
    main()