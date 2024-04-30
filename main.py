import tkinter as tk
from tkinter import filedialog
import json
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

acountkey = {
  "type": "service_account",
  "project_id": "tryy-f9c82",
  "private_key_id": "1da15df9d4c2e8e96b161dffac2a6f280e2d4a1d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCXOZtnkz25PHhX\n7uXADpWCisIlkN+qd8zyc2bBT48zb4gtJhXYNrNC+0j6fX/IVSH3jn8xX7ea3dfD\nut6LSUCNtGcF9KGwIEiq2pSIJx8UhAbAJlPcFT19N10VouTLPD/VCa3uTZICj7il\n3X0cH65IOL2ALHcncuWv5rVbnjO3a9+CQ8dFW8T2GccELbsu3/GvbcWxlFemeIDE\nOBivUtQ+ok/BLutYRnkQ4eo3PDdCWBI5cUOONBhVXRuIG6zdV0DOoS6pj4wMInvM\neaydWfNIzySdqL81yVb26BwxnIQFbpd7zyVVWqvaSyDMjsFWF+Hbi4+mdzTTz1hj\n26Wu8E95AgMBAAECggEAAguUibg8+3yRHtcu+256nlG166JUY8ZvRWWTmm83rE+d\n8KCZ9UpmeBMEI2Fb/R6ITaVjl8Umua0Lj68sJh9TS7dUgSV3rYguZJnlotkZyaNW\nOBwjHFKIjRVWqIXwQxGyz4fZJjAiRgvkHfRh2lL7vChuEn7MMtyzQ0B7/uCtZ3SL\nY+baLI/eSmDnL5APO7vZCku8My34tGD37q9qaIC11q1u9Na7dN9Hu/FhNxuipdRL\nLsVBTM0T/7POQxcGWq6MjWXclYLtpTDqo502LLP5N+LEhIAQZrQS61Fksmslm+jj\nlbyQB+apSaikZ0IVgPt1J9yW1kk3DGaqYhtoOGTNwwKBgQDPsVNRuheko4myTDVJ\n7VW8aIrBvuJ70fk8B/QXQABDCKcrhiwC4Urhb3yRxDD7jCdQwkkgbYUj20AXPQfL\nC0SGqP6VAByUdVPWLl0/0oOPXyaiA+SwcyChGhTdvIVPx6MxjMcJekDEZT4ocDqd\nEokjzBDyxJPmNkk8PChxd1TuNwKBgQC6ZgUx9mWikeCJkZOw34T3sySje+KMYebM\nCuxaPsKtSTX9re4r/Md1/M15eEfQAEkT4+VOt/Sir3lT69fdlWp3qyZ8YgU0wNcM\n7XquH5YFbtONLtsZ5M/KDtyp9bB3LyPSoQ38DCwt5DQ/latYLJ+LmbkV/UNXQzhy\nSlg4fqlXzwKBgEnoBwcpGmq6yzAIUForO3wdE2tYWs3G7VLAXcq8OpugA6TITPcF\nZpkMDB7u2qNYv1DMoisI7fzRc2ARlqlZLBxjHJy2+nSVv6ySuRoR9kDZkizLB+EG\nRtEtL8mr4SB/oQHr35PuzgdVI6ZOMX1dcDGt10YcT6j3Hl5x5c5isXVHAoGAWUdQ\nKbQYzhsM7xdZJBiLOZEGdX967T5fK0/4EOmKmTE9uPm74Dm815h0Wj/wNYJNfkdj\np6aYd+uQM0/9HtbYHeVOE7lnQPM0ja6ZWhkq5ANHNJJCw05C8EbaDlXtZcigYdxe\nNGEoL/rjw6jOXvdQm67PZebegEdkG+ncA4M3XSUCgYBRCZdARYYbnt3WyUXFYqDA\nYKY4BaSpbXkzumOT9nmx/yGNXlHXa9UeZw5y4Bu2p5Eeow2wErxPuGT7IPsZJ5Lw\nzzCV9ytULcGWbDIiHVuUuDiOEW0FM+E26M11GVx9Kk+V95Y/59Xnkj/h212UHtmf\nXf5yWBhJe3z1gOteyzn9Lw==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-bs40e@tryy-f9c82.iam.gserviceaccount.com",
  "client_id": "115243368868211466673",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bs40e%40tryy-f9c82.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(acountkey)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tryy-f9c82-default-rtdb.europe-west1.firebasedatabase.app'
})




