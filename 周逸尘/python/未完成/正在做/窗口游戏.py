from tkinter import*
from tkinter.messagebox import askokcancel as okcancel
import time
from random import*
import sys
sys.setrecursionlimit(10**9)
def start_program():
    class tk_game :
        moveX=(10,110,210)
        moveY=(10,40,70,100,130,160)
        rdmobj=('red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','blue','blue','yellow','yellow','yellow','green','orange','orange')
        speed=1
        score=0
        score_mode=1
        high_score_sum=0
        heart=3
        blue_num=-1
        saved_speed=0
        no_enemy=-1
        def __init__(self):
            root.title('得分:0 生命:3')
            root.configure(bg='black')
            root.geometry('300x190')
            root.resizable(False,False)
            x=10
            for i in range(3):
                y=10
                for i in range(5):
                    Label(root,text='                   ',bg='white').place(x=x,y=y)
                    y+=30
                x+=100
            x=10
            for i in range(3):
                Label(root,text='                   ',bg='silver').place(x=x,y=y)
                x+=100
            self.ctrl_x=1
            self.lab_ctrl=Label(root,text='                   ',bg='dimgray')
            self.lab_ctrl.place(x=self.moveX[self.ctrl_x],y=160)
            root.bind('<Left>',self.move_left)
            root.bind('<Right>',self.move_right)
            root.bind('<a>',self.move_left)
            root.bind('<d>',self.move_right)
            self.parent=root
            self.start_game()
        def start_game(self):
            if choice(self.rdmobj)=='yellow':
                self.yellow()
            elif choice(self.rdmobj)=='blue':
                self.blue()
            elif choice(self.rdmobj)=='orange':
                self.orange()
            elif choice(self.rdmobj)=='green':
                self.green()
            else:
                self.red()
        def move_left(self,event):
            if self.ctrl_x>=1:
                self.ctrl_x-=1
            self.lab_ctrl.place_forget()
            self.lab_ctrl.place(x=self.moveX[self.ctrl_x],y=160)
        def move_right(self,event):
            if self.ctrl_x<=1:
                self.ctrl_x+=1
            self.lab_ctrl.place_forget()
            self.lab_ctrl.place(x=self.moveX[self.ctrl_x],y=160)
        def red(self):
            cc=choice((0,1,2))
            y=0
            try:
                l_red=Label(self.parent,bg='red',text='                   ')
                l_red.place(x=self.moveX[cc],y=self.moveY[y])
                for i in range(5):
                    self.wait_time(2)
                    y+=1
                    try:
                        l_red.place_forget()
                        l_red.place(x=self.moveX[cc],y=self.moveY[y])
                    except:
                        break
                if self.ctrl_x==cc:
                    l_red.place_forget()
                    self.score+=self.score_mode
                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                else:
                    t=time.time()
                    break_no=True
                    while time.time()-t<=0.3/self.speed and break_no:
                        try:
                            if self.no_enemy==-1:
                                if self.ctrl_x==cc:
                                    l_red.place_forget()
                                    self.score+=self.score_mode
                                else:
                                    break_no=False
                                    l_red.place_forget()
                                    self.heart-=1
                                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                                    self.parent.configure(bg='red')
                                    self.wait_time(2)
                                    self.parent.configure(bg='black')
                                    if self.heart==0:
                                        m=okcancel('GAME OVER!','得分：'+str(self.score)+'\n要重新再来吗？')
                                        if m:
                                            self.parent.destroy()
                                            start_program()
                                            break
                                        else:
                                            self.parent.destroy()
                            else:
                                l_red.place_forget()
                            self.parent.update()
                        except:
                            break
            except:
                try:
                    self.parent.quit()
                except:
                    pass
                pass
            try:
                if self.score_mode==2:
                    self.high_score_sum+=1
                    if self.high_score_sum==4:
                        self.high_score_sum=0
                        self.parent.configure(bg='black')
                        self.score_mode=1
                if self.blue_num!=-1:
                    self.blue_num+=1
                if self.blue_num>=4:
                    self.blue_num=-1
                    self.speed=self.saved_speed
                    self.parent.configure(bg='black')
                if self.no_enemy!=-1:
                    self.no_enemy+=1
                if self.no_enemy==4:
                    self.no_enemy=-1
                    self.parent.configure(bg='black')
                self.start_game()
            except:
                pass
        def blue(self):
            cc=choice((0,1,2))
            y=0
            try:
                l_blue=Label(self.parent,bg='blue',text='                   ')
                l_blue.place(x=self.moveX[cc],y=self.moveY[y])
                for i in range(5):
                    self.wait_time(2)
                    y+=1
                    try:
                        l_blue.place_forget()
                        l_blue.place(x=self.moveX[cc],y=self.moveY[y])
                    except:
                        break
                if self.ctrl_x==cc:
                    l_blue.place_forget()
                    self.score+=self.score_mode
                    self.parent.configure(bg='darkblue')
                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                else:
                    t=time.time()
                    break_no=True
                    while time.time()-t<=0.3/self.speed and break_no:
                        try:
                            if self.no_enemy==-1:
                                if self.ctrl_x==cc:
                                    l_blue.place_forget()
                                    self.score+=self.score_mode
                                    self.parent.configure(bg='darkblue')
                                else:
                                    break_no=False
                                    l_blue.place_forget()
                                    self.heart-=1
                                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                                    self.parent.configure(bg='red')
                                    self.wait_time(2)
                                    self.parent.configure(bg='black')
                                    if self.heart==0:
                                        m=okcancel('GAME OVER!','得分：'+str(self.score)+'\n要重新再来吗？')
                                        if m:
                                            self.parent.destroy()
                                            start_program()
                                            break
                                        else:
                                            self.parent.destroy()
                            else:
                                l_blue.place_forget()
                            self.parent.update()
                        except:
                            break
            except:
                try:
                    self.parent.quit()
                except:
                    pass
                pass
            try:
                self.blue_num=0
                self.saved_speed=self.speed
                self.speed=self.speed-0.25
                if self.score_mode==2:
                    self.high_score_sum+=1
                    if self.high_score_sum==4:
                        self.high_score_sum=0
                        self.parent.configure(bg='black')
                        self.score_mode=1
                if self.blue_num!=-1:
                    self.blue_num+=1
                if self.blue_num>=4:
                    self.blue_num=-1
                    self.speed=self.saved_speed
                    self.parent.configure(bg='black')
                try:
                    self.parent.configure(bg='blue')
                except:
                    pass
                if self.no_enemy!=-1:
                    self.no_enemy+=1
                if self.no_enemy==4:
                    self.no_enemy=-1
                    self.parent.configure(bg='black')
                self.start_game()
            except:
                pass
        def yellow(self):
            cc=choice((0,1,2))
            y=0
            try:
                l_yellow=Label(self.parent,bg='yellow',text='                   ')
                l_yellow.place(x=self.moveX[cc],y=self.moveY[y])
                for i in range(5):
                    self.wait_time(2)
                    y+=1
                    try:
                        l_yellow.place_forget()
                        l_yellow.place(x=self.moveX[cc],y=self.moveY[y])
                    except:
                        break
                if self.ctrl_x==cc:
                    l_yellow.place_forget()
                    self.score+=self.score_mode
                    self.parent.configure(bg='gold')
                    self.score_mode=2
                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                else:
                    t=time.time()
                    break_no=True
                    while time.time()-t<=0.3/self.speed and break_no:
                        try:
                            if self.no_enemy==-1:
                                if self.ctrl_x==cc:
                                    l_yellow.place_forget()
                                    self.score+=self.score_mode
                                    self.parent.configure(bg='gold')
                                    self.score_mode=2
                                else:
                                    break_no=False
                                    l_yellow.place_forget()
                                    self.heart-=1
                                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                                    self.parent.configure(bg='red')
                                    self.wait_time(2)
                                    self.parent.configure(bg='black')
                                    if self.heart==0:
                                        m=okcancel('GAME OVER!','得分：'+str(self.score)+'\n要重新再来吗？')
                                        if m:
                                            self.parent.destroy()
                                            start_program()
                                            break
                                        else:
                                            self.parent.destroy()
                            else:
                                l_yellow.place_forget()
                            self.parent.update()
                        except:
                            break
            except:
                try:
                    self.parent.quit()
                except:
                    pass
                pass
            try:
                if self.blue_num!=-1:
                    self.blue_num+=1
                if self.blue_num>=4:
                    self.blue_num=-1
                    self.speed=self.saved_speed
                    self.parent.configure(bg='black')
                try:
                    self.parent.configure(bg='gold')
                except:
                    pass
                
                if self.no_enemy!=-1:
                    self.no_enemy+=1
                if self.no_enemy==4:
                    self.no_enemy=-1
                    self.parent.configure(bg='black')
                self.start_game()
            except:
                pass
        def orange(self):
            cc=choice((0,1,2))
            y=0
            try:
                l_orange=Label(self.parent,bg='orange',text='                   ')
                l_orange.place(x=self.moveX[cc],y=self.moveY[y])
                for i in range(5):
                    self.wait_time(2)
                    y+=1
                    try:
                        l_orange.place_forget()
                        l_orange.place(x=self.moveX[cc],y=self.moveY[y])
                    except:
                        break
                if self.ctrl_x==cc:
                    self.parent.configure(bg='orange')
                    l_orange.place_forget()
                    self.score+=self.score_mode
                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                else:
                    t=time.time()
                    break_no=True
                    while time.time()-t<=0.3/self.speed and break_no:
                        try:
                            if self.no_enemy==-1:
                                if self.ctrl_x==cc:
                                    self.parent.configure(bg='orange')
                                    self.no_enemy=0
                                    l_orange.place_forget()
                                    self.score+=self.score_mode
                                else:
                                    break_no=False
                                    l_orange.place_forget()
                                    if self.heart==0:
                                        m=okcancel('GAME OVER!','得分：'+str(self.score)+'\n要重新再来吗？')
                                        if m:
                                            self.parent.destroy()
                                            start_program()
                                            break
                                        else:
                                            self.parent.destroy()
                            else:
                                l_orange.place_forget()
                            self.parent.update()
                        except:
                            break
            except:
                try:
                    self.parent.quit()
                except:
                    pass
                pass
            try:
                self.no_enemy=0
                self.parent.configure(bg='orange')
                if self.score_mode==2:
                    self.high_score_sum+=1
                    if self.high_score_sum==4:
                        self.high_score_sum=0
                        self.parent.configure(bg='black')
                        self.score_mode=1
                if self.blue_num!=-1:
                    self.blue_num+=1
                if self.blue_num>=4:
                    self.blue_num=-1
                    self.speed=self.saved_speed
                    self.parent.configure(bg='black')
                if self.no_enemy!=-1:
                    self.no_enemy+=1
                if self.no_enemy==4:
                    self.no_enemy=-1
                    self.parent.configure(bg='black')
                self.start_game()
            except:
                pass
        def green(self):
            cc=choice((0,1,2))
            y=0
            try:
                l_green=Label(self.parent,bg='green',text='                   ')
                l_green.place(x=self.moveX[cc],y=self.moveY[y])
                for i in range(5):
                    self.wait_time(1)
                    y+=1
                    try:
                        l_green.place_forget()
                        l_green.place(x=self.moveX[cc],y=self.moveY[y])
                    except:
                        break
                if self.ctrl_x==cc:
                    self.parent.configure(bg='green')
                    l_green.place_forget()
                    self.heart+=1
                    self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                    self.wait_time(2)
                    self.parent.configure(bg='black')
                else:
                    t=time.time()
                    break_no=True
                    while time.time()-t<=0.15/self.speed and break_no:
                        try:
                            if self.ctrl_x==cc:
                                self.parent.configure(bg='green')
                                l_green.place_forget()
                                self.heart+=1
                                self.parent.title('得分:'+str(self.score)+' 生命:'+str(self.heart))
                                self.wait_time(2)
                                self.parent.configure(bg='black')
                            l_green.place_forget()
                            self.parent.update()
                        except:
                            break
            except:
                try:
                    self.parent.quit()
                except:
                    pass
                pass
            try:
                self.start_game()
            except:
                pass
        def wait_time(self,mode):
            self.speed+=(1/self.speed)*0.01
            #print(self.speed)
            t=time.time()
            if mode==1:
                wt=0.15
            else:
                wt=0.3
            while time.time()-t<=wt/self.speed:
                try:
                    self.parent.update()
                except:
                    try:
                        self.parent.quit()
                    except:
                        break
                    pass
    root=Tk()
    tk_game()
    root.mainloop()
start_program()