from tkinter import*
import tkinter.messagebox
import time
try:
    from pymouse import PyMouse
except:
    tkinter.messagebox.showerror('ERROR!','请下载pymouse模块！')
try:
    import keyboard
except:
    tkinter.messagebox.showerror('ERROR!','请下载pymouse模块！')
pms=PyMouse()
class mouseclick:
    '鼠标连点器'
    Turn=True
    def __init__(self):
        self.parent=root
        self.parent.configure(bg='blanchedalmond')
        self.parent.geometry('300x200')
        self.parent.title('鼠标连点器')
        self.parent.resizable(False,False)
        self.parent.wm_attributes('-topmost',1)
        lab1=Label(self.parent,text='请输入间隔时间',bg='blanchedalmond')
        lab1.pack()
        ent1=Entry(self.parent)
        ent1.pack()
        Label(self.parent,text='按Ctrl-Shift-d开始连点！\n按回车结束连点！',bg='blanchedalmond').pack()
        self.parent.bind('<Control-D>',lambda event:self.start(ent1.get()))
        keyboard.hook(self.end)
    def start(self,e):
        self.Turn=True
        if self.Turn:
            while self.Turn==True:
                try:
                    self.parent.update()
                except:
                    exit()
                mouseX,mouseY=pms.position()
                pms.click(mouseX,mouseY)
                if e!=0:
                    try:
                        e=float(e)
                        time.sleep(e)
                    except:
                        tkinter.messagebox.showerror('ERROR!','请输入数字！')
        else:
            self.Turn=False
        keyboard.hook(self.end)
    def end(self,event):
        if str(event)=='KeyboardEvent(enter down)':
            self.Turn=False
root=Tk()
mouseclick()
root.mainloop()