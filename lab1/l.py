from tkinter import *
top = Tk()

def createPointCallBack():
    return
def findTriangleCallBack():
    return

top.geometry("1000x700")

C = Canvas(top, bg = "gray", height = 700, width = 700)
C.pack(side = LEFT)

inputFrame = Frame(top, bg = "blue")
inputFrame.pack()

XLabel = Label(inputFrame, text = "X: ")
XLabel.pack()
XEntry = Entry(inputFrame, bd = 5)
XEntry.pack()
YLabel = Label(inputFrame, text = "Y: ")
YLabel.pack()
YEntry = Entry(inputFrame, bd = 5)
YEntry.pack()

createPointButton = Button(inputFrame, text = "Создать точку", command = createPointCallBack())
createPointButton.pack()
findTriangleButton = Button(inputFrame, text = "Найти треугольник", command = findTriangleCallBack())
findTriangleButton.pack()
top.mainloop()
