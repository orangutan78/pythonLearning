import tkinter
##############
class Quit_windows:
    '窗口退出程序'
    def __init__(self,parent):
        parent.geometry('300x200')
        btn_root1=tkinter.Button(parent,text='创建窗口',command=self.start)
        btn_root1.pack()
    def start(self):
        tk=tkinter.Tk()
        tk.geometry('300x200')
        btn_tk1=tkinter.Button(tk,text='quit!',command=lambda:self.退出(tk))
        btn_tk1.pack()
    def 退出(self,parent2):
        parent2.quit()
##############
root=tkinter.Tk()
quit_windows=Quit_windows(root)
##############
root.mainloop()