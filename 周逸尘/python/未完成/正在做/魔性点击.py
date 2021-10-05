from pymouse import PyMouse
from random import*
from time import sleep
pms=PyMouse()
sleep(1)
for i in range(50):
    pms.click(randint(0,1960),randint(0,1280))
    sleep(0.1)