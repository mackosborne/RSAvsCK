import tkinter as tk
from tkinter import ttk
from time import sleep
from deleter import *
import RSA_gen
import kyber





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

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Encryption GUI")
        self.geometry("1000x1000")

        #Form 1 Setup
        self.form1 = tk.Frame(self)
        self.form1.pack(side="top", fill="both", expand=True)
        self.form1_label = tk.Label(self.form1, text="Generate Ciphertexts")
        self.form1_label.pack(side="top", fill="x")

        #Dropdown Select
        self.form1_dropdown_var = tk.StringVar()
        self.form1_dropdown_label = tk.Label(self.form1, text="Encryption Algorithm")
        self.form1_dropdown = ttk.Combobox(self.form1, textvariable=self.form1_dropdown_var, values=["RSA", "Kyber512","Kyber768","Kyber1024"])
        self.form1_dropdown_label.pack(side="left")
        self.form1_dropdown.pack(side="left")

        #Text Entry Box
        self.form1_text_var = tk.StringVar()
        self.form1_text_label = tk.Label(self.form1, text="Number of Iterations")
        self.form1_text = tk.Entry(self.form1, textvariable=self.form1_text_var)
        self.form1_text_label.pack(side="left")
        self.form1_text.pack(side="left")

        #Radio Buttons
        self.form1_radio_var = tk.StringVar()
        self.form1_radio_label = tk.Label(self.form1, text="Training or Testing")
        self.form1_radio1 = tk.Radiobutton(self.form1, text="Training", variable=self.form1_radio_var, value="Training")
        self.form1_radio2 = tk.Radiobutton(self.form1, text="Testing", variable=self.form1_radio_var, value="Testing")
        self.form1_radio_label.pack(side="left")
        self.form1_radio1.pack(side="left")
        self.form1_radio2.pack(side="left")

        #Generate Button
        self.button = tk.Button(self.form1, text="Generate", command=lambda: start_generation(self))
        self.button.pack(side="left")

        #Setup Second Form
        self.form2 = tk.Frame(self)
        self.form2.pack(side="top", fill="both", expand=True)
        self.form2_label = tk.Label(self.form2, text="View Ciphertexts")
        self.form2_label.pack(side="top", fill="x")

        #Dropdown Select
        self.form2_dropdown_var = tk.StringVar()
        self.form2_dropdown_label = tk.Label(self.form2, text="Select CSV:")
        #Values will be populated by a function
        self.form2_dropdown = ttk.Combobox(self.form2, textvariable=self.form2_dropdown_var, values=find_csvs())
        self.form2_dropdown_label.pack(side="left")
        self.form2_dropdown.pack(side="left")

        #Text Labels
        self.form2_label1 = tk.Label(self.form2, text = "Data Size:")
        self.form2_label2 = tk.Label(self.form2, text = "Total Generation Time:")
        self.form2_label3 = tk.Label(self.form2, text = "Average Generation Time:")
        self.form2_label1.pack(side="top", fill = "x")
        self.form2_label2.pack(side="top", fill = "x")
        self.form2_label3.pack(side="top", fill = "x")

        #Text Window
        self.form2_text = tk.Text(self.form2, height=10, width=100)
        self.form2_text.pack(side="top", fill="both", expand=True)

        #Open File Button
        self.form2_button = tk.Button(self.form2, text="Open File", command=lambda: open_file(self.form2_dropdown_var.get()))
        self.form2_button.pack(side="left")

if __name__ == "__main__":
    app = App()
    app.mainloop()
