import tkinter
import tkinter.messagebox
###############
txt=None
labtxt=None
num=0
################
def ok(t):
    l3=tkinter.Label(tk,text=t)
    l3.pack()
################
def start(x,y):
    global labtxt
    global num
    try:
        num=float(x)
        num=float(y)
        if x>y:
            txt=x
        elif x==y:
            txt="一样"
        elif x<y:
            txt=y
        labtxt=txt+"大"
        ok(labtxt)
    except ValueError:
        tkinter.messagebox.showerror(title='ERROR!',message='请输入数字')
##################
tk=tkinter.Tk()
tk.title("比大小")
tk.geometry("400x300")
l1=tkinter.Label(tk,text="请输入数字1")
l1.pack()
e1=tkinter.Entry(tk)
e1.pack()
l2=tkinter.Label(tk,text="请输入数字2")
l2.pack()
e2=tkinter.Entry(tk)
e2.pack()
b=tkinter.Button(tk,text="比大小",command=lambda:start(e1.get(),e2.get()))
b.pack()
###################
tk.mainloop()
