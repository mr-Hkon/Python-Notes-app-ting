import tkinter as tk
from tkinter import filedialog
import json
import os

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


def popup1():
    popupwindov = tk.Toplevel(side1)
    popupwindov.title("popopp")
    popupwindov.geometry("480x360+1100+500")
    tekstnr1lbl.grid(row=3, column=5)
    tekstnr3lbl = tk.Label(popupwindov, text="ein liten pop up")
    tekstnr3lbl.pack()


for i in range(100):
    side1.grid_rowconfigure(i, weight=1)

for j in range(200):
    side1.grid_columnconfigure(j, weight=1)

lagratekst = ""
#if lagratekst == "":
#    lagratekst = "tomt"


currentfile = ""

#if currentfile != "":
#    print("there is something in the file")
#else:
#    print("there is nothin here")


def lagra(currentfile):
    global lagratekst
    if currentfile != "":
        lagratekst = inputtxt.get("1.0", tk.END)
        with open(currentfile, "w") as f:
            json.dump(lagratekst, f)

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




#testlbl = tk.Label(side1, text=lagratekst)
tekstnr1lbl = tk.Label(side1, text="HALLOOO")
tekstnr2lbl = tk.Label(side1, text="hei")
knappnr1btn = tk.Button(side1, text="kje trykk", command=naikjetrykk)
exitbtn = tk.Button(side1, text="X", command=exitknapp)
exitbtn.config(bg="grey55", font=(20), height= 1, width=2)
##popoppbtn = tk.Button(side1, text="trykk", command=popup1)

lagrebtn = tk.Button(side1, text="Save", command=lambda: lagra(currentfile))
loadbtn = tk.Button(side1, text="Load", command=load)

#entrytry = tk.Entry(side1)
inputtxt = tk.Text(side1, height=1, width=1, borderwidth=5,)

########### PUT PÅ BORDER COLOR??????????????????????????????????????????????????????????????????????????


# tekstnr1lbl.place(x=50, y=25)
# tekstnr2lbl.place(x=60, y=30)
# knappnr1btn.pack()
knappnr1btn.grid(row=50, column=150, columnspan=1)
exitbtn.grid(row=2, column=1, rowspan=5, columnspan=5, sticky="nsew", padx=0, pady=0)
##popoppbtn.grid(row=22, column=11, columnspan=1, rowspan=2, sticky="nsew")

lagrebtn.grid(row=84, column=22, padx=1, rowspan=3, columnspan=10, pady=1, sticky="nsew")
#loadbtn.grid(row=10, column=16, padx=1, rowspan=2, columnspan=5, pady=1, sticky="nsew")
inputtxt.grid(row=8, column=22, rowspan=75, columnspan=150, sticky="nsew")
inputtxt.config(bg="grey55")

# exitbtn.place(x=1880, y=1050)
# popoppbtn.pack()
side1.mainloop()
