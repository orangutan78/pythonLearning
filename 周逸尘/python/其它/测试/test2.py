from pymouse import PyMouse
from pykeyboard import PyKeyboard
pms=PyMouse()
kbd=PyKeyboard()
x,y=pms.screen_size()
pms.click(x//2,y-100,1)
#for i in range(100):
    #kbd.type_string('\r')
mouseX,mouseY=pms.position()
print(mouseX)
print(mouseY)