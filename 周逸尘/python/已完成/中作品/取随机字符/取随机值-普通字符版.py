import random
###############
def ranstr(num):
    strings='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={[}]\\|;:\'\",.<>/?！￥（）——｛｝【】、；：‘’“”，。《》？·~`'
    salt=''
    for i in range(num):
        salt+=random.choice(strings)
    return salt
salt=ranstr(random.randint(3,20))
print(salt)