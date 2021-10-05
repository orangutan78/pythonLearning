import tkinter
###########
###########
def start():
    pass
###########
root=tkinter.Tk()
root.geometry('400x300')
root.title('')
lab1=tkinter.Label(root,text='')
lab1.pack()
btn1=tkinter.Button(root,text='',command=start)
btn1.pack()
###########
root.mainloop()