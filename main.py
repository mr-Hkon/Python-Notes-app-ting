import tkinter as tk
from tkinter import filedialog
import json
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/HåkonEllingsen/Desktop/FIREBASEPY/tryy-f9c82-firebase-adminsdk-bs40e-1da15df9d4.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tryy-f9c82-default-rtdb.europe-west1.firebasedatabase.app'
})




plas = db.reference('/mby/savedtext')
dataa =plas.get()
print(dataa)

side1 = tk.Tk()
side1.title("en_side")
side1.geometry("1920x1080+-1915+120")
side1.state("zoomed")
side1.configure(bg="gray18")

sideicon = tk.PhotoImage(file="cat.png")
side1.iconphoto(True, sideicon)



def naikjetrykk():
    tekstnr1lbl.config(text="stoppp")
def exitknapp():
    side1.destroy()


for i in range(100):
    side1.grid_rowconfigure(i, weight=1)

for j in range(200):
    side1.grid_columnconfigure(j, weight=1)

lagratekst = ""
currentfile = ""






def lagra(currentfile):
    global lagratekst
    global savedfire
    if currentfile != "":
        fixafil = currentfile.replace('.json','')
        savedfire = db.reference(f'/lagrafiler/{fixafil}')
        lagratekst = inputtxt.get("1.0", tk.END)
        with open(currentfile, "w") as f:
            json.dump(lagratekst, f)
        savedfire.set(lagratekst)
        print(savedfire)

def load(file_path):
    global lagratekst
    global currentfile
    with open(file_path, "r") as f:
        lagratekst=json.load(f)
        inputtxt.delete("1.0", tk.END)
        inputtxt.insert(tk.END, lagratekst)
        print(lagratekst)
        currentfile = file_path
        print("the file is: ", file_path)

def nyjson():
    global currentfile
    file_name = tk.simpledialog.askstring("Input", "File Name:")
    if file_name:
        with open(file_name+'.json', 'w') as f:
            json.dump("", f)
        print("sucses in making: ", file_name)
        file_list()


def file_list():
    Hkons_jsonfiles = [file for file in os.listdir() if file.endswith(".json")]
    rowss= 8
    for jsonfil in Hkons_jsonfiles:
        namejsonfil, ext = os.path.splitext(jsonfil)
        jsonbtns = tk.Button(side1, text=namejsonfil, command=lambda fp=jsonfil: load(fp), height=2 )
        jsonbtns.grid(row=rowss, column=1, columnspan=20, sticky='ew')
        jsonbtns.config(bg="grey55", font=("TkDefaultFont", 10, "bold"))
        rowss += 1


file_list()



nyjsonbtn= tk.Button(side1, text="ny text", command=nyjson, height=2,)
nyjsonbtn.grid(row=82, column=1, rowspan=1, columnspan= 20, sticky='ew')


tekstnr1lbl = tk.Label(side1, text="HALLOOO")
tekstnr2lbl = tk.Label(side1, text="hei")
knappnr1btn = tk.Button(side1, text="kje trykk", command=naikjetrykk)

exitbtn = tk.Button(side1, text="X", command=exitknapp)
exitbtn.config(bg="grey55", font=(20), height= 1, width=2)
lagrebtn = tk.Button(side1, text="Save", command=lambda: lagra(currentfile))
loadbtn = tk.Button(side1, text="Load", command=load)


inputtxt = tk.Text(side1, height=1, width=1, borderwidth=5,)

########### PUT PÅ BORDER COLOR??????????????????????????????????????????????????????????????????????????


knappnr1btn.grid(row=50, column=150, columnspan=1)
exitbtn.grid(row=2, column=1, rowspan=5, columnspan=5, sticky="nsew", padx=0, pady=0)


lagrebtn.grid(row=84, column=22, padx=1, rowspan=3, columnspan=10, pady=1, sticky="nsew")
#loadbtn.grid(row=10, column=16, padx=1, rowspan=2, columnspan=5, pady=1, sticky="nsew")
inputtxt.grid(row=8, column=22, rowspan=75, columnspan=150, sticky="nsew")
inputtxt.config(bg="grey55")



side1.mainloop()

#fix firebase file load
#remove firebase cred thin in the start and use a file with gitignore