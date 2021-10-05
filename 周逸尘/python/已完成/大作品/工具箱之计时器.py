import time
import tkinter
import math
###########
class Start_program:
    '程序开始'
    before_time=0.0
    now_time=0.0
    distance_time=0.0
    distance_time_minute=0
    distance_time_second=0
    distance_time_microsecond=0
    pause_or_not=1
    turn=0
    saved_str=''
    saved_time=0
    is_reset=0
    def __init__(self):
        root.geometry('400x300')
        root.title('计时器     开始/暂停:空格；记次:C；停止:S')
        root.configure(bg='lightgray')
        root.resizable(width=False,height=False)
        self.var=tkinter.StringVar()
        self.var.set('00:00:00')
        lab1=tkinter.Label(root,text='TIMER',bg='lightgray')
        lab1.pack()
        self.lab2=tkinter.Label(root,textvariable=self.var,bg='lightgray',font=('微软雅黑',70))
        self.lab2.place(x=10,y=20)
        btn1=tkinter.Button(root,text='开始',command=lambda:self.start(None),bg='lightgray')
        btn1.place(x=100,y=150)
        btn2=tkinter.Button(root,text='暂停',command=self.pause,bg='lightgray')
        btn2.place(x=150,y=150)
        btn3=tkinter.Button(root,text='记次',command=lambda:self.count(None),bg='lightgray')
        btn3.place(x=200,y=150)
        btn4=tkinter.Button(root,text='清零',command=lambda:self.rstt(None),bg='lightgray')
        btn4.place(x=250,y=150)
        root.bind('<space>',self.space_pressed)
        root.bind('<KeyPress-c>',self.count)
        root.bind('<KeyPress-s>',self.rstt)
        self.root=root
    def space_pressed(self,event):
        if self.pause_or_not==0:
            self.pause_or_not=1
        else:
            self.start(self.root)
    def start(self,event):
        self.is_reset=0
        self.pause_or_not=0
        self.root.update()
        self.before_time=time.time()
        while True:
            try:
                if self.pause_or_not==0:
                    self.root.update()
                    self.now_time=time.time()
                    self.distance_time=self.now_time-self.before_time+self.saved_time
                    self.distance_time_minute=math.floor(self.distance_time/60)
                    print(self.saved_time)
                    if self.distance_time_minute<100:
                        self.distance_time_second=math.floor(self.distance_time-self.distance_time_minute*60)
                        self.distance_time_microsecond=math.floor((self.distance_time-self.distance_time_minute*60-self.distance_time_second)*100)
                        if math.floor(self.distance_time_minute/10)==0:
                            self.distance_time_minute=str(0)+str(self.distance_time_minute)
                        if math.floor(self.distance_time_second/10)==0:
                            self.distance_time_second=str(0)+str(self.distance_time_second)
                        if math.floor(self.distance_time_microsecond/10)==0:
                            self.distance_time_microsecond=str(0)+str(self.distance_time_microsecond)
                        self.saved_str=str(self.distance_time_minute)+':'+str(self.distance_time_second)+':'+str(self.distance_time_microsecond)
                        self.var.set(self.saved_str)
                else:
                    if self.is_reset==0:
                        self.saved_time=self.distance_time
                    break
            except:
                break
    def pause(self):
        self.pause_or_not=1
    def count(self,event):
        if self.turn<=999 and self.pause_or_not==0:
            self.turn+=1
            if self.turn%9==1:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(y=180)
            elif self.turn%9==2:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(y=220)
            elif self.turn%9==3:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(y=260)
            elif self.turn%9==4:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(x=135,y=180)
            elif self.turn%9==5:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(x=135,y=220)
            elif self.turn%9==6:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(x=135,y=260)
            elif self.turn%9==7:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(x=270,y=180)
            elif self.turn%9==8:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(x=270,y=220)
            elif self.turn%9==0:
                l_count=tkinter.Label(self.root,text=str(self.turn)+' '+self.saved_str,font=('微软雅黑',16),bg='lightgray')
                l_count.place(x=270,y=260)
    def rstt(self,event):
        self.before_time=0.0
        self.now_time=0.0
        self.distance_time=0.0
        self.distance_time_minute=0
        self.distance_time_second=0
        self.distance_time_microsecond=0
        self.pause_or_not=1
        self.turn=0
        self.saved_time=0
        self.saved_str=''
        self.is_reset=1
        self.var.set("00:00:00")
        self.root.bind('<space>',self.space_pressed)
        self.root.bind('<KeyPress-c>',self.count)
        self.root.bind('<KeyPress-s>',self.rstt)
###########
root=tkinter.Tk()
start_program=Start_program()
###########
root.mainloop()