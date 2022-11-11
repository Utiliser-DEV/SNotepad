import tkinter as tk
import os

lastfile = "NotNamed.txt"
def openfile():
    global lastfile
    def openn():
        global lastfile
        fopen = entry.get()
        lastfile = fopen
        with open(fopen, "r") as filee:
            tmp = filee.read()
            labelinwrite.insert(0.0, tmp)
        openm.destroy()
    openm = tk.Tk()
    openm.title("Открыть файл")
    openm.geometry("450x200")
    openm.resizable(False, False)

    entry = tk.Entry(openm, width=450)
    entry.pack()
    opn = tk.Button(openm, text="Открыть", command=openn)
    opn.place(x=20, y=120)
def save():
    filee = open(lastfile, "w+")
    tmp = labelinwrite.get("1.0",'end-1c')
    filee.write(tmp)
    tmp.close()
def run():
    os.system(f"start {lastfile}\nexit")

root = tk.Tk()
root.title("SNotepad")
root.geometry("560x400")
root["bg"] = "blue"
root.resizable(False, False)

writespace = tk.Frame(root, bg="black", width=560, height=350)
writespace.pack()

labelinwrite = tk.Text(writespace, width=560, height=21)
labelinwrite.pack()
openbtn = tk.Button(root, text="Открыть", command=openfile)
openbtn.place(x=15, y=370)
savebtn = tk.Button(root, text="Сохранить", command=save)
savebtn.place(x=120, y=370)
runbtn = tk.Button(root, text="Запустить", command=run)
runbtn.place(x=255, y=370)

root.mainloop()