from tkinter import *
from cv2 import *
from PIL import Image
from time import time
#from PIL import ImageGrab
class faceAI:
    '人脸识别'
    def __init__(self):
        self.lab=Label(root)
        root.configure(bg='lightgoldenrodyellow')
        root.geometry('300x200')
        #root.resizable(0,0)
        root.title('人脸识别')
        Button(root,text='拍照',command=self.take_photo,bg='lightgoldenrodyellow').pack()
    def take_photo(self):
        self.lab.pack_forget()
        cap=VideoCapture(0,CAP_DSHOW)
        ret,frame=cap.read()
        now_time=int(time())
        imwrite(str(now_time)+'.jpg',frame)
        cap.release()
        pil_image=Image.open(str(now_time)+'.jpg')
        pil_image=pil_image.resize((200,150))
        pil_image.save(str(now_time)+'.ppm')
        photo=PhotoImage(file=str(now_time)+'.ppm')
        self.lab=Label(root,image=photo)
        self.lab.image=photo
        self.lab.pack()
root=Tk()
faceAI()
root.mainloop()