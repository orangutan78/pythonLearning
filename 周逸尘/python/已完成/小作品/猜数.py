import tkinter
import random
import tkinter.messagebox
###########
number=0
txt=None
turn=0
###########
def ok():
    global number
    begin(1)
###########
def begin(a):
    global turn
    turn=turn+1
    if a!=100 and a!=1:
        def start(x,y):
            global number
            global txt
            if y==0:
                number=random.randint(0,10)
            try:
                num=int(x)
                if num>10 or num<0:
                    tkinter.messagebox.showerror(title='PAY ATTENTION!',message='请把范围控制在0~10之间！')
                else:
                    if num==number:
                        txt='你猜对了！'
                        begin(100)
                    elif num<number:
                        txt='小了'
                        begin(1)
                    elif num>number:
                        txt='大了'
                        begin(1)
                    l=tkinter.Label(root,text=txt)
                    l.pack()
            except ValueError:
                tkinter.messagebox.showerror(title='ERROR!',message='请输入整数!')
        root=tkinter.Tk()
        root.geometry('400x300')
        root.title('猜数游戏')
        lab1=tkinter.Label(root,text='请输入一个数')
        lab1.pack()
        ent1=tkinter.Entry(root)
        ent1.pack()
        btn1=tkinter.Button(root,text='guess!',command=lambda:start(ent1.get(),turn))
        btn1.pack()
        btn2=tkinter.Button(root,text='重来',command=ok())
        btn2.pack()
    elif a==100:
        turn=0
###########
rootroot=tkinter.Tk()
b=tkinter.Button(rootroot,text='start!',command=lambda:begin(0))
b.pack()
###########
rootroot.mainloop()