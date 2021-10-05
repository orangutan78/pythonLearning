from tkinter import *
import tkinter.messagebox as m
class log_in():
    '登录程序'
    def __init__(self):
        self.lst=[['admin','Python@16']]
        root.title('登录')
        root.configure(bg='lightgoldenrodyellow')
        root.geometry('300x200')
        lab1=Label(root,text='请输入账号',bg='lightgoldenrodyellow')
        lab1.pack()
        ent1=Entry(root)
        ent1.pack()
        lab2=Label(root,text='请输入密码',bg='lightgoldenrodyellow')
        lab2.pack()
        ent2=Entry(root,show='*')
        ent2.pack()
        btn1=Button(root,text='登录',command=lambda:self.logIn(ent1.get(),ent2.get()))
        btn1.pack()
        btn2=Button(root,text='注册',command=lambda:self.logOut(ent1.get(),ent2.get()))
        btn2.pack()
    def logIn(self,user,pwd):
        length=len(self.lst)
        turn=0
        for i in range(length):
            if self.lst[turn][0]==user:
                break
            else:
                turn+=1
        if turn==length:
            m.showerror('ERROR!','账号有误！')
        else:
            if self.lst[turn][1]==pwd:
                m.showinfo('CONGURATULATIONS!','登录成功！')
            else:
                m.showerror('ERROR!','密码有误！')
    def logOut(self,user,pwd):
        if user==None or user=='\0' or pwd==None or pwd=='\0':
            m.showerror('ERROR!','帐号或密码为空！')
        else:
            lst=[user,pwd]
            self.lst+=[lst]
            m.showinfo('CONGURATULATIONS!','注册成功！')
root=Tk()
log_in()
root.mainloop()