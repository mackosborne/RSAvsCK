import tkinter as tk
from tkinter import ttk
from time import sleep
from deleter import *


root = tk.Tk()
root.geometry("1000x1000")

generate_button = tk.Button(root, text="Generate", command=lambda:start_generation() )
generate_button.pack()

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

#---------- Functions ----------#
#Look for CSVs in the directory
def find_csvs():
    csvs = []
    for file in os.listdir():
        if file.endswith(".csv") or file.endswith(".arff"):
            csvs.append(file)
    return csvs


if __name__ == "__main__":
    
    #app = App()
    #app.mainloop()
    files = ["CK_Stream.csv", "CK_Stream_Training.csv", "RSA_Stream.csv", "RSA_Stream_Training.csv", "CK_Stream.arff", "CK_Stream_Training.arff", "RSA_Stream.arff", "RSA_Stream_Training.arff"]
    files.append(find_csvs())
    #files = find_csvs()


    for file in files:
        if file == "CK_Stream.csv":
            file.remove(file)
        elif file == "CK_Stream_Training.csv":
            file.remove(file)
        elif file == "RSA_Stream.csv":
            file.remove(file)
        elif file == "RSA_Stream_Training.csv":
            file.remove(file)
        elif file == "CK_Stream.arff":
            file.remove(file)
        elif file == "CK_Stream_Training.arff":
            file.remove(file)
        elif file == "RSA_Stream.arff":
            file.remove(file)
        elif file == "RSA_Stream_Training.arff":
            file.remove(file)
    if files != []:
        popup("Insufficient Data. Missing" + files)
    popup.mainloop()
    root.mainloop()