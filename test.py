import os
import subprocess
import sys

opener = "open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, "outputs/CK_Stream_Training.csv"])


#Load a given file


#CK_Stream_Training.csv

dir = os.listdir()
file = input("Enter file name: ")
file = "./outputs/" + file
#if os.path.exists(file):
os.startfile(file)
#else:
print("File does not exist")