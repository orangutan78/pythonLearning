import tkinter
import tkinter.messagebox
class 判断:
    def __init__(self,parent):
        parent.title('判断质数合数')
        parent.geometry('300x500')
        parent.configure(bg='thistle')
        lab1=tkinter.Label(parent,text='请输入要判断的数',bg='thistle')
        lab1.pack()
        ent1=tkinter.Entry(parent,bg='lightgray')
        ent1.pack()
        btn1=tkinter.Button(parent,text='判断',bg='plum',command=lambda:self.start(parent,ent1.get()))
        btn1.pack()
    def start(self,parent,number_to_panduan):
        num_turn=0
        is_heshu=0
        try:
            int_panduan=int(number_to_panduan)
            if int_panduan>10000000:
                tkinter.messagebox.showerror('ERROR!','输入数字过大！')
            else:
                if int_panduan<=1:
                    tkinter.messagebox.showerror('ERROR!','请输入大于1的数！')
                else:
                    if int(int_panduan/3)==int_panduan/3:
                        for i in range(int(int_panduan/3)):
                            num_turn+=1
                            if int(int_panduan/num_turn)==int_panduan/num_turn and int_panduan!=3:
                                is_heshu=1
                    if int(int_panduan/2)==int_panduan/2:
                            is_heshu=1
                    if is_heshu==1:
                        lab2=tkinter.Label(parent,text=str(number_to_panduan)+'是合数',bg='thistle')
                        lab2.pack()
                    else:
                        lab3=tkinter.Label(parent,text=str(number_to_panduan)+'是质数',bg='thistle')
                        lab3.pack()
        except ValueError:
            tkinter.messagebox.showerror('ERROR!','请输入整数！')
tk=tkinter.Tk()
panduan=判断(tk)
tk.mainloop()