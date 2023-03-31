import tkinter as tk
from tkinter import ttk
from time import sleep
from deleter import *
import sys
#Get Both RSA and CK
#Command line
#export PYTHONPATH='/home/mack/Desktop/RSAvsCK/kyber'
#export PYTHONPATH='/home/mack/Desktop/RSAvsCK/RSA_gen'
sys.path.insert(0, '/home/mack/Desktop/RSAvsCK/kyber')
sys.path.insert(0, '/home/mack/Desktop/RSAvsCK/RSA_gen')
from CK_Gen import *
from RSA_Gen import *
import sys

print(sys.path)
print("Done")

#Select Kyber Version
select = int(input("Enter 1 or nothing for Kyber512, 2 for Kyber768, 3 for Kyber1024: "))
#Select Training or Testing  
method = int(input("Training 1, Test 2: "))
#Select string creation method      
isStatic = int(input("Static Gen 1, Random Gen 2: "))
#Select number of iterations
limit = int(input("Enter number of iterations: "))
if(select == 1):
    KyberChoice = "Kyber512"
if(select == 2):
    KyberChoice = "Kyber768"  
if(select == 3):
    KyberChoice = "Kyber1024"
else:
    KyberChoice = "Kyber512"
kyber.generate(KyberChoice, method, isStatic, limit)
print("Done")


#---------- Functions ----------#
#Launches a popup window
def popup(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    B2 = ttk.Button(popup, text="Exit Program", command = quit)
    B2.pack()

#Starts the generation process
def start_generation(self):
    popup("Generation will replace all existing files. Please remove any .arff or .csv you wish to save from working directoryContinue?")
    #Disable the button
    self.button.config(state="disabled")

    #Start Loading and update the progress bar
    for i in range(101):
        sleep(0.1)
        self.progress["value"] = i
        self.progress.update()
    #Enable the button
    self.button.config(state="enabled")


#Look for CSVs in the directory
def find_csvs():
    csvs = []
    for file in os.listdir():
        if file.endswith(".csv") or file.endswith(".arff"):
            csvs.append(file)
    return csvs
#Opens a file
def open_file(file):
    fileWindow = tk.Tk()
    fileWindow.wm_title(file)
    #If the file exists
    if os.path.exists(file):
        #Load text from file
        with open(file, "r") as f:
            content = f.read()
    elif os.path.exists("./outputs/" + file):
        #Load text from file
        with open("./outputs/" + file, "r") as f:
            content = f.read()
    elif file == '' or file == None or file == ' ':
        content = "No file selected"
    else:
        content = "Error"
    lable = ttk.Label(fileWindow, text=content)
    lable.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(fileWindow, text="Close", command = fileWindow.destroy)
    B1.pack()

#----------------------------------#