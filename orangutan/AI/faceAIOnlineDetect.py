import os
from tkinter import *
from cv2 import *
from PIL import Image
from time import time
from tkinter.messagebox import showerror as serror
import base64
from aip import AipFace
from requests.api import options

'''新建aipface的配置'''
""" 你的 APPID AK SK """
APP_ID = '24879858'
API_KEY = 'tOlnrkmLR0hlShhqPj8g1K0F'
SECRET_KEY = 'WLBs7bCmjEilCyV2xIS3S0XZiHGyMFnx'



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
        face_num=0
        self.lab.pack_forget()
        cap=VideoCapture(0,CAP_DSHOW)
        ret,frame=cap.read()
        if ret:
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
            client = AipFace(APP_ID, API_KEY, SECRET_KEY)
            f = open(str(now_time)+'.jpg', 'rb')
            image = base64.b64encode(f.read())
            image64 = str(image,'utf-8')
            image_type = "BASE64"
            faceOptions={}
            faceOptions['max_face_num']=10
            dic=client.detect(image64, image_type,faceOptions)
            if dic['error_code']==0:
                face_num=dic['result']['face_num']
            #print(client.detect(image64, image_type,faceOptions))  # 此处的返回值为人脸的基本检测的数值效果
            print('人脸数量：'+str(face_num))
            f.close()
            self.remove_file(str(now_time)+'.jpg')
        else:
            serror('ERROR!','拍照失败！')
    def remove_file(self,file_name):
        os.remove(str(file_name)+'.ppm')
        os.remove(file_name)
root=Tk()
faceAI()
root.mainloop()




