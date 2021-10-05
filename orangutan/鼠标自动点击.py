from pymouse import PyMouse
import time
m = PyMouse()
#time.sleep(3)
#for i in range(1,10):
while True:
    print(m.position()) #获取当前坐标的位置
    m.click(40,1300)    #在当前坐标的位置点击
    #time.sleep(0.1)
'''m.move(1600,1200)   #鼠标移动到(x,y)位置
a = m.position()
print(a)
'''

#1895,1260


'''m.click(1600,1200)  #移动并且在(x,y)位置左击'''
