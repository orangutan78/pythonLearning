from tkinter import *
from tkinter.messagebox import*
def judge(aqi):
    global root
    global l
    l.pack_forget()
    try:
        aqi=float(aqi)
        if aqi>=0:
            if aqi<=50:
                l=Label(root,text='空气质量优，各类人群可户外活动',bg='green',fg='white')
            elif aqi<=100:
                l=Label(root,text='空气质量良，少数敏感人群减少户外活动',bg='yellow')
            elif aqi<=150:
                l=Label(root,text='空气轻度污染，减少长时间户外运动',bg='orange')
            elif aqi<=200:
                l=Label(root,text='空气中度污染，应适量减少户外活动',bg='red')
            elif aqi<=250:
                l=Label(root,text='空气重度污染，一般人减少户外活动',bg='purple',fg='white')
            else:
                l=Label(root,text='空气严重污染，一般人避免户外活动',bg='darkred',fg='white')
            l.pack()
        else:
            showerror('ERROR!','请输入非负数！')
    except TypeError:
        showerror('ERROR!','请输入数字！')
root=Tk()
root.geometry('300x200')
root.configure(bg='lightgoldenrodyellow')
Label(root,text='请输入AQI指数',bg='lightgoldenrodyellow').pack()
e=Entry(root)
e.pack()
Button(root,command=lambda:judge(e.get()),bg='lightgoldenrodyellow',text='转换').pack()
l=Label(root)
root.mainloop()