plas = db.reference('/lagrafiler')
#plas.set('')
dataa =plas.get()
print(dataa)

side1 = tk.Tk()
side1.title("en_side")
side1.geometry("1920x1080+-1915+120")
side1.state("zoomed")
side1.configure(bg="gray18")

sideicon = tk.PhotoImage(file="cat.png")
side1.iconphoto(True, sideicon)


savedplace = 'C:/Users/HåkonEllingsen/PycharmProjects/skoletkinter/notes'
#os.makedirs(savedplace, exist_ok=True)   # skjønne kje heilt denna linjå

firebasesavedplace = db.reference('/lagrafiler')
data = firebasesavedplace.get()
fil_names = list(data.keys()) if data else []


for file_name in fil_names:
    file_ref = firebasesavedplace.child(file_name)
    file_innehold = file_ref.get()
    savedfile = os.path.join(savedplace, f'{file_name}.json')
    with open(savedfile, 'w') as file:
        json.dump(file_innehold, file)
    print(f'saved {file_name}.json')


print (data)



def naikjetrykk():
    tekstnr1lbl.config(text="stoppp")
def exitknapp():
    side1.destroy()


for i in range(100):
    side1.grid_rowconfigure(i, weight=1)

for j in range(200):
    side1.grid_columnconfigure(j, weight=1)

#lagratekst = ""
currentfile = ""






def lagra(currentfile):
    global lagratekst
    global savedfire
    if currentfile != "":
        fixafil = os.path.basename(currentfile).replace('.json','')
        savedfire = db.reference(f'/lagrafiler/{fixafil}')
        print(f"the fixafil is: {fixafil}")
        lagratekst = inputtxt.get("1.0", tk.END)
        print(f"det som lagres e denna texten: {lagratekst}")
        try:
            savedfire.set(lagratekst)
        except Exception as e:
            print(f"Error saving: {e}")
        savedplace
        savethis = fixafil + '.json'
        #file

        with open(currentfile, "w") as f:
            json.dump(lagratekst, f)
    else:
        print("currentfile is empty")

def load(file_path):
    global lagratekst
    global currentfile
    global savedplace
    global filplacement
    filplacement = os.path.join(savedplace, file_path)
    if os.path.exists(filplacement):
        print(f"finne folder{filplacement}")
    else:
        print("fant kje folder")
    print(file_path)
    with open(filplacement, "r") as f:
        print ("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        lagratekst=json.load(f)
        inputtxt.delete("1.0", tk.END)
        inputtxt.insert(tk.END, lagratekst)
        print(lagratekst)
        currentfile = filplacement
        print("the file is: ", filplacement)

#def deletefile():



def nyjson():
    global currentfile
    file_name = tk.simpledialog.askstring("Input", "File Name:")
    if file_name:
        filenew = os.path.join(savedplace, file_name + '.json')
        with open(filenew, 'w') as f:
            json.dump("", f)
        print("sucses in making: ", file_name)
        file_list()


def file_list():
    global savedplace
    Hkons_jsonfiles = [file for file in os.listdir(savedplace) if file.endswith(".json")]
    rowss= 8
    for jsonfil in Hkons_jsonfiles:
        namejsonfil, ext = os.path.splitext(jsonfil)
        jsonbtns = tk.Button(side1, text=namejsonfil, command=lambda fp=jsonfil: load(fp), height=2 )
        jsonbtns.grid(row=rowss, column=1, columnspan=20, sticky='ew')
        jsonbtns.config(bg="grey55", font=("TkDefaultFont", 10, "bold"))
        rowss += 1
        print(f"rows:{rowss}")


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
