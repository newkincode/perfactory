import tkinter
import json

window=tkinter.Tk()

conveyorBeltImg = tkinter.PhotoImage(file="asset/img/conveyor_belt.png")
conveyorBeltImgUL = tkinter.PhotoImage(file="asset/img/conveyor_belt_ul.png")
conveyorBeltImgLR = tkinter.PhotoImage(file="asset/img/conveyor_belt_lr.png")
selectItem = 0

def setSelect(a):
    save = open("data/playerData.json","w")
    save.write(json.dumps({"selectItem":a}))
    save.close()

window.title("sfg2컨트롤")
window.geometry("640x400")
window.resizable(False, False)

canvas = tkinter.Canvas(window,width=640, height=400)
canvas.place(x=50, y=30)

canvas.create_rectangle(10, 10, 278, 278, outline='black', width=3)

selectText=tkinter.Label(window, text="아이템 선택")
selectText.place(x=50, y=30)

conveyorBeltBtn = tkinter.Button(window,image=conveyorBeltImg, command=lambda: setSelect(0))
conveyorBeltBtn.place(x=70, y=62)

conveyorBeltULBtn = tkinter.Button(window,image=conveyorBeltImgUL, command=lambda: setSelect(1))
conveyorBeltULBtn.place(x=122, y=62)

conveyorBeltLRBtn = tkinter.Button(window,image=conveyorBeltImgLR, command=lambda: setSelect(2))
conveyorBeltLRBtn.place(x=174, y=62)


window.mainloop()