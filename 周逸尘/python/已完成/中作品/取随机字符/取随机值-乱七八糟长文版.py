# -*- coding:utf-8 -*-
import random
import time
###############
def ranstr(num):
    strings='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{;}\|:\'\",.<>/?`~，。《》、？！￥……【】｛｝、；：‘’“”·¿¡〖〗︻︼「」—ˉ﹫〃‖☰≈≠≤≥∶∞∧∨∑∏∪∩∈∵∴⊥∥∠⌒⊙√°′″〒￠￡₴₰¢₤¥₳₲₪₵Ұ₣₱฿¤₡₮₭₩₢₥₫₦złčर₹ƒ₸€ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζνξοπρσηθικλμτυφχψωАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяāáǎàōóǒòēéěèīíǐìūúǔùǖǘǚǜüêɑńňˆˇ﹖•¨\ \ \ \ \ \ \ '
    salt=''
    for i in range(num):
        salt+=random.choice(strings)
    return salt
salt=ranstr(random.randint(20000,200000))
print(salt)
while True:
    time.sleep(1)
#请注意：运行后你可能感觉眼花缭乱！