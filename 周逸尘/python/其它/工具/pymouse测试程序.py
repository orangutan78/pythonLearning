from tkinter import *
def start():
    global var
    global turn
    turn+=1
    var.set(turn)
turn=0
win=Tk()
win.geometry('200x150')
var=IntVar()
var.set(0)
Button(win,textvariable=var,width=10,height=3,font=('微软雅黑',20),bd=3,command=start).pack()
win.mainloop()