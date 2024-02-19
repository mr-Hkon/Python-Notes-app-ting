import tkinter as tk
import json
from tkinter import filedialog
import os

side1 = tk.Tk()
side1.title("en_side")
side1.geometry("1920x1080+-1915+120")
side1.state("zoomed")

sideicon = tk.PhotoImage(file="cat.png")
side1.iconphoto(True, sideicon)



def naikjetrykk():
    tekstnr1lbl.config(text="stoppp")


def exitknapp():
    side1.destroy()


def popup1():
    popupwindov = tk.Toplevel(side1)
    popupwindov.title("popopp")
    popupwindov.geometry("480x360+1100+500")
    tekstnr1lbl.pack()
    tekstnr3lbl = tk.Label(popupwindov, text="ein liten pop up")
    tekstnr3lbl.pack()


for i in range(100):
    side1.grid_rowconfigure(i, weight=1)

for j in range(200):
    side1.grid_columnconfigure(j, weight=1)

lagratekst = ""
#if lagratekst == "":
#    lagratekst = "tomt"


def lagra():
    global lagratekst
    lagratekst = inputtxt.get("1.0", tk.END)
    with open("savedtext.json", "w") as f:
        json.dump(lagratekst, f)

def load():
    global lagratekst
    with open("savedtext.json", "r") as f:
        lagratekst=json.load(f)
        inputtxt.delete("1.0", tk.END)
        inputtxt.insert(tk.END, lagratekst)
        print(lagratekst)

def file_list():
    Hkons_jsonfiles = [file for file in os.listdir() if file.endswith(".json")]
    rowss= 0
    for each jsonfil in Hkons_jsonfiles:
        jsonbtns = tk.Button(side1, text=)






testlbl = tk.Label(side1, text=lagratekst)
tekstnr1lbl = tk.Label(side1, text="HALLOOO")
tekstnr2lbl = tk.Label(side1, text="hei")
knappnr1btn = tk.Button(side1, text="kje trykk", command=naikjetrykk)
exitbtn = tk.Button(side1, text="exitt", command=exitknapp)
popoppbtn = tk.Button(side1, text="trykk", command=popup1)

lagrebtn = tk.Button(side1, text="save", command=lagra)
loadbtn = tk.Button(side1, text="load", command=load)

entrytry = tk.Entry(side1)
inputtxt = tk.Text(side1, height=1, width=1)




# tekstnr1lbl.place(x=50, y=25)
# tekstnr2lbl.place(x=60, y=30)
# knappnr1btn.pack()
knappnr1btn.grid(row=50, column=150, columnspan=1)
exitbtn.grid(row=2, column=1, rowspan=5, columnspan=5, sticky="nsew")
popoppbtn.grid(row=22, column=11, columnspan=1, rowspan=2, sticky="nsew")

lagrebtn.grid(row=10, column=11, padx=1, rowspan=2, columnspan=5, pady=1, sticky="nsew")
loadbtn.grid(row=10, column=16, padx=1, rowspan=2, columnspan=5, pady=1, sticky="nsew")
inputtxt.grid(row=5, column=11, rowspan=5, columnspan=10, sticky="nsew")

# exitbtn.place(x=1880, y=1050)
# popoppbtn.pack()
side1.mainloop()
