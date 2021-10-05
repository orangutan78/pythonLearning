import tkinter
###########
class Start_program:
    '程序开始'
    def __init__(self):
        root.geometry('400x300')
        root.title('')
        root.configure(bg='white')
        lab1=tkinter.Label(root,text='',bg='white')
        lab1.pack()
        ent1=tkinter.Entry(root,bg='white')
        ent1.pack()
        btn1=tkinter.Button(root,text='',command=lambda:self.start(ent1.get()),bg='white')
        btn1.pack()
    def start(self,ent_get):
        pass
###########
root=tkinter.Tk()
start_program=Start_program()
###########
root.mainloop()