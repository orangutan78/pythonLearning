import os
from tkinter import *
from cv2 import *
from PIL import Image,ImageTk
from time import time
from tkinter.messagebox import showerror as serror
import base64
from aip import AipFace
'''新建aipface的配置'''
""" 你的 APPID AK SK """
APP_ID = '24879858'
API_KEY = 'tOlnrkmLR0hlShhqPj8g1K0F'
SECRET_KEY = 'WLBs7bCmjEilCyV2xIS3S0XZiHGyMFnx'
class faceAI:
    start_take_photo=False
    '人脸识别'
    def __init__(self):
        root.configure(bg='white')
        root.geometry('300x270')
        root.resizable(0,0)
        root.title('人脸识别')
        tkimg1=PhotoImage(file='camera1.ppm')
        tkimg2=PhotoImage(file='camera2.ppm')
        self.camera_btn=Button(root,image=tkimg1,command=lambda:self.take_photo(tkimg1,tkimg2),bd=0,relief=SUNKEN)
        self.camera_btn.image=tkimg1
        self.camera_btn.place(x=125,y=215)
        self.cpt=VideoCapture(0,CAP_DSHOW+0)
        while not self.start_take_photo:
            try:
                photo=ImageTk.PhotoImage(image=Image.fromarray(cvtColor(self.cpt.read()[1],COLOR_BGR2RGB)).resize((280,210)))
                Label(root,image=photo).place(x=8,y=0)
                root.update()
            except TclError:
                break
            except RuntimeError:
                break
    def take_photo(self,tkimg1,tkimg2):
        self.start_take_photo=True
        root.update()
        self.camera_btn=Button(root,image=tkimg2,bd=0,relief=SUNKEN)
        self.camera_btn.image=tkimg2
        self.camera_btn.place(x=125,y=215)
        root.update()
        ret,frame=self.cpt.read()
        if ret:
            now_time=int(time())
            the_file_name=str(now_time)+'.jpg'
            imwrite(the_file_name,frame)
            try:
                pimg=ImageTk.PhotoImage(image=Image.fromarray(cvtColor(frame,COLOR_BGR2RGB)).resize((280,210)))
                Label(root,image=pimg).place(x=8,y=0)
                root.update()
            except TclError:
                pass
            self.cpt.release()
            client = AipFace(APP_ID, API_KEY, SECRET_KEY)
            groupIdList='default'
            f = open(the_file_name, 'rb')
            image = base64.b64encode(f.read())
            image64 = str(image,'utf-8')
            image_type = "BASE64"
            faceOptions={}
            faceOptions['max_face_num']=3
            dic=client.search(image64, image_type,groupIdList,faceOptions)
            user_id=''
            score=0
            if dic['error_code']==0:
                user_id=dic['result']['user_list'][0]['user_id']
                score=round(dic['result']['user_list'][0]['score'],1)
                print('用户：'+user_id+'\n匹配率：'+str(score)+'%')  # 此处的返回值为人脸的基本检测的数值效果
            else:
                serror('ERROR!','没识别到人脸！')
            f.close()
            os.remove(the_file_name)
            self.camera_btn=Button(root,image=tkimg1,command=lambda:self.take_photo(tkimg1,tkimg2),bd=0,relief=SUNKEN)
            self.camera_btn.image=tkimg1
            self.camera_btn.place(x=125,y=215)
            root.update()
        else:
            serror('ERROR!','拍照失败！')
root=Tk()
faceAI()
root.mainloop()