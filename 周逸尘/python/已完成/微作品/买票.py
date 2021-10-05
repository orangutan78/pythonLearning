import tkinter
import tkinter.messagebox
#############
print('1、任务一\n购票问题：景区门票购买，年龄大于12岁的收全价50元，年龄小于等于12岁的收半价25元。\n输入年龄，根据年龄判断需要收取的门票金额')
#############
a=0
txt=None
#############
def start(x):
    global txt
    try:
        num=int(x)
        if num>12:
            a=50
        if num<=12:
            a=25
        txt='应收'+str(a)+'元'
        l=tkinter.Label(root,text=txt)
        l.pack()
    except ValueError:
        tkinter.messagebox.showerror(title='ERROR!',message='输入错误！')
#############
root=tkinter.Tk()
root.title("请输入年龄")
root.geometry('230x100')
e1=tkinter.Entry(root)
e1.pack()
b1=tkinter.Button(root,text='计算',command=lambda:start(e1.get()))
b1.pack()
#############
tkinter.mainloop()