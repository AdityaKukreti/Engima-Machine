import csv
from tkinter import *


FONT = "Verdana"

ROOT = Tk()
ROOT.title("Enigma Machine Simulator")
ROOT.geometry("450x280")
ROOT.resizable(False,False)
ROOT.configure(bg="#333333")

Label(text = "Rotors: ", font = FONT, fg = "white", bg="#333333").place(relx = 0.025, y = 20, width = 100, height = 30)
rotor_box = Entry(font = FONT)
rotor_box.insert(END,"I-II-III")
rotor_box.place(x = 150, y = 20, width = 250, height = 30)


Label(text = "Rotor Start: ", font = FONT, fg = "white", bg="#333333").place(relx = 0.005, y = 60, width = 160, height = 30)
rotor_start_box = Entry(font = FONT)
rotor_start_box.insert(END,"MCK")
rotor_start_box.place(x = 150, y = 60, width = 250, height = 30)

Label(text = "Rings: ", font = FONT, fg = "white", bg="#333333").place(relx = 0.025, y = 100, width = 90, height = 30)
rings_box = Entry(font = FONT)
rings_box.insert(END,"AAA")
rings_box.place(x = 150, y = 100, width = 250, height = 30)


Label(text = "Plugboard: ", font = FONT, fg = "white", bg="#333333").place(relx = 0.02, y = 140, width = 135, height = 30)
plugboard_box = Entry(font = FONT)
plugboard_box.place(x = 150, y = 140, width = 250, height = 30)


Label(text = "Reflector: ", font = FONT, fg = "white", bg="#333333").place(relx = 0.01, y = 180, width = 135, height = 30)
reflector_box = Entry(font = FONT)
reflector_box.insert(END,"B")
reflector_box.place(x = 150, y = 180, width = 250, height = 30)


def result_setter():
    global ROOT,STATUS
    rotor_data = rotor_box.get().split("-")
    r1 = rotor_data[0]
    r2 = rotor_data[1]
    r3 = rotor_data[2]
    pb = plugboard_box.get().split()
    rf = reflector_box.get()
    
    with open("config.csv","w") as cf:
        writer = csv.writer(cf)
        writer.writerow([r1,r2,r3,rotor_start_box.get(),[ord(rings_box.get()[0])-64,ord(rings_box.get()[1])-64,ord(rings_box.get()[2])-64],pb,rf])
    ROOT.destroy()


Button(text = "Submit", font = FONT, bg = "grey",bd = 0,activebackground="#bfbebb",command= lambda : (result_setter())).place(relx = 0.35, y = 230, width = 120, height = 30)
