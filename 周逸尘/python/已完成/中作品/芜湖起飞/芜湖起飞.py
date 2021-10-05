# -*- coding:utf-8 -*-
import tkinter
import turtle
import tkinter.messagebox
import time
import random
import threading
from tkinter.constants import W
class Whqf:
    '芜湖起飞'
    a=0
    txt_end=None
    choose_no_turn=0
    choose_yes_turn=0
    def __init__(self,parent):
        parent.geometry('340x190+400+400')
        parent.configure(bg='lightgoldenrodyellow')
        parent.title('芜湖起飞')
        parent.resizable(width=False,height=False)
        self.btn1=tkinter.Button(parent,text='起飞!',font=('黑体',81),bd=4,command=lambda:self.start_loading(parent))
        self.btn1.pack()
        self.lab1=tkinter.Label(root)
    def start_loading(self,parent):
        for i in range(20):
            parent.geometry('300x100+400+400')
            try:
                self.lab1.pack_forget()
                self.a=self.a+1
                forth_a=self.a/4
                if int(forth_a)==forth_a:
                    self.txt_end='—'
                elif int(forth_a)==forth_a-0.25:
                    self.txt_end='/ .'
                elif int(forth_a)==forth_a-0.5:
                    self.txt_end='|..'
                elif int(forth_a)==forth_a-0.75:
                    self.txt_end='\\...'
                self.lab1=tkinter.Label(parent,text='loading'+self.txt_end,bg='lightgoldenrodyellow',font=('华文隶书',60))
                self.btn1.pack_forget()
                self.lab1.pack(anchor=W)
                parent.update()
                time.sleep(0.2)
            except:
                break
        self.lab1.pack_forget()
        parent.destroy()
        self.create_new_window()
    def create_new_window(self):
        new_win=tkinter.Tk()
        new_win.geometry('406x406+400+400')
        try:
            smile=tkinter.PhotoImage(file='D:\学习\pythonLearning\周逸尘\python\已完成\中作品\芜湖起飞\奸笑.png')
            a_corner=tkinter.PhotoImage(file='D:\学习\pythonLearning\周逸尘\python\已完成\中作品\芜湖起飞\局部.png')
        except FileNotFoundError:
            tkinter.messagebox.showerror('ERROR!','找不到奸笑.png、局部.png文件！')
        lab_new_win1=tkinter.Label(new_win,image=smile)
        lab_new_win1.pack()
        lab_new_win2=tkinter.Label(new_win,font=('华文行楷',20),image=a_corner,fg='red',text='你是伞兵吗？', compound="center",bd=0,bg='red')
        lab_new_win2.place(x=130,y=50)
        btn_new_win3=tkinter.Button(new_win,font=('华文行楷',15),image=None,fg='blue',text='是', compound="center",bd=0,padx=25,pady=0,bg='deeppink',command=self.choose_yes)
        btn_new_win3.place(x=55,y=150)
        btn_new_win4=tkinter.Button(new_win,font=('华文行楷',15),image=None,fg='blue',text='否', compound="center",bd=0,padx=25,pady=0,bg='deeppink',command=self.choose_no)
        btn_new_win4.place(x=280,y=150)
        new_win.mainloop()
    def choose_yes(self):
        self.choose_yes_turn+=1
        if self.choose_yes_turn<2:
            try:
                turtle.shape('turtle')
                turtle.speed(0)
                turtle.penup()
                turtle.goto(-450,300)#你
                turtle.speed(6)
                turtle.pendown()
                turtle.pensize(10)
                turtle.goto(-550,100)
                turtle.penup()
                turtle.goto(-500,200)
                turtle.right(90)
                turtle.pendown()
                turtle.forward(200)
                turtle.penup()
                turtle.goto(-380,300)
                turtle.pendown()
                turtle.goto(-460,140)
                turtle.penup()
                turtle.goto(-413,220)
                turtle.pendown()
                turtle.left(90)
                turtle.forward(150)
                turtle.right(120)
                turtle.forward(80)
                turtle.penup()
                turtle.goto(-375,200)
                turtle.pendown()
                turtle.left(30)
                turtle.forward(220)
                turtle.right(120)
                turtle.forward(50)
                turtle.penup()
                turtle.goto(-420,150)
                turtle.pendown()
                turtle.goto(-460,70)
                turtle.penup()
                turtle.goto(-330,150)
                turtle.pendown()
                turtle.goto(-290,70)
                turtle.penup()
                turtle.goto(-200,300)#是
                turtle.left(120)
                turtle.pendown()
                turtle.forward(100)
                turtle.right(180)
                turtle.forward(100)
                turtle.right(90)
                turtle.forward(80)
                turtle.right(90)
                turtle.forward(100)
                turtle.penup()
                turtle.goto(-200,250)
                turtle.left(90)
                turtle.pendown()
                turtle.forward(80)
                turtle.penup()
                turtle.goto(-200,200)
                turtle.pendown()
                turtle.forward(80)
                turtle.penup()
                turtle.goto(-280,150)
                turtle.pendown()
                turtle.forward(240)
                turtle.penup()
                turtle.goto(-160,150)
                turtle.pendown()
                turtle.right(90)
                turtle.forward(100)
                turtle.penup()
                turtle.goto(-160,100)
                turtle.pendown()
                turtle.left(90)
                turtle.forward(60)
                turtle.penup()
                turtle.goto(-200,100)
                turtle.pendown()
                turtle.right(120)
                turtle.forward(100)
                turtle.right(180)
                turtle.forward(50)
                turtle.right(70)
                turtle.forward(200)
                turtle.penup()
                turtle.goto(100,300)#伞
                turtle.pendown()
                turtle.right(125)
                turtle.forward(200)
                turtle.right(180)
                turtle.forward(200)
                turtle.right(90)
                turtle.forward(200)
                turtle.penup()
                turtle.goto(30,200)
                turtle.pendown()
                turtle.forward(60)
                turtle.penup()
                turtle.goto(175,200)
                turtle.pendown()
                turtle.right(90)
                turtle.forward(60)
                turtle.penup()
                turtle.goto(0,120)
                turtle.left(135)
                turtle.pendown()
                turtle.forward(200)
                turtle.penup()
                turtle.goto(100,250)
                turtle.right(90)
                turtle.pendown()
                turtle.forward(250)
                turtle.penup()
                turtle.goto(420,300)#兵
                turtle.right(75)
                turtle.pendown()
                turtle.forward(100)
                turtle.left(75)
                turtle.forward(150)
                turtle.right(180)
                turtle.forward(75)
                turtle.right(90)
                turtle.forward(150)
                turtle.right(180)
                turtle.forward(60)
                turtle.left(90)
                turtle.forward(75)
                turtle.penup()
                turtle.right(90)
                turtle.forward(180)
                turtle.right(180)
                turtle.pendown()
                turtle.forward(300)
                turtle.penup()
                turtle.goto(340,100)
                turtle.right(120)
                turtle.pendown()
                turtle.forward(80)
                turtle.penup()
                turtle.goto(430,100)
                turtle.left(60)
                turtle.pendown()
                turtle.forward(80)
                m=tkinter.messagebox.showinfo('CONGRATULATIONS!','恭喜获得称号：伞兵！')
                wait_event=threading.Event()
                if m:
                    turn=0
                    for i in range(100):
                        turn+=1
                        wait_event.wait(0.05)
                        print('伞兵'+str(turn)+'号卢本伟准备就绪！')
            except:
                pass
    def choose_no(self):
        self.choose_no_turn=self.choose_no_turn+1
        if self.choose_no_turn<10:
            objects=('unknown','untrue','timeout')
            choice_of_windows=random.choice(objects)
            if choice_of_windows=='unknown':
                tkinter.messagebox.showerror(title='ERROR!',message='未知性错误！')
            elif choice_of_windows=='untrue':
                tkinter.messagebox.showerror(title='ERROR!',message='你选择的选项不属实！')
            elif choice_of_windows=='timeout':
                time.sleep(5)
                tkinter.messagebox.showwarning(title='ERROR!',message='加载时间过长！')
        elif self.choose_no_turn==10:
            window_distanse_up=0
            window_distanse_left=0
            window_geometry='300x100'
            for i in range(26):
                strings='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={[}]\\|;:\'\",.<>/?！￥（）——｛｝【】、；：‘’“”，。《》？·~`'
                salt1=''
                salt2=''
                for i in range(random.randint(3,20)):
                    salt1+=random.choice(strings)
                for i in range(30):
                    salt2+=random.choice(strings)
                tk_error=tkinter.Tk()
                window_geometry='300x100+'+str(window_distanse_left)+"+"+str(window_distanse_up)
                tk_error.geometry(window_geometry)
                window_distanse_up=window_distanse_up+50
                window_distanse_left=window_distanse_left+90
                tk_error.configure(bg='red')
                tk_error.title(salt1)
                lab_error=tkinter.Label(tk_error,text=salt2,bg='red')
                lab_error.pack()
            window_distanse_up=0
            window_distanse_left=2260
            window_geometry='300x100'
            for i in range(26):
                strings2='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={[}]\\|;:\'\",.<>/?！￥（）——｛｝【】、；：‘’“”，。《》？·~`'
                salt11=''
                salt22=''
                for i in range(random.randint(3,20)):
                    salt11+=random.choice(strings2)
                for i in range(30):
                    salt22+=random.choice(strings2)
                tk_error2=tkinter.Tk()
                window_geometry='300x100+'+str(window_distanse_left)+"+"+str(window_distanse_up)
                tk_error2.geometry(window_geometry)
                window_distanse_up=window_distanse_up+50
                window_distanse_left=window_distanse_left-90
                tk_error2.configure(bg='red')
                tk_error2.title(salt11)
                lab_error2=tkinter.Label(tk_error2,text=salt22,bg='red')
                lab_error2.pack()
        elif self.choose_no_turn==11:
            def ranstr(num):
                strings='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
                salt=''
                for i in range(num):
                    salt+=random.choice(strings)
                return salt
            salt=ranstr(random.randint(20000,100000))
            print(salt)
        elif self.choose_no_turn==12:
            for i in range(100):
                print('我警告你!给我选是！否则你电脑没了！')
        else:
            strings='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{;}\|:\'\",.<>/?`~，。《》、？！￥……【】｛｝、；：‘’“”·¿¡〖〗︻︼「」—ˉ﹫〃‖☰≈≠≤≥∶∞∧∨∑∏∪∩∈∵∴⊥∥∠⌒⊙√°′″〒￠￡₴₰¢₤¥₳₲₪₵Ұ₣₱฿¤₡₮₭₩₢₥₫₦złčर₹ƒ₸€ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζνξοπρσηθικλμτυφχψωАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяāáǎàōóǒòēéěèīíǐìūúǔùǖǘǚǜüêɑńňˆˇ﹖•¨'
            salt=''
            while True:
                salt+=random.choice(strings)
                print(salt)
root=tkinter.Tk()
whqf=Whqf(root)
root.mainloop()