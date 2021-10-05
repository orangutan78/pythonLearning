# -*- coding:utf-8 -*-
import random
###############
def ranstr(num):
    strings='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{;}\|:\'\",.<>/?`~，。《》、？！￥……【】｛｝、；：‘’“”·¿¡〖〗︻︼「」—ˉ﹫〃‖☰≈≠≤≥∶∞∧∨∑∏∪∩∈∵∴⊥∥∠⌒⊙√°′″〒￠￡₴₰¢₤¥₳₲₪₵Ұ₣₱฿¤₡₮₭₩₢₥₫₦złčर₹ƒ₸€ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζνξοπρσηθικλμτυφχψωАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяāáǎàōóǒòēéěèīíǐìūúǔùǖǘǚǜüêɑńňˆˇ﹖•¨\ \ \ \ \ \ \ '
    salt=''
    for i in range(num):
        salt+=random.choice(strings)
    return salt
salt=ranstr(random.randint(3,20))
print(salt)