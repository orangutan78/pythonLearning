import turtle
import random
turtle.shape ("turtle")
turtle.setup(600,600)
turtle.speed(0)
try:
    while True:
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        turtle.goto(x,y)
except:
    pass