# -*- coding:utf-8 -*-
import tkinter
import tkinter.messagebox
import turtle
import random
import time
import math
import pickle
import threading
from tkinter.constants import W
class Start_program:
    '程序开始'
    def __init__(self):
        root.geometry('402x278')
        root.title('工具箱')
        root.configure(bg='mistyrose')
        root.resizable(False,False)
        btn1=tkinter.Button(root,text='进制转换',command=self.change_numbers,bg='white',relief=tkinter.GROOVE,width=20,height=10)
        btn1.place(x=0,y=0)
        btn2=tkinter.Button(root,text='取随机值',command=self.random_anything,bg='lightgoldenrodyellow',relief=tkinter.GROOVE,width=20,height=10)
        btn2.place(x=148,y=0)
        btn3=tkinter.Button(root,text='计算器',command=self.calculator,bg='cornsilk',relief=tkinter.GROOVE,width=30,height=5)
        btn3.place(x=0,y=181)
        btn4=tkinter.Button(root,text='计时器',command=self.timer,bg='lightgray',relief=tkinter.GROOVE,width=25,height=5)
        btn4.place(x=218,y=181)
        btn5=tkinter.Button(root,text='计算阶乘',command=self.factorial,bg='lavender',relief=tkinter.GROOVE,width=14,height=5)
        btn5.place(x=295)
        btn6=tkinter.Button(root,text='判断质数合数',command=self.judge,bg='thistle',relief=tkinter.GROOVE,width=14,pady=30)
        btn6.place(x=295,y=95)
        root.bind('<Control-w>',lambda event:self.芜湖起飞(root))
    def change_numbers(self):
        class Change:
            '程序开始'
            def __init__(self,parent):
                parent.geometry('300x800')
                parent.title('进制转换')
                parent.configure(bg='white')
                lab1=tkinter.Label(parent,text='请输入要开始转换的数',bg='white')
                lab1.pack()
                ent1=tkinter.Entry(parent,bg='lightgray')
                ent1.pack()
                lab3=tkinter.Label(parent,text='请输入你所输数的进制',bg='white')
                lab3.pack()
                ent3=tkinter.Entry(parent,bg='lightgray')
                ent3.pack()
                lab2=tkinter.Label(parent,text='请输入你要转换的进制',bg='white')
                lab2.pack()
                ent2=tkinter.Entry(parent,bg='lightgray')
                ent2.pack()
                btn1=tkinter.Button(parent,text='转换',command=lambda:self.start(parent,ent1.get(),ent2.get(),ent3.get()),bg='white')
                btn1.pack()
            def start(self,parent,num_begin,cal_way,cal_way_from):
                try:
                    int(num_begin)
                    cal_way=float(cal_way)
                    if int(cal_way)!=cal_way:
                        tkinter.messagebox.showerror('ERROR!','请输入整数！')
                    elif cal_way<2 or cal_way>36 or int(cal_way_from)<2 or int(cal_way_from)>36:
                        tkinter.messagebox.showerror('ERROR!','进制只能在2至36范围内！')
                    else:
                        dic_chinese={2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十',11:'十一',12:'十二',13:'十三',14:'十四',15:'十五',16:'十六',17:'十七',18:'十八',19:'十九',20:'二十',21:'二十一',22:'二十二',23:'二十三',24:'二十四',25:'二十五',26:'二十六',27:'二十七',28:'二十八',29:'二十九',30:'三十',31:'三十一',32:'三十二',33:'三十三',34:'三十四',35:'三十五',36:'三十六'}
                        num_out=0
                        one_num=0
                        count_turn=0
                        real_one_int=0
                        one_cal=0
                        every_letters=list(num_begin)
                        count_numbers=len(num_begin)
                        plus_or_subtract=1
                        ok_to_pack=True
                        if '-' in num_begin:
                            plus_or_subtract=-1
                            del(every_letters[0])
                            count_numbers-=1
                        for i in range(0,count_numbers):
                            one_num=every_letters[count_numbers-1]
                            if one_num=='A':
                                real_one_int=10
                            elif one_num=='B':
                                real_one_int=11
                            elif one_num=='C':
                                real_one_int=12
                            elif one_num=='D':
                                real_one_int=13
                            elif one_num=='E':
                                real_one_int=14
                            elif one_num=='F':
                                real_one_int=15
                            elif one_num=='G':
                                real_one_int=16
                            elif one_num=='H':
                                real_one_int=17
                            elif one_num=='I':
                                real_one_int=18
                            elif one_num=='J':
                                real_one_int=19
                            elif one_num=='K':
                                real_one_int=20
                            elif one_num=='L':
                                real_one_int=21
                            elif one_num=='M':
                                real_one_int=22
                            elif one_num=='N':
                                real_one_int=23
                            elif one_num=='O':
                                real_one_int=24
                            elif one_num=='P':
                                real_one_int=25
                            elif one_num=='Q':
                                real_one_int=26
                            elif one_num=='R':
                                real_one_int=27
                            elif one_num=='S':
                                real_one_int=28
                            elif one_num=='T':
                                real_one_int=29
                            elif one_num=='U':
                                real_one_int=30
                            elif one_num=='V':
                                real_one_int=31
                            elif one_num=='W':
                                real_one_int=32
                            elif one_num=='X':
                                real_one_int=33
                            elif one_num=='Y':
                                real_one_int=34
                            elif one_num=='Z':
                                real_one_int=35
                            else:
                                try:
                                    if num_begin=='\0':
                                        tkinter.messagebox.showerror('ERROR!','请输入内容！')
                                    else:
                                        if one_num=='1' or one_num=='2' or one_num=='3' or one_num=='4' or one_num=='5' or one_num=='6' or one_num=='7' or one_num=='8' or one_num=='9' or one_num=='0':
                                            real_one_int=int(one_num)
                                        else:
                                            tkinter.messagebox.showerror('ERROR!','使用了不支持的字符！\n只能输入数字及大写英文字母！')
                                except:
                                    pass
                                real_one_int=int(one_num)
                            if real_one_int>=int(cal_way_from):
                                tkinter.messagebox.showerror('ERROR!','使用了该进制不支持的编码！')
                                ok_to_pack=False
                                break
                            else:
                                one_cal=real_one_int*(int(cal_way_from)**count_turn)
                                num_out+=one_cal
                                count_numbers-=1
                                count_turn+=1
                        if num_out>=999999999999999:
                            tkinter.messagebox.showerror('ERROR!','输入的数10进制绝对值\n不得大于999999999999998！')
                        else:
                            num=num_out
                            turn=0
                            max_number=0
                            square_turn=0
                            num_end=''
                            one_int=None
                            int_one_int=0
                            while True:
                                if num>cal_way**turn:
                                    turn+=1
                                elif num==cal_way**turn:
                                    num_end=10**turn
                                    break
                                else:
                                    square_turn=turn-1
                                    max_number=cal_way**square_turn
                                    one_int=str(math.floor(num/max_number))
                                    if one_int=='10':
                                        one_int='A'
                                    elif one_int=='11':
                                        one_int='B'
                                    elif one_int=='12':
                                        one_int='C'
                                    elif one_int=='13':
                                        one_int='D'
                                    elif one_int=='14':
                                        one_int='E'
                                    elif one_int=='15':
                                        one_int='F'
                                    elif one_int=='16':
                                        one_int='G'
                                    elif one_int=='17':
                                        one_int='H'
                                    elif one_int=='18':
                                        one_int='I'
                                    elif one_int=='19':
                                        one_int='J'
                                    elif one_int=='20':
                                        one_int='K'
                                    elif one_int=='21':
                                        one_int='L'
                                    elif one_int=='22':
                                        one_int='M'
                                    elif one_int=='23':
                                        one_int='N'
                                    elif one_int=='24':
                                        one_int='O'
                                    elif one_int=='25':
                                        one_int='P'
                                    elif one_int=='26':
                                        one_int='Q'
                                    elif one_int=='27':
                                        one_int='R'
                                    elif one_int=='28':
                                        one_int='S'
                                    elif one_int=='29':
                                        one_int='T'
                                    elif one_int=='30':
                                        one_int='U'
                                    elif one_int=='31':
                                        one_int='V'
                                    elif one_int=='32':
                                        one_int='W'
                                    elif one_int=='33':
                                        one_int='X'
                                    elif one_int=='34':
                                        one_int='Y'
                                    elif one_int=='35':
                                        one_int='Z'
                                    for i in range(-1,square_turn):
                                        num_end+=one_int
                                        square_turn-=1
                                        if one_int=='A':
                                            int_one_int=10
                                        elif one_int=='B':
                                            int_one_int=11
                                        elif one_int=='C':
                                            int_one_int=12
                                        elif one_int=='D':
                                            int_one_int=13
                                        elif one_int=='E':
                                            int_one_int=14
                                        elif one_int=='F':
                                            int_one_int=15
                                        elif one_int=='G':
                                            int_one_int=16
                                        elif one_int=='H':
                                            int_one_int=17
                                        elif one_int=='I':
                                            int_one_int=18
                                        elif one_int=='J':
                                            int_one_int=19
                                        elif one_int=='K':
                                            int_one_int=20
                                        elif one_int=='L':
                                            int_one_int=21
                                        elif one_int=='M':
                                            int_one_int=22
                                        elif one_int=='N':
                                            int_one_int=23
                                        elif one_int=='O':
                                            int_one_int=24
                                        elif one_int=='P':
                                            int_one_int=25
                                        elif one_int=='Q':
                                            int_one_int=26
                                        elif one_int=='R':
                                            int_one_int=27
                                        elif one_int=='S':
                                            int_one_int=28
                                        elif one_int=='T':
                                            int_one_int=29
                                        elif one_int=='U':
                                            int_one_int=30
                                        elif one_int=='V':
                                            int_one_int=31
                                        elif one_int=='W':
                                            int_one_int=32
                                        elif one_int=='X':
                                            int_one_int=33
                                        elif one_int=='Y':
                                            int_one_int=34
                                        elif one_int=='Z':
                                            int_one_int=35
                                        else:
                                            int_one_int=int(one_int)
                                        num-=int_one_int*max_number
                                        max_number=cal_way**square_turn
                                        one_int=str(math.floor(num/max_number))
                                        if one_int=='10':
                                            one_int='A'
                                        elif one_int=='11':
                                            one_int='B'
                                        elif one_int=='12':
                                            one_int='C'
                                        elif one_int=='13':
                                            one_int='D'
                                        elif one_int=='14':
                                            one_int='E'
                                        elif one_int=='15':
                                            one_int='F'
                                        elif one_int=='16':
                                            one_int='G'
                                        elif one_int=='17':
                                            one_int='H'
                                        elif one_int=='18':
                                            one_int='I'
                                        elif one_int=='19':
                                            one_int='J'
                                        elif one_int=='20':
                                            one_int='K'
                                        elif one_int=='21':
                                            one_int='L'
                                        elif one_int=='22':
                                            one_int='M'
                                        elif one_int=='23':
                                            one_int='N'
                                        elif one_int=='24':
                                            one_int='O'
                                        elif one_int=='25':
                                            one_int='P'
                                        elif one_int=='26':
                                            one_int='Q'
                                        elif one_int=='27':
                                            one_int='R'
                                        elif one_int=='28':
                                            one_int='S'
                                        elif one_int=='29':
                                            one_int='T'
                                        elif one_int=='30':
                                            one_int='U'
                                        elif one_int=='31':
                                            one_int='V'
                                        elif one_int=='32':
                                            one_int='W'
                                        elif one_int=='33':
                                            one_int='X'
                                        elif one_int=='34':
                                            one_int='Y'
                                        elif one_int=='35':
                                            one_int='Z'
                                    break
                            if plus_or_subtract==-1:
                                num_end='-'+num_end
                            if ok_to_pack:
                                lab_end=tkinter.Label(parent,text=str(num_begin)+'（'+str(dic_chinese[int(cal_way_from)])+'进制）'+'='+str(num_end)+'（'+str(dic_chinese[cal_way])+'进制）',bg='white')
                                lab_end.pack()
                except ValueError:
                    tkinter.messagebox.showerror('ERROR!','请输入整数！')
    
    ###########
        root=tkinter.Tk()
        change=Change(root)
    ###########
        root.mainloop()
    def random_anything(self):
        class Start_program:
            '程序开始'
            acrnum=0
            is_selected=-1
            random_word=()
            big_list=[]
            open_list=[]
            lst=[]
            def __init__(self,parent):
                self.lab_num4=tkinter.Label()
                self.lab_str2=tkinter.Label()
                parent.geometry('300x200+200+200')
                parent.title('随机值')
                parent.configure(bg='lightgoldenrodyellow')
                parent.resizable(False,False)
                lab1=tkinter.Label(parent,text='请选择你要取的随机项目',bg='lightgoldenrodyellow')
                lab1.pack()
                btn1=tkinter.Button(parent,text='抽取随机数',command=lambda:self.start(1,parent),bg='aquamarine')
                btn1.pack()
                btn2=tkinter.Button(parent,text='抽取随机字符',command=lambda:self.start(2,parent),bg='lightcyan')
                btn2.pack()
            def start(self,object,parent):
                if object==1:
                    self.is_selected=-1
                    win_num=tkinter.Tk()
                    win_num.geometry('300x200+200+200')
                    win_num.title('抽取随机数')
                    win_num.configure(bg='aquamarine')
                    win_num.resizable(False,False)
                    lab_num1=tkinter.Label(win_num,text='请输入最小值',bg='aquamarine')
                    lab_num1.pack()
                    ent_num1=tkinter.Entry(win_num,bg='lightgray')
                    ent_num1.pack()
                    lab_num2=tkinter.Label(win_num,text='请输入最大值',bg='aquamarine')
                    lab_num2.pack()
                    ent_num2=tkinter.Entry(win_num,bg='lightgray')
                    ent_num2.pack()
                    lab_num3=tkinter.Label(win_num,text='请选择保留小数位数，方可跳出按钮',bg='aquamarine')
                    lab_num3.pack()
                    itv=tkinter.IntVar()
                    itv.set(0)
                    rdb_num0=tkinter.Radiobutton(win_num,text="0",variable=itv,value=0,command=lambda:self.selected(0,win_num,ent_num1,ent_num2),bg='aquamarine')
                    rdb_num1=tkinter.Radiobutton(win_num,text="1",variable=itv,value=1,command=lambda:self.selected(1,win_num,ent_num1,ent_num2),bg='aquamarine')
                    rdb_num2=tkinter.Radiobutton(win_num,text="2",variable=itv,value=2,command=lambda:self.selected(2,win_num,ent_num1,ent_num2),bg='aquamarine')
                    rdb_num3=tkinter.Radiobutton(win_num,text="3",variable=itv,value=3,command=lambda:self.selected(3,win_num,ent_num1,ent_num2),bg='aquamarine')
                    rdb_num4=tkinter.Radiobutton(win_num,text="4",variable=itv,value=4,command=lambda:self.selected(4,win_num,ent_num1,ent_num2),bg='aquamarine')
                    rdb_num5=tkinter.Radiobutton(win_num,text="5",variable=itv,value=5,command=lambda:self.selected(5,win_num,ent_num1,ent_num2),bg='aquamarine')
                    rdb_num0.place(x=30,y=115)
                    rdb_num1.place(x=70,y=115)
                    rdb_num2.place(x=110,y=115)
                    rdb_num3.place(x=150,y=115)
                    rdb_num4.place(x=190,y=115)
                    rdb_num5.place(x=230,y=115)
                elif object==2:
                    win_str=tkinter.Tk()
                    win_str.geometry('300x200+200+200')
                    win_str.title('抽取随机字符')
                    win_str.configure(bg='lightcyan')
                    win_str.resizable(False,False)
                    lab_str1=tkinter.Label(win_str,text='请添加字符',bg='lightcyan')
                    lab_str1.pack()
                    ent_str1=tkinter.Entry(win_str,bg='lightgray')
                    ent_str1.pack()
                    btn_str1=tkinter.Button(win_str,text='添加',command=lambda:self.begin_string(ent_str1.get()),bg='cyan')
                    btn_str1.pack()
                    btn_str2=tkinter.Button(win_str,text='从中抽取',command=lambda:self.string_choose(win_str),bg='cyan')
                    btn_str2.pack()
                    lab_str3=tkinter.Label(win_str,text='创建文件：                 .roj(虚拟文件名)',font=('微软雅黑',11),bg='lightcyan')
                    lab_str3.place(y=104)
                    btn_str3=tkinter.Button(win_str,text='创建',command=lambda:self.create_new_file(ent_str2.get()),bg='cyan',padx=8,pady=0,bd=1,font=('微软雅黑',8))
                    btn_str3.place(x=255,y=106)
                    ent_str2=tkinter.Entry(win_str,bg='lightgray',width=10)
                    ent_str2.place(x=72,y=108)
                    lab_str33=tkinter.Label(win_str,text='打开文件：                 .roj(虚拟文件名)',font=('微软雅黑',11),bg='lightcyan')
                    lab_str33.place(y=134)
                    ent_str22=tkinter.Entry(win_str,bg='lightgray',width=10)
                    ent_str22.place(x=72,y=138)
                    btn_str33=tkinter.Button(win_str,text='抽取',command=lambda:self.load_file(ent_str22.get(),win_str),bg='cyan',padx=8,pady=0,bd=1,font=('微软雅黑',8))
                    btn_str33.place(x=255,y=136)
            def selected(self,selected_number,win,ent1,ent2):
                self.is_selected=selected_number
                self.return_float(win,ent1,ent2)
            def return_float(self,win,ent1,ent2):
                btn_num1=tkinter.Button(win,text='开始！',command=lambda:self.begin_float(ent1.get(),ent2.get(),self.is_selected,win),bg='lightgreen')
                btn_num1.place(x=120,y=140)
            def begin_float(self,num1,num2,rdb_get,win):
                try:
                    self.lab_num4.place_forget()
                    int1=float(num1)
                    int2=float(num2)
                    rdmflt=random.uniform(int1,int2)
                    if rdb_get==0:
                        self.acrnum=round(rdmflt)
                        self.acrnum_end=self.acrnum
                    elif rdb_get==1:
                        self.acrnum=round(rdmflt*10)
                        self.acrnum_end=self.acrnum/10
                    elif rdb_get==2:
                        self.acrnum=round(rdmflt*100)
                        self.acrnum_end=self.acrnum/100
                    elif rdb_get==3:
                        self.acrnum=round(rdmflt*1000)
                        self.acrnum_end=self.acrnum/1000
                    elif rdb_get==4:
                        self.acrnum=round(rdmflt*10000)
                        self.acrnum_end=self.acrnum/10000
                    elif rdb_get==5:
                        self.acrnum=round(rdmflt*100000)
                        self.acrnum_end=self.acrnum/100000
                    self.lab_num4=tkinter.Label(win,text='你要取的随机数是：'+str(self.acrnum_end),font=('仿宋',15),bg='aquamarine')
                    self.lab_num4.place(y=170)
                except ValueError:
                    tkinter.messagebox.showerror(title='ERROR!',message='请输入数字!')
            def begin_string(self,ent_get):
                if ent_get==None or ent_get=='\0':
                    tkinter.messagebox.showerror(title='ERROR!',message='请添加内容!')
                else:
                    tp_ent_get=(ent_get,)
                    self.random_word=self.random_word+tp_ent_get
            def string_choose(self,win_str):
                if self.random_word==() or self.random_word==('\0',):
                    tkinter.messagebox.showerror(title='ERROR!',message='请添加内容!')
                else:
                    self.lab_str2.place_forget()
                    choice=random.choice(self.random_word)
                    self.lab_str2=tkinter.Label(win_str,text='你抽取的随机值是：'+choice,font=('仿宋',15),bg='lightcyan')
                    self.lab_str2.place(y=160)
            def load_file(self,name,win_str):
                try:
                    f=open('random object.roj.txt','rb')
                    f_load=pickle.load(f)
                    self.open_list=f_load
                    n=0
                    while True:
                        try:
                            if name in self.open_list[n]:
                                self.lst=self.open_list[n]
                                break
                            else:
                                n+=1
                        except:
                            tkinter.messagebox.showerror(title='ERROR!',message='找不到文件!')
                            break
                    self.lab_str2.place_forget()
                    choice=random.choice(self.lst[1])
                    self.lab_str2=tkinter.Label(win_str,text='你抽取的随机值是：'+choice,font=('仿宋',15),bg='lightcyan')
                    self.lab_str2.place(y=160)
                except FileNotFoundError:
                    tkinter.messagebox.showerror(title='ERROR!',message='找不到\nrandom object.roj.txt!')
                except EOFError or IndexError:
                    tkinter.messagebox.showerror(title='ERROR!',message='random object.roj.txt\n内容为空!')
                except pickle.UnpicklingError:
                    tkinter.messagebox.showerror(title='ERROR!',message='random object.roj.txt\n内容被篡改!')
                except:
                    tkinter.messagebox.showerror(title='ERROR!',message='未知错误!')
            def create_new_file(self,name):
                if self.random_word==() or self.random_word==('\0',) or name==None or name=='\0':
                    tkinter.messagebox.showerror(title='ERROR!',message='请添加内容!')
                else:
                    try:
                        f_show=open('random object.roj.txt','rb')
                        f_in=pickle.load(f_show)
                        self.open_list=f_in
                        self.lst=[name,self.random_word]
                        self.big_list=self.open_list+[self.lst]
                        f_show.close()
                        f_write=open('random object.roj.txt','wb')
                        pickle.dump(self.big_list,f_write)
                        f_write.close()
                        f_read=open('random object.roj.txt','rb')
                        #f_out=pickle.load(f_read)
                        #print(f_out)
                        f_read.close()
                    except FileNotFoundError:
                        tkinter.messagebox.showerror(title='ERROR!',message='找不到\nrandom object.roj.txt!')
                    except EOFError or IndexError:
                        tkinter.messagebox.showerror(title='ERROR!',message='random object.roj.txt\n内容为空!')
                    except pickle.UnpicklingError:
                        tkinter.messagebox.showerror(title='ERROR!',message='random object.roj.txt\n内容被篡改!')
                    except:
                        tkinter.messagebox.showerror(title='ERROR!',message='未知错误!')
    ###########
        root=tkinter.Tk()
        start_program=Start_program(root)
    ###########
        root.mainloop()
    def calculator(self):
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
                    self.outing_label=tkinter.Label(parent,text=self.strv_p.get(),bg='cornsilk',font=('微软雅黑',16))
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
                    self.outing_label=tkinter.Label(parent,text=self.strv_p.get(),bg='cornsilk',font=('微软雅黑',16))
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
                    self.outing_label=tkinter.Label(parent,text=self.strv_p.get(),bg='cornsilk',font=('微软雅黑',16))
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
                                self.outing_label=tkinter.Label(parent,text=self.strv_p.get(),bg='cornsilk',font=('微软雅黑',16))
                                self.outing_label.place(y=160)
                    else:
                        self.label_packed=False
                        if int(self.outing_number)==self.outing_number:
                            self.outing_number=int(self.outing_number)
                        self.strv_p=tkinter.StringVar()
                        self.strv_p.set(str(first_number)+'÷'+str(second_number)+'='+str(self.outing_number))
                        parent.update()
                        self.outing_label.place_forget()
                        self.outing_label=tkinter.Label(parent,text=self.strv_p.get(),bg='cornsilk',font=('微软雅黑',16))
                        self.outing_label.place(y=160)
                else:
                    tkinter.messagebox.showerror('ERROR!','除数不能为零！')
            def square(self,parent,first_number,second_number):
                if second_number>100 and first_number>10:
                    tkinter.messagebox.showerror('ERROR!','数字过大！')
                else:
                    try:
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
                            self.outing_label=tkinter.Label(parent,text=self.strv_p.get(),bg='cornsilk',font=('微软雅黑',16))
                            self.outing_label.place(y=160)
                    except OverflowError:
                        tkinter.messagebox.showerror('ERROR!','数字过大！')
            def squareRoot(self,parent,b,way):
                a=0
                zero=0
                subtract_or_not=False#有无变号
                add_turn=0
                while True:
                    try:
                        squared_a=a**way
                        if round(squared_a,10)<b:#+
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
                    self.outing_label=tkinter.Label(parent,text=self.strv_p.get(),bg='cornsilk',font=('微软雅黑',16))
                    self.outing_label.place(y=160)
        root=tkinter.Tk()
        start_program=Start_program(root)
    ############
        root.mainloop()
    def timer(self):
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
                self.lab2=tkinter.Label(root,text=self.var.get(),bg='lightgray',font=('微软雅黑',70))
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
                                self.lab2.place_forget()
                                self.lab2=tkinter.Label(root,text=self.saved_str,bg='lightgray',font=('微软雅黑',70))
                                self.lab2.place(x=10,y=20)
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
                self.saved_str='00:00:00'
                self.is_reset=1
                self.saved_str=str(self.distance_time_minute)+':'+str(self.distance_time_second)+':'+str(self.distance_time_microsecond)
                self.lab2.place_forget()
                self.lab2=tkinter.Label(root,text='00:00:00',bg='lightgray',font=('微软雅黑',70))
                self.lab2.place(x=10,y=20)
                self.root.bind('<space>',self.space_pressed)
                self.root.bind('<KeyPress-c>',self.count)
                self.root.bind('<KeyPress-s>',self.rstt)
    ###########
        root=tkinter.Tk()
        start_program=Start_program()
    ###########
        root.mainloop()
    def factorial(self):
        class Λ:
            '阶乘'
            def __init__(self):
                root.geometry('400x300')
                root.title('计算阶乘')
                root.configure(bg='lavender')
                lab1=tkinter.Label(root,text='请输入要计算阶乘的数',bg='lavender')
                lab1.pack()
                ent1=tkinter.Entry(root,bg='lightgray')
                ent1.pack()
                btn1=tkinter.Button(root,text='计算',command=lambda:self.start(ent1.get(),root),bg='lavender')
                btn1.pack()
            def start(self,ent_get,parent):
                time_turn=1
                time_ok_number=1
                try:
                    num_get=float(ent_get)
                    if num_get>100:
                        tkinter.messagebox.showerror('ERROR!','输入数字过大！')
                    elif num_get!=int(num_get):
                        tkinter.messagebox.showerror('ERROR!','请输入整数！')
                    elif num_get<0:
                        tkinter.messagebox.showerror('ERROR!','请输入正数！')
                    else:
                        int_get=int(num_get)
                        for i in range(int_get):
                            time_ok_number*=time_turn
                            time_turn+=1
                        l=tkinter.Label(root,text=ent_get+'!='+str(time_ok_number),bg='lavender') 
                        l.pack(anchor=W)
                except ValueError:
                    tkinter.messagebox.showerror('ERROR!','请输入数字！')
    ###########
        root=tkinter.Tk()
        λ=Λ()
    ###########
        root.mainloop()
    def judge(self):
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
    def 芜湖起飞(self,root):
        root.destroy()
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
                    smile=tkinter.PhotoImage(file='奸笑.png')
                    a_corner=tkinter.PhotoImage(file='局部.png')
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
                t=False
                self.choose_yes_turn+=1
                if self.choose_yes_turn<2:
                    try:
                        t=True
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
                            self.choose_yes_turn=0
                            turn=0
                            for i in range(99):
                                turn+=1
                                wait_event.wait(0.05)
                                print('伞兵'+str(turn)+'号卢本伟准备就绪！')
                            turtle.bye()
                    except:
                        pass
                        self.choose_yes_turn=0
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
                        wait_event=threading.Event()
                        wait_event.wait(5)
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
###########
root=tkinter.Tk()
start_program=Start_program()
###########
root.mainloop()