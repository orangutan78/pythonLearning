import tkinter
import random
##########################################
num1=0
num2=0
num3=None
pc_score=0
pp_score=0
x=0
##########################################
def p_to_c():
    global x
    tk_pc=tkinter.Tk()
    tk_pc.geometry("300x200")
    tk_pc.title("人机模式,请开始")
    btn3=tkinter.Button(tk_pc,text="石头",command=lambda:ok(1))
    btn4=tkinter.Button(tk_pc,text="剪刀",command=lambda:ok(2))
    btn5=tkinter.Button(tk_pc,text="布",command=lambda:ok(3))
    btn3.pack()
    btn4.pack()
    btn5.pack()
    if x==1:
        tk_pc.destroy()
        tk_pc=tkinter.Tk()
        tk_pc.geometry("300x200")
        tk_pc.title("人机模式,请开始")
        btn3=tkinter.Button(tk_pc,text="石头",command=lambda:ok(1))
        btn4=tkinter.Button(tk_pc,text="剪刀",command=lambda:ok(2))
        btn5=tkinter.Button(tk_pc,text="布",command=lambda:ok(3))
        btn3.pack()
        btn4.pack()
        btn5.pack()
    x=1
##########################################
def p_to_p():
    tk_pp=tkinter.Tk()
    tk_pp.geometry("300x200")
    tk_pp.title("第一位请开始选择")
    btn6=tkinter.Button(tk_pp,text="石头",command=lambda:pp_ok(1))
    btn7=tkinter.Button(tk_pp,text="剪刀",command=lambda:pp_ok(2))
    btn8=tkinter.Button(tk_pp,text="布",command=lambda:pp_ok(3))
    btn6.pack()
    btn7.pack()
    btn8.pack()
##########################################
tk=tkinter.Tk()
tk.title("石头剪刀布")
tk.geometry("300x200")
lab1=tkinter.Label(tk,text="请选择模式")
btn1=tkinter.Button(tk,text="人机模式",command=p_to_c)
btn2=tkinter.Button(tk,text="双人模式",command=p_to_p)
lab1.pack()
btn1.pack()
btn2.pack()
##########################################
def ok(a):
    tke=tkinter.Tk()
    tke.geometry("300x200")
    ti=None
    tx=None
    num1=a
    if a==1:
        num3="你出了:石头"
    elif a==2:
        num3="你出了:剪刀"
    elif a==3:
        num3="你出了:布"
    lab_pp_p=tkinter.Label(tke,text=num3)
    lab_pp_p.pack()
    pc_form=random.choice(['石头','剪刀','布'])
    if pc_form=='石头':
        lab_pc_stone=tkinter.Label(tke,text="电脑出的是：石头")
        lab_pc_stone.pack()
        num2=1
    elif pc_form=='剪刀':
        lab_pc_cut=tkinter.Label(tke,text="电脑出的是：剪刀")
        lab_pc_cut.pack()
        num2=2
    elif pc_form=='布':
        lab_pc_cloth=tkinter.Label(tke,text="电脑出的是：布")
        num2=3
        lab_pc_cloth.pack()
    if num1==num2:
        ti="draw"
        tx="平局"
    elif num1==1 and num2==2:
        ti="win"
        tx="你赢了"
    elif num1==1 and num2==3:
        ti="lost"
        tx="你输了"
    elif num1==2 and num2==1:
        ti="lost"
        tx="你输了"
    elif num1==2 and num2==3:
        ti="win"
        tx="你赢了"
    elif num1==3 and num2==1:
        ti="win"
        tx="你赢了"
    elif num1==3 and num2==2:
        ti="lost"
        tx="你输了"
    tke.title(ti)
    labe=tkinter.Label(tke,text=tx)
    labe.pack()
    btne=tkinter.Button(tke,text="人机模式",command=p_to_c)
    btne.pack()
    btne1=tkinter.Button(tke,text="双人模式",command=p_to_p)
    btne1.pack()
##########################################
def pp_okok(i,j):
    tit=None
    tx1=None
    tx2=None
    tk_ppe=tkinter.Tk()    
    if i==j:
        tit="draw"
        tx1="平局"
        tx2=None
    elif i==1 and j==2:
        tit="p1win"
        tx1="p1:你赢了"
        tx2="p2:你输了"
    elif i==1 and j==3:
        tit="p2win"
        tx1="p1:你输了"
        tx2="p2:你赢了"
    elif i==2 and j==1:
        tit="p2win"
        tx1="p1:你输了"
        tx2="p2:你赢了"
    elif i==2 and j==3:
        tit="p1win"
        tx1="p1:你赢了"
        tx2="p2:你输了"
        tit="p1win"
        tx1="p1:你赢了"
        tx2="p2:你输了"
    elif i==3 and j==2:
        tit="p2win"
        tx1="p1:你输了"
        tx2="p2:你赢了"
    def ppe_quit():
        tk_ppe.quit()
    tk_ppe.title(tit)
    tk_ppe.geometry("300x200")
    lab_ppe=tkinter.Label(tk_ppe,text=tx1)
    lab_ppe.pack()
    lab_ppe2=tkinter.Label(tk_ppe,text=tx2)
    lab_ppe2.pack()
    btnee=tkinter.Button(tk_ppe,text="人机模式",command=p_to_c)
    btnee.pack()
    btnee1=tkinter.Button(tk_ppe,text="双人模式",command=p_to_p)
    btnee1.pack()
    btnnee2=tkinter.Button(tk_ppe,text='退出',command=ppe_quit)
    btnnee2.pack()
##########################################
def pp_ok(n):
    tk_ppt=tkinter.Tk()
    tk_ppt.geometry("300x200")
    tk_ppt.title("第二位请开始选择")
    btn9=tkinter.Button(tk_ppt,text="石头",command=lambda:pp_okok(n,1))
    btn10=tkinter.Button(tk_ppt,text="剪刀",command=lambda:pp_okok(n,2))
    btn11=tkinter.Button(tk_ppt,text="布",command=lambda:pp_okok(n,3))
    btn9.pack()
    btn10.pack()
    btn11.pack()
##########################################
tk.mainloop()