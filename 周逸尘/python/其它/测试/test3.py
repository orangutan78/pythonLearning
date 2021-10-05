from pymouse import PyMouse
from time import sleep
pms=PyMouse()
sleep(2)
for i in range(1400):
    mouseX,mouseY=pms.position()
    pms.click(mouseX,mouseY)
    #sleep(0.1)