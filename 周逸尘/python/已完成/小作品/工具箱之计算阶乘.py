import tkinter
from tkinter.constants import W
import tkinter.messagebox
###########
class Λ:
    '阶乘'
    def __init__(self):
        root.geometry('400x300')
        root.title('计算阶乘')
        root.configure(bg='lavender')
        lab1=tkinter.Label(root,text='请输入要计算阶乘的数',bg='lavender')
        lab1.pack()
        ent1=tkinter.Entry(root,bg='lightgray')
        ent1.pack()
        btn1=tkinter.Button(root,text='计算',command=lambda:self.start(ent1.get(),root),bg='lavender')
        btn1.pack()
    def start(self,ent_get,parent):
        time_turn=1
        time_ok_number=1
        try:
            num_get=float(ent_get)
            if num_get>100:
                tkinter.messagebox.showerror('ERROR!','输入数字过大！')
            elif num_get!=int(num_get):
                tkinter.messagebox.showerror('ERROR!','请输入整数！')
            elif num_get<0:
                tkinter.messagebox.showerror('ERROR!','请输入正数！')
            else:
                int_get=int(num_get)
                for i in range(int_get):
                    time_ok_number*=time_turn
                    time_turn+=1
                l=tkinter.Label(root,text=ent_get+'!='+str(time_ok_number),bg='lavender') 
                l.pack(anchor=W)
        except ValueError:
            tkinter.messagebox.showerror('ERROR!','请输入数字！')
###########
root=tkinter.Tk()
λ=Λ()
###########
root.mainloop()