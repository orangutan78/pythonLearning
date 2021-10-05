import base64
from aip import AipFace
from requests.api import options

'''新建aipface的配置'''
""" 你的 APPID AK SK """
APP_ID = '24879858'
API_KEY = 'tOlnrkmLR0hlShhqPj8g1K0F'
SECRET_KEY = 'WLBs7bCmjEilCyV2xIS3S0XZiHGyMFnx'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


f = open('./orangutan/img/zycface.jpg', 'rb')
image = base64.b64encode(f.read())
image64 = str(image,'utf-8')
image_type = "BASE64"
groupIdList='default'
print(client.search(image64, image_type,groupIdList))  # 此处的返回值为人脸的基本检测的数值效果

# print(strs)
# 人脸检测
# image = str(strs)  # 取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串

'''imageType = "BASE64"

groupIdList = "17ai_1"

""" 调用人脸搜索 """


print(client.search(str(image64), image_type, groupIdList))

# 将返回对比结果
'''
'''
""" 如果有可选参数 """
options = {}
options["quality_control"] = "NORMAL"
options["liveness_control"] = "LOW"
options["user_id"] = "233451"
options["max_user_num"] = 3

""" 带参数调用人脸搜索 """
# print(client.search(image, imageType, , options))


#  人脸搜索返回例子
''' 
face = {
  "face_token": "fid",
  "user_list": [
     {
        "group_id": "test1",
        "user_id": "u333333",
        "user_info": "Test User",
        "score": 99.3
    }
  ]
}