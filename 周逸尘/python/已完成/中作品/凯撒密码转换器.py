from tkinter import*
from tkinter.messagebox import showerror as s
class st:
    '开始'
    strings='abcdefghijklmnopqrstuvwxyz'
    t=tuple(strings)
    upper_strings=str.upper(strings)
    upper_t=tuple(upper_strings)
    def __init__(self):
        r.title('凯撒密码转换器')
        r.geometry('400x300')
        r.configure(bg='azure')
        Label(r,text='请输入明文',bg='azure').pack()
        e1=Entry(r)
        e1.pack()
        Label(r,text='请输入偏移量',bg='azure').pack()
        e2=Entry(r)
        e2.pack()
        Button(r,text='转换',bg='azure',command=lambda:self.st(e1.get(),e2.get(),r)).pack()
    def st(self,e1g,e2g,parent):
        end=''
        try:
            if int(e2g)!=float(e2g):
                s('ERROR!','偏移量必须是整数！')
            elif int(e2g)>25:
                s('ERROR!','偏移量过大！')
            elif int(e2g)<-25:
                s('ERROR!','偏移量过小！')
            else:
                n=int(e2g)
                l=list(e1g)
                t=0
                for i in range(len(l)):
                    if l[t] in self.t:
                        order=self.t.index(l[t])
                        try:
                            end+=self.t[order+n]
                        except IndexError:
                            out=25-order
                            o=n-out-1
                            end+=self.t[o]
                    elif l[t] in self.upper_t:
                        order=self.upper_t.index(l[t])
                        try:
                            end+=self.upper_t[order+n]
                        except IndexError:
                            out=25-order
                            o=n-out-1
                            end+=self.t[o]
                    else:
                        end+=l[t]
                    t+=1
        except ValueError:
            s('ERROR!','偏移量必须是整数！')
            pass
        if end=='':
            s('ERROR!','内容不是凯撒密码的格式！')
        else:
            Label(parent,text=e1g+'的凯撒密码是：'+end,bg='azure',font=('微软雅黑',12)).pack(anchor=W)
r=Tk()
st()
r.mainloop()