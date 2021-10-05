import tkinter
import tkinter.messagebox
############
class Start_program:
    '程序开始'
    selected_obj=0
    outing_number=0
    label_packed=False
    def __init__(self,parent):
        self.btn1=tkinter.Button(parent)
        parent.geometry('350x200')
        parent.title('calculator')
        parent.configure(bg='cornsilk')
        parent.resizable(width=False,height=False)
        self.outing_label=tkinter.Label(parent)
        lab1=tkinter.Label(parent,text='请输入加数/被减数/乘数/被除数/底数/被开方数',bg='cornsilk')
        lab1.pack()
        self.ent1=tkinter.Entry(parent,bg='darkgray')
        self.ent1.pack()
        lab2=tkinter.Label(parent,text='请输入加数/减数/乘数/除数/指数/根次',bg='cornsilk')
        lab2.place(x=70,y=80)
        self.ent2=tkinter.Entry(parent,bg='darkgray')
        self.ent2.place(x=105,y=105)
        self.btn1=tkinter.Button(parent,text='start!',command=lambda:self.cannot_start(None))
        self.btn1.place(x=155,y=130)
        parent.bind('<Return>',self.cannot_start)
        itv=tkinter.IntVar(parent)
        itv.set(0)
        rdb_plus=tkinter.Radiobutton(parent,text='加',variable=itv,value=1,
                                     command=lambda:self.plus_selected(\
                                         parent),bg='cornsilk')
        rdb_subtract=tkinter.Radiobutton(parent,text='减',variable=itv,value=2,
                                         command=lambda:self.subtract_selected(\
                                             parent),bg='cornsilk')
        rdb_time=tkinter.Radiobutton(parent,text='乘',variable=itv,value=3,
                                     command=lambda:self.time_selected(\
                                         parent),bg='cornsilk')
        rdb_devide=tkinter.Radiobutton(parent,text='除',variable=itv,value=4,
                                       command=lambda:self.divide_selected(\
                                           parent),bg='cornsilk')
        rdb_square=tkinter.Radiobutton(parent,text='乘方',variable=itv,value=5,
                                       command=lambda:self.square_selected(\
                                           parent),bg='cornsilk')
        rdb_squareRoot=tkinter.Radiobutton(parent,text='开根',variable=itv,value=6,
                                       command=lambda:self.squareRoot_selected(\
                                           parent),bg='cornsilk')
        rdb_plus.place(x=25,y=55)
        rdb_subtract.place(x=75,y=55)
        rdb_time.place(x=125,y=55)
        rdb_devide.place(x=175,y=55)
        rdb_square.place(x=225,y=55)
        rdb_squareRoot.place(x=275,y=55)
        self.btn2=tkinter.Button(parent,text='start!',
                                 command=lambda:self.start(self.ent1.get(),self.ent2.get(),parent))
    def start(self,ent1_get,ent2_get,parent):
        try:
            if ent1_get=='\0' or ent2_get=='\0':
                tkinter.messagebox.showerror('ERROR!','请输入内容！')
            else:
                first_number=float(ent1_get)
                second_number=float(ent2_get)
                if float(int(first_number))==first_number:
                    first_number=int(first_number)
                if float(int(second_number))==second_number:
                    second_number=int(second_number)
                cal_kind=self.selected_obj
                if cal_kind==1:
                    self.plus(parent,first_number,second_number)
                elif cal_kind==2:
                    self.subtract(parent,first_number,second_number)
                elif cal_kind==3:
                    self.time(parent,first_number,second_number)
                elif cal_kind==4:
                    self.divide(parent,first_number,second_number)
                elif cal_kind==5:
                    self.square(parent,first_number,second_number)
                else:
                    self.squareRoot(parent,first_number,second_number)
        except ValueError:
            tkinter.messagebox.showerror('ERROR!','请输入数字！')
    def cannot_start(self,event):
        tkinter.messagebox.showerror('ERROR!','请选择运算方式！')
    def plus_selected(self,parent):
        self.selected_obj=1
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn2.place(x=155,y=130)
        parent.unbind('<Return>')
        parent.bind('<Return>',lambda event:self.start(self.ent1.get(),self.ent2.get(),parent))
    def subtract_selected(self,parent):
        self.selected_obj=2
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn2.place(x=155,y=130)
        parent.unbind('<Return>')
        parent.bind('<Return>',lambda event:self.start(self.ent1.get(),self.ent2.get(),parent))
    def time_selected(self,parent):
        self.selected_obj=3
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn2.place(x=155,y=130)
        parent.unbind('<Return>')
        parent.bind('<Return>',lambda event:self.start(self.ent1.get(),self.ent2.get(),parent))
    def divide_selected(self,parent):
        self.selected_obj=4
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn2.place(x=155,y=130)
        parent.unbind('<Return>')
        parent.bind('<Return>',lambda event:self.start(self.ent1.get(),self.ent2.get(),parent))
    def square_selected(self,parent):
        self.selected_obj=5
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn2.place(x=155,y=130)
        parent.unbind('<Return>')
        parent.bind('<Return>',lambda event:self.start(self.ent1.get(),self.ent2.get(),parent))
    def squareRoot_selected(self,parent):
        self.selected_obj=6
        self.btn1.place_forget()
        self.btn2.place_forget()
        self.btn2.place(x=155,y=130)
        parent.unbind('<Return>')
        parent.bind('<Return>',lambda event:self.start(self.ent1.get(),self.ent2.get(),parent))
        self.turn=1
    def plus(self,parent,first_number,second_number):
        self.outing_number=first_number+second_number
        tp=tuple(str(first_number)+str(second_number)+str(self.outing_number))
        length=len(tp)
        if length>26:
            tkinter.messagebox.showerror('ERROR!','数字过长！')
        else:
            self.label_packed=False
            if int(self.outing_number)==self.outing_number:
                self.outing_number=int(self.outing_number)
            self.strv_p=tkinter.StringVar()
            self.strv_p.set(str(first_number)+'+'+str(second_number)+'='+str(self.outing_number))
            parent.update()
            self.outing_label.place_forget()
            self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
            self.outing_label.place(y=160)
    def subtract(self,parent,first_number,second_number):
        self.outing_number=first_number-second_number
        tp=tuple(str(first_number)+str(second_number)+str(self.outing_number))
        length=len(tp)
        if length>26:
            tkinter.messagebox.showerror('ERROR!','数字过长！')
        else:
            self.label_packed=False
            if int(self.outing_number)==self.outing_number:
                self.outing_number=int(self.outing_number)
            self.strv_p=tkinter.StringVar()
            self.strv_p.set(str(first_number)+'-'+str(second_number)+'='+str(self.outing_number))
            parent.update()
            self.outing_label.place_forget()
            self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
            self.outing_label.place(y=160)
    def time(self,parent,first_number,second_number):
        self.outing_number=first_number*second_number
        tp=tuple(str(first_number)+str(second_number)+str(self.outing_number))
        length=len(tp)
        if length>26:
            tkinter.messagebox.showerror('ERROR!','数字过长！')
        else:
            self.label_packed=False
            if int(self.outing_number)==self.outing_number:
                self.outing_number=int(self.outing_number)
            self.strv_p=tkinter.StringVar()
            self.strv_p.set(str(first_number)+'×'+str(second_number)+'='+str(self.outing_number))
            parent.update()
            self.outing_label.place_forget()
            self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
            self.outing_label.place(y=160)
    def divide(self,parent,first_number,second_number):
        if second_number!=0:
            self.outing_number=first_number/second_number
            tp=tuple(str(first_number)+str(second_number)+str(self.outing_number))
            length=len(tp)
            if length>26:
                tp_front=tuple(str(first_number)+str(second_number))
                length_front=len(tp_front)+2
                if length_front>=26:
                    tkinter.messagebox.showerror('ERROR!','数字过长！')
                else:
                    after=26-length_front
                    divided_num=self.outing_number/(10**after)
                    about_num=divided_num*(10**after)
                    int_num=int(self.outing_number)
                    if about_num<int_num:
                        tkinter.messagebox.showerror('ERROR!','数字过长！')
                    else:
                        self.outing_number=about_num
                        self.strv_p=tkinter.StringVar()
                        self.strv_p.set(str(first_number)+'÷'+str(second_number)+'='+str(self.outing_number))
                        parent.update()
                        self.outing_label.place_forget()
                        self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
                        self.outing_label.place(y=160)
            else:
                self.label_packed=False
                if int(self.outing_number)==self.outing_number:
                    self.outing_number=int(self.outing_number)
                self.strv_p=tkinter.StringVar()
                self.strv_p.set(str(first_number)+'÷'+str(second_number)+'='+str(self.outing_number))
                parent.update()
                self.outing_label.place_forget()
                self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
                self.outing_label.place(y=160)
        else:
            tkinter.messagebox.showerror('ERROR!','除数不能为零！')
    def square(self,parent,first_number,second_number):
        if second_number>100 and first_number>10:
            tkinter.messagebox.showerror('ERROR!','数字过大！')
        else:
            self.outing_number=first_number**second_number
            tp=tuple(str(first_number)+str(second_number)+str(self.outing_number))
            length=len(tp)
            if length>26:
                tkinter.messagebox.showerror('ERROR!','数字过长！')
            else:
                self.label_packed=False
                if int(self.outing_number)==self.outing_number:
                    self.outing_number=int(self.outing_number)
                self.strv_p=tkinter.StringVar()
                self.strv_p.set(str(first_number)+'^'+str(second_number)+'='+str(self.outing_number))
                parent.update()
                self.outing_label.place_forget()
                self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
                self.outing_label.place(y=160)
    def squareRoot(self,parent,b,way):
        a=0
        zero=0
        subtract_or_not=False#有无变号
        add_turn=0
        while True:
            try:
                squared_a=a**way
                if round(squared_a,10)<b:#+
                    print(a)
                    if add_turn==-1:
                        subtract_or_not=True
                    else:
                        subtract_or_not=False
                    if subtract_or_not==False:#不变（加）
                        a+=1/(10**zero)
                        add_turn=1
                    else:#变
                        if add_turn==-1:#减
                            zero+=1
                            a+=1/(10**zero)
                            subtract_or_not=True
                            add_turn=1
                        else:#加
                            a+=1/(10**zero)
                            add_turn=1
                            subtract_or_not=False
                elif round(squared_a,10)>b:#-
                    print(a)
                    if add_turn==1:
                        subtract_or_not=True
                    else:
                        subtract_or_not=False
                    if subtract_or_not==False:
                        a-=1/(10**zero)
                        add_turn=-1
                    else:#变
                        if add_turn==1:
                            zero+=1
                            a-=1/(10**zero)
                            subtract_or_not=True
                            add_turn=-1
                        else:
                            a-=1/(10**zero)
                            add_turn=-1
                            subtract_or_not=False
                else:
                    print(a)
                    if int(a)==a:
                        a=int(a)
                    break
            except OverflowError:
                tkinter.messagebox.showerror('ERROR!','数字过大！')
                break
        first_number=b
        second_number=way
        self.outing_number=a
        tp=tuple(str(first_number)+str(second_number)+str(self.outing_number))
        length=len(tp)
        if length>26:
            tp_front=tuple(str(first_number)+str(second_number))
            length_front=len(tp_front)+2
            if length_front>=26:
                tkinter.messagebox.showerror('ERROR!','数字过长！')
            else:
                after=26-length_front
                divided_num=self.outing_number/(10**after)
                about_num=divided_num*(10**after)
                int_num=int(self.outing_number)
                if about_num<int_num:
                    tkinter.messagebox.showerror('ERROR!','数字过长！')
                else:
                    self.outing_number=about_num
                    self.strv_p=tkinter.StringVar()
                    self.strv_p.set(str(first_number)+'√'+str(second_number)+'='+str(self.outing_number))
                    parent.update()
                    self.outing_label.place_forget()
                    self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
                    self.outing_label.place(y=160)
        else:
            self.label_packed=False
            if int(self.outing_number)==self.outing_number:
                self.outing_number=int(self.outing_number)
            self.strv_p=tkinter.StringVar()
            self.strv_p.set(str(first_number)+'√'+str(second_number)+'='+str(self.outing_number))
            parent.update()
            self.outing_label.place_forget()
            self.outing_label=tkinter.Label(parent,textvariable=self.strv_p,bg='cornsilk',font=('微软雅黑',16))
            self.outing_label.place(y=160)
root=tkinter.Tk()
start_program=Start_program(root)
############
root.mainloop()
