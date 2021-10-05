import tkinter
import tkinter.messagebox
################
class Plus_one:
    '加一'
    def __init__(self,who_win):
        global draw_turn
        global red_win_turn
        global black_win_turn
        if who_win==0:
            draw_turn+=1
        elif who_win==1:
            black_win_turn+=1
        elif who_win==2:
            red_win_turn+=1
################
class XO:
    turn=0
    num=0
    x=0
    img=None
    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    is_done=0
    def __init__(self,msgbx_True_or_False):
        self.red_win_turn=red_win_turn
        self.black_win_turn=black_win_turn
        self.draw_turn=draw_turn
        start=self.start
        tk.geometry('307x308+200+200')
        tk.title('井字棋')
        tk.resizable(width=False,height=False)
        tk.configure(bg='black')
        tk.overrideredirect(True)
        self.b1=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(1,imagex,imageo))
        self.b1.place(x=30,y=30)
        self.b2=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(2,imagex,imageo))
        self.b2.place(x=130,y=30)
        self.b3=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(3,imagex,imageo))
        self.b3.place(x=230,y=30)
        self.b4=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(4,imagex,imageo))
        self.b4.place(x=30,y=130)
        self.b5=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(5,imagex,imageo))
        self.b5.place(x=130,y=130)
        self.b6=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(6,imagex,imageo))
        self.b6.place(x=230,y=130)
        self.b7=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(7,imagex,imageo))
        self.b7.place(x=30,y=230)
        self.b8=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(8,imagex,imageo))
        self.b8.place(x=130,y=230)
        self.b9=tkinter.Button(tk,bd=0,height=4,width=10,command=lambda:start(9,imagex,imageo))
        self.b9.place(x=230,y=230)
        self.lx=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx2=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo2=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx3=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo3=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx4=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo4=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx5=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo5=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx6=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo6=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx7=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo7=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx8=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo8=tkinter.Label(tk,image=imageo,height=73,width=72)
        self.lx9=tkinter.Label(tk,image=imagex,height=73,width=72)
        self.lo9=tkinter.Label(tk,image=imageo,height=73,width=72)
        l_fill_green=tkinter.Label(tk,text='    ',bg='darkseagreen',fg='darkseagreen',font=('微软雅黑',10),padx=5,height=14)
        l=tkinter.Label(tk,text='\n重\n新\n开\n始\n，\n\n退\n出\n游\n戏',bg='darkseagreen',font=('微软雅黑',10),width=3,height=14,fg='white')
        l_English1=tkinter.Label(tk,text='TIPS:\nCtrl+p',bg='darkseagreen',font=('微软雅黑',6),padx=0,fg='white')
        l_English2=tkinter.Label(tk,text='Ctrl+q',bg='darkseagreen',font=('微软雅黑',6),padx=0,fg='white')
        l_title=tkinter.Label(tk,text='井字棋3.0  对局:'+str(self.red_win_turn+self.black_win_turn+self.draw_turn)+' P1胜:'+str(self.black_win_turn)+' P2胜:'+str(self.red_win_turn)+' 平局:'+str(self.draw_turn),font=('微软雅黑',12),width=30,pady=2,bg='darkseagreen',fg='white')
        l_fill_black=tkinter.Label(tk,text='    ',bg='black',pady=4)
        self.tk=tk
        self.tk.bind('<Control-p>',self.restart)
        self.tk.bind('<Control-q>',self.window_quit)
        if msgbx_True_or_False==1:
            l_title.place(x=1,y=1)
            l_fill_black.place(x=306,y=1)
            self.restart(None)
        else:
            l_fill_green.place(x=1,y=20)
            l.place(x=1,y=35)
            l_English1.place(x=1,y=54)
            l_English2.place(x=1,y=179)
            l_title.place(x=1,y=1)
            l_fill_black.place(x=306,y=1)
    def restart(self,event):
        b1=self.b1
        b2=self.b2
        b3=self.b3
        b4=self.b4
        b5=self.b5
        b6=self.b6
        b7=self.b7
        b8=self.b8
        b9=self.b9
        b1.place_forget()
        b2.place_forget()
        b3.place_forget()
        b4.place_forget()
        b5.place_forget()
        b6.place_forget()
        b7.place_forget()
        b8.place_forget()
        b9.place_forget()
        self.lx.place_forget()
        self.lx2.place_forget()
        self.lx3.place_forget()
        self.lx4.place_forget()
        self.lx5.place_forget()
        self.lx6.place_forget()
        self.lx7.place_forget()
        self.lx8.place_forget()
        self.lx9.place_forget()
        self.lo.place_forget()
        self.lo2.place_forget()
        self.lo3.place_forget()
        self.lo4.place_forget()
        self.lo5.place_forget()
        self.lo6.place_forget()
        self.lo7.place_forget()
        self.lo8.place_forget()
        self.lo9.place_forget()
        b1.place(x=30,y=30)
        b2.place(x=130,y=30)
        b3.place(x=230,y=30)
        b4.place(x=30,y=130)
        b5.place(x=130,y=130)
        b6.place(x=230,y=130)
        b7.place(x=30,y=230)
        b8.place(x=130,y=230)
        b9.place(x=230,y=230)
        self.turn=0
        self.num=0
        self.x=0
        self.img=None
        self.i1=0
        self.i2=0
        self.i3=0
        self.i4=0
        self.i5=0
        self.i6=0
        self.i7=0
        self.i8=0
        self.i9=0
        self.is_done=0
    ################
    def start(self,x=0,imgx=None,imgo=None):
        turn=self.turn
        num=self.num
        i1=self.i1
        i2=self.i2
        i3=self.i3
        i4=self.i4
        i5=self.i5
        i6=self.i6
        i7=self.i7
        i8=self.i8
        i9=self.i9
        b1=self.b1
        b2=self.b2
        b3=self.b3
        b4=self.b4
        b5=self.b5
        b6=self.b6
        b7=self.b7
        b8=self.b8
        b9=self.b9
        lx=self.lx
        lx2=self.lx2
        lx3=self.lx3
        lx4=self.lx4
        lx5=self.lx5
        lx6=self.lx6
        lx7=self.lx7
        lx8=self.lx8
        lx9=self.lx9
        lo=self.lo
        lo2=self.lo2
        lo3=self.lo3
        lo4=self.lo4
        lo5=self.lo5
        lo6=self.lo6
        lo7=self.lo7
        lo8=self.lo8
        lo9=self.lo9
        is_done=self.is_done
        if is_done==0:
            turn=turn+1
            num=turn/2
            if num==int(num):
                img=imgo
            else:
                img=imgx
            if x==1:
                b1.place_forget()
                if img==imgx:
                    lx.place(x=30,y=30)
                    i1=1
                else:
                    lo.place(x=30,y=30)
                    i1=2
            elif x==2:
                b2.place_forget()
                if img==imgx:
                    lx2.place(x=130,y=30)
                    i2=1
                else:
                    lo2.place(x=130,y=30)
                    i2=2
            elif x==3:
                b3.place_forget()
                if img==imgx:
                    lx3.place(x=230,y=30)
                    i3=1
                else:
                    lo3.place(x=230,y=30)
                    i3=2
            elif x==4:
                b4.place_forget()
                if img==imgx:
                    lx4.place(x=30,y=130)
                    i4=1
                else:
                    lo4.place(x=30,y=130)
                    i4=2
            elif x==5:
                b5.place_forget()
                if img==imgx:
                    lx5.place(x=130,y=130)
                    i5=1
                else:
                    lo5.place(x=130,y=130)
                    i5=2
            elif x==6:
                b6.place_forget()
                if img==imgx:
                    lx6.place(x=230,y=130)
                    i6=1
                else:
                    lo6.place(x=230,y=130)
                    i6=2
            elif x==7:
                b7.place_forget()
                if img==imgx:
                    lx7.place(x=30,y=230)
                    i7=1
                else:
                    lo7.place(x=30,y=230)
                    i7=2
            elif x==8:
                b8.place_forget()
                if img==imgx:
                    lx8.place(x=130,y=230)
                    i8=1
                else:
                    lo8.place(x=130,y=230)
                    i8=2
            elif x==9:
                b9.place_forget()
                if img==imgx:
                    lx9.place(x=230,y=230)
                    i9=1
                else:
                    lo9.place(x=230,y=230)
                    i9=2
            if i1==i2:
                if i2==i3:
                    if i2==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i2==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i4==i5:
                if i5==i6:
                    if i4==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i4==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i7==i8:
                if i8==i9:
                    if i7==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i7==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i1==i4:
                if i4==i7:
                    if i7==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i7==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i2==i5:
                if i8==i5:
                    if i2==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i2==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i3==i6:
                if i6==i9:
                    if i9==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i9==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i1==i5:
                if i9==i5:
                    if i1==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i1==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i3==i5:
                if i7==i5:
                    if i3==1:
                        m=tkinter.messagebox.showinfo(title='P1 WIN!',message='玩家一胜利！')
                        Plus_one(1)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
                    elif i3==2:
                        m=tkinter.messagebox.showinfo(title='P2 WIN!',message='玩家二胜利！')
                        Plus_one(2)
                        if m:
                            m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                            if m2==True:
                                XO(1)
                        is_done=1
            if i1!=i2 or i1!=i3:
                if i4!=i5 or i4!=i6:
                    if i7!=i8 or i7!=i9:
                        if i1!=i4 or i1!=i7:
                            if i2!=i5 or i2!=i8:
                                if i3!=i6 or i3!=i9:
                                    if i1!=i5 or i1!=i9:
                                        if i3!=i5 or i3!=i7:
                                            if i1!=0:
                                                if i2!=0:
                                                    if i3!=0:
                                                        if i4!=0:
                                                            if i5!=0:
                                                                if i6!=0:
                                                                    if i7!=0:
                                                                        if i8!=0:
                                                                            if i9!=0:
                                                                                m=tkinter.messagebox.showinfo(title='DRAW!',message='平局')
                                                                                self.draw_turn+=1
                                                                                Plus_one(0)
                                                                                if m:
                                                                                    m2=tkinter.messagebox.askokcancel('Want to play again?','要重新开始吗？')
                                                                                    if m2==True:
                                                                                        XO(1)
                                                                                is_done=1
        self.turn=turn
        self.num=num
        self.i1=i1
        self.i2=i2
        self.i3=i3
        self.i4=i4
        self.i5=i5
        self.i6=i6
        self.i7=i7
        self.i8=i8
        self.i9=i9
        self.b1=b1
        self.b2=b2
        self.b3=b3
        self.b4=b4
        self.b5=b5
        self.b6=b6
        self.b7=b7
        self.b8=b8
        self.b9=b9
        self.lx=lx
        self.lx2=lx2
        self.lx3=lx3
        self.lx4=lx4
        self.lx5=lx5
        self.lx6=lx6
        self.lx7=lx7
        self.lx8=lx8
        self.lx9=lx9
        self.lo=lo
        self.lo2=lo2
        self.lo3=lo3
        self.lo4=lo4
        self.lo5=lo5
        self.lo6=lo6
        self.lo7=lo7
        self.lo8=lo8
        self.lo9=lo9
        self.is_done=is_done
    def window_quit(self,event):
        self.tk.quit()
################
tk=tkinter.Tk()
try:
    imagex=tkinter.PhotoImage(file='x.png')
    imageo=tkinter.PhotoImage(file='o.png')
    red_win_turn=0
    black_win_turn=0
    draw_turn=0
    plus_one=Plus_one(3)
    xo=XO(0)
    tk.mainloop()
except:
    tkinter.messagebox.showerror('ERROR!','找不到x.png、o.png！')
################
'''井字棋3.0.py更新说明：
    新增：
        1)窗口美化：
            1.删除窗口自带边框而用Label项替代；
            2.边框四周皆有一像素边框；
            3.提示放置在左侧（2.2版：右侧，干扰视线）
        2)记分系统
    属于加强性更新。
存在BUG:1)重新开始时左侧Label多出一像素（原因：未知）；
        2)按下Ctrl+p时记分系统不参与工作而直到重来的messagebox选择‘是’才累积计算（原因：Class Plus_one 中数据只在CLass XO开始执行时显现）
        3)点击其他窗口时该窗口将永久关闭。'''