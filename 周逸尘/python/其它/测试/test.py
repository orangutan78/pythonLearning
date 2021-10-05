from random import random as r
import math
while 1:
    num=int(input('tds:'))
    point=0
    for i in range(num):
        x,y=r(),r()
        dist=math.sqrt(x**2+y**2)
        if dist<=1:
            point+=1
    Pi=4*point/num
    print('Pi:'+str(Pi))