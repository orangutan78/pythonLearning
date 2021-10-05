import tkinter
import random
import tkinter.messagebox
import pickle
###########
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
        parent.state('icon')
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
            f=open('D:\\学习\\pythonLearning\\周逸尘\\python\\已完成\\大作品\\random object.roj.txt','rb')
            f_load=pickle.load(f)
            self.open_list=f_load
            n=0
        except FileNotFoundError:
            tkinter.messagebox.showerror(title='ERROR!',message='在桌面上找不到\nrandom object.roj.txt!')
        except EOFError:
            tkinter.messagebox.showerror(title='ERROR!',message='random object.roj.txt\n内容为空!')
        except pickle.UnpicklingError:
            tkinter.messagebox.showerror(title='ERROR!',message='random object.roj.txt\n内容被篡改!')
        except:
            tkinter.messagebox.showerror(title='ERROR!',message='未知错误!')
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
    def create_new_file(self,name):
        if self.random_word==() or self.random_word==('\0',) or name==None or name=='\0':
            tkinter.messagebox.showerror(title='ERROR!',message='请添加内容!')
        else:
            try:
                f_show=open('D:\\学习\\pythonLearning\\周逸尘\\python\\已完成\\大作品\\random object.roj.txt','rb')
                f_in=pickle.load(f_show)
                self.open_list=f_in
                self.lst=[name,self.random_word]
                self.big_list=self.open_list+[self.lst]
                f_show.close()
                f_write=open('D:\\学习\\pythonLearning\\周逸尘\\python\\已完成\\大作品\\random object.roj.txt','wb')
                pickle.dump(self.big_list,f_write)
                f_write.close()
                f_read=open('D:\\学习\\pythonLearning\\周逸尘\\python\\已完成\\大作品\\random object.roj.txt','rb')
                f_out=pickle.load(f_read)
                print(f_out)
                f_read.close()
            except FileNotFoundError:
                tkinter.messagebox.showerror(title='ERROR!',message='在桌面上找不到\nrandom object.roj.txt!')
            except EOFError:
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
#D:\学习\pythonLearning\周逸尘\python\未完成\正在做\工具箱之random anything\\random object.roj.txt
