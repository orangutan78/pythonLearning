from tkinter import *
root=Tk()
b=Button(root,text='FLAT',relief=FLAT)
b.pack()
b=Button(root,text='SUNKEN',relief=SUNKEN)
b.pack()
b=Button(root,text='RAISED',relief=RAISED)
b.pack()
b=Button(root,text='GROOVE',relief=GROOVE)
b.pack()
b=Button(root,text='RIDGE',relief=RIDGE)
b.pack()
b=Button(root,text='SOLID',relief=SOLID)
b.pack()
root.mainloop()