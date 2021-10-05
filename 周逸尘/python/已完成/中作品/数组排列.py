import tkinter
import tkinter.messagebox
import random
###########
class Start_program:
    '程序开始'
    a=()
    b=()
    def __init__(self,parent):
        parent.geometry('400x300')
        parent.title('数组排列')
        lab1=tkinter.Label(parent,text='请输入数组中数的个数')
        lab1.pack()
        ent1=tkinter.Entry(parent)
        ent1.pack()
        lab2=tkinter.Label(parent,text='请输入数组最大值')
        lab2.pack()
        ent2=tkinter.Entry(parent)
        ent2.pack()
        btn1=tkinter.Button(parent,text='start!',command=lambda:self.start(parent,ent1.get(),ent2.get()))
        btn1.pack()
    def start(self,parent,number1,number2):
        self.a=()
        self.b=()
        turn=0
        ltxt='\0'
        try:
            num1=int(number1)
            num2=int(number2)
            if num1!=float(number1) or num2!=float(number2) or float(number1)<1 or float(number2)<1:
                tkinter.messagebox.showerror(title='ERROR!',message='请输入正整数！')
            elif num1>20 or num2>100000:
                tkinter.messagebox.showerror(title='ERROR!',message='输入数字过大！')
            else:
                for i in range(num1):
                    self.b=(random.randint(0,num2),)
                    self.a=self.a+self.b
                l=sorted(self.a)
                l.sort()
                l=tuple(l)
                for i in range(num1):
                    txt=str(l[turn])
                    ltxt=ltxt+' '+txt
                    turn=turn+1
                le=tkinter.Label(parent,text='你生成的数组是：'+ltxt,font=('华文楷体',11))
                le.pack(anchor='w')
        except ValueError:
            tkinter.messagebox.showerror(title='ERROR!',message='请输入数字！')
###########
root=tkinter.Tk()
start_program=Start_program(root)
###########
root.mainloop()