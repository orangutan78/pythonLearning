from aip import AipFace
import base64
import requests 

""" 你的 APPID AK SK """
APP_ID = '24879858'
API_KEY = 'tOlnrkmLR0hlShhqPj8g1K0F'
SECRET_KEY = 'WLBs7bCmjEilCyV2xIS3S0XZiHGyMFnx'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
#---------------------------------------------
#获取token
def getToken():
    #在下面的双引号中分别填入 你的 AK 和 SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
    response = requests.get(host, headers=headers)
    json_result = json.loads(response.text)
    return json_result['access_token']

#---------------------------------------------
#访问API
def detect_face(img_BASE64):
    # 人脸检测与属性分析
    img_BASE64 = img_BASE64
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    usrID=generate_random_str(randomlength=20)
    post_data = {
        # 必填项
        "image": img_BASE64,
        "image_type": "BASE64",
        "group_id": "jinridaofang",
        "user_id": usrID,
        "max_user_num":10,
    }
    access_token =getToken()
    request_url = request_url + "?access_token=" + access_token
    response = requests.post(url=request_url, data=post_data, headers=headers)
    if response:
        print(response.json())
