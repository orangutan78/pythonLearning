import time
from winsound import Beep
from tkinter import*
from math import floor
class metronome:
    '节拍器'
    speed=100#formula:beep_time=(60/speed)/3*100=20000/speed(ms);wait_time=60/speed*(2/3)=40/speed(s)
    beat=4
    color=0#0:black;1:red;2:gray
    start_or_not=False
    def __init__(self):
        root.title('节拍器')
        root.geometry('300x330')
        root.configure(bg='navajowhite')
        root.resizable(0,0)
        for i in range(5):
            Label(root,bg='navajowhite').pack()
        lab_readme=Label(root,text='README',bg='navajowhite',font=('微软雅黑',15))
        lab_readme.place(x=105,y=90)
        Label(root,text='空格-开始/暂停\n上键-加快速度\n下键-减慢速度\n左键-降低拍数\n右键-提高拍数',font=('微软雅黑',12),bg='navajowhite').pack()
        self.speed_label=Label(root,text='当前速度：'+str(self.speed),bg='navajowhite',font=('微软雅黑',25))
        self.speed_label.place(x=30,y=25)
        Label(root,text='BPM',font=('黑体',8),bg='navajowhite').place(x=255,y=50)
        self.beat_label=Label(root,text='当前节拍：'+str(self.beat),bg='navajowhite',font=('微软雅黑',25))
        self.beat_label.place(x=50,y=240)
        self.color_label=Label(root,text='    ',bg='black',pady=0)
        self.color_label.place(x=10,y=10)
        root.bind('<space>',self.start)
        root.bind('<Up>',self.fast)
        root.bind('<Down>',self.slow)
        root.bind('<Left>',self.subtract)
        root.bind('<Right>',self.add)
        self.parent=root
    def start(self,event):
        if not self.start_or_not:
            self.start_or_not=True
            while self.start_or_not:
                try:
                    self.color_label.place_forget()
                    self.color_label=Label(self.parent,text='    ',bg='red',fg='red',pady=0)
                    self.color_label.place(x=10,y=10)
                    self.parent.update()
                    print(1)
                    beep_time=floor(18500/self.speed)
                    self.color_label=Label(self.parent,text='    ',bg='black',pady=0)
                    self.color_label.place(x=10,y=10)
                    wait_time=40/self.speed
                    Beep(1200,beep_time)
                    print(2)
                    self.wait(wait_time)
                    self.parent.update()
                    self.parent.bind('<space>',self.start)
                except TclError:
                    break
                for i in range(self.beat-1):
                    if self.start_or_not:
                        beep_time=floor(18500/self.speed)
                        wait_time=40/self.speed
                        try:
                            self.color_label=Label(self.parent,text='    ',bg='gray',pady=0)
                            self.color_label.place(x=10,y=10)
                            self.parent.update()
                            Beep(600,beep_time)
                            self.color_label=Label(self.parent,text='    ',bg='black',pady=0)
                            self.color_label.place(x=10,y=10)
                            self.wait(wait_time)
                            self.parent.update()
                        except:
                            break
                    try:
                        self.parent.bind('<space>',self.start)
                    except TclError:
                        break
        else:
            self.start_or_not=False
    def fast(self,event):
        if self.speed<300:
            self.speed+=1
            try:
                self.speed_label.place_forget()
                self.speed_label=Label(root,text='当前速度：'+str(self.speed),bg='navajowhite',font=('微软雅黑',25))
                self.speed_label.place(x=30,y=25)
            except:
                pass
    def slow(self,event):
        if self.speed>30:
            self.speed-=1
            try:
                self.speed_label.place_forget()
                self.speed_label=Label(root,text='当前速度：'+str(self.speed),bg='navajowhite',font=('微软雅黑',25))
                self.speed_label.place(x=30,y=25)
            except:
                pass
    def add(self,event):
        if self.beat<10:
            self.beat+=1
            try:
                self.beat_label.place_forget()
                self.beat_label=Label(root,text='当前节拍：'+str(self.beat),bg='navajowhite',font=('微软雅黑',25))
                self.beat_label.place(x=50,y=240)
            except:
                pass
    def subtract(self,event):
        if self.beat>1:
            self.beat-=1
            try:
                self.beat_label.place_forget()
                self.beat_label=Label(root,text='当前节拍：'+str(self.beat),bg='navajowhite',font=('微软雅黑',25))
                self.beat_label.place(x=50,y=240)
            except:
                pass
    def wait(self,wait_time):
        bt=time.time()
        while time.time()<bt+wait_time:
            try:
                self.parent.update()
            except TclError:
                break
root=Tk()
metronome()
root.mainloop()