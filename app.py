import tkinter as tk
from tkinter import ttk
from time import sleep
from deleter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Encryption GUI")
        self.geometry("1000x1000")
        
#-----------------------Frame for Generate Cyphertext-----------------------#
        self.frame = tk.Frame(self)
        self.frame.pack()

        #Create a label widget
        self.label = ttk.Label(self.frame, text="Generate Ciphertext")
        self.label.pack()
        
        #Dropdown to select which encryption algorithm to use
        self.dropdown = ttk.Combobox(self.frame, values=["RSA", "Kyber512","Kyber768","Kyber1024"])
        self.dropdown.pack()

        #Text box to define number of iterations
        self.textbox = ttk.Entry(self.frame)
        self.textbox.pack()

        #Radio Button to select Training or Testing
        self.radio = ttk.Radiobutton(self, text="Training", value=1)
        self.radio.pack()
        self.radio = ttk.Radiobutton(self, text="Testing", value=2)
        self.radio.pack()


        #Generate Ciphertext Button
        self.button = ttk.Button(self.frame, text="Generate Ciphertext", command=self.start_loading)
        self.button.pack()

        #Create a progress bar widget
        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

#-----------------------Frame for View Ciphertext-----------------------#
        self.frame = tk.Frame(self)
        self.frame.pack()

        #Create a label widget
        self.label = ttk.Label(self.frame, text="View Ciphertext")
        self.label.pack()

        #Dropdown to select which CSV to view
        self.dropdown = ttk.Combobox(self.frame, values=["-none-"])
        self.dropdown.pack()

        #Text to display Average Encryption Time
        self.text = ttk.Entry(self.frame)
        self.text.pack()

        #Text to display number of iterations
        self.text = ttk.Entry(self.frame)
        self.text.pack()

        #Text to display total time
        self.text = ttk.Entry(self.frame)
        self.text.pack()

        #--- Window for ciphertext viewing ---#
        #frame for viewing csvs
        self.frame = tk.Frame(self)
        self.frame.pack(pady=1)

        #Create a text widget
        self.text = tk.Text(self.frame, width=40, height=10)
        self.text.pack(side="left", fill="both", expand=True)

        #Create a scrollbar widget
        self.scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.text.yview)
        self.scroll.pack(side="right", fill="y")

        #Configure the text widget
        self.text.config(yscrollcommand=self.scroll.set)

        #Button to open selected csv
        self.button = ttk.Button(self, text="Open File", command=self.start_loading)
        self.button.pack()


    #Launches a popup window
    def popup(msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()

        
        files = find_csvs()
        
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
    

    


    def start_loading(self):
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
    app = App()
    app.mainloop()
    files = find_csvs()
        
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