import base64
from aip import AipFace
from requests.api import options

'''新建aipface的配置'''
""" 你的 APPID AK SK """
APP_ID = '24879858'
API_KEY = 'tOlnrkmLR0hlShhqPj8g1K0F'
SECRET_KEY = 'WLBs7bCmjEilCyV2xIS3S0XZiHGyMFnx'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

f = open('./orangutan/img/face.jpg', 'rb')

image = base64.b64encode(f.read())
image64 = str(image,'utf-8')
image_type = "BASE64"
groupID='default'
userID='zyc'
faceOptions={}

faceOptions["action_type"] = "REPLACE"  #如有重复，则替换
result=client.addUser(image64, image_type,groupID,userID,faceOptions)

print(result)  # 此处的返回值为人脸注册的基本的数值效果






