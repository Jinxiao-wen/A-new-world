import turtle as t
import time as ti
t.penup()
t.setup(800,600,0,0)
t.pencolor("black")
t.pensize(2)
t.goto(200,0)
t.pendown()
t.goto(200,200)
t.goto(-200,200)
t.goto(-200,-200)
t.goto(200,-200)
t.goto(200,0)
t.penup()
t.goto(0,0)
t.pendown()
def up():
    t.seth(90)
def left():
    t.seth(180)
def down():
    t.seth(270)
def right():
    t.seth(0)
t.onkeypress(left,"a")
t.onkeypress(down,"s")
t.onkeypress(right,"d")
t.onkeypress(up,"w")
t.listen()
while True:
    ti.sleep(0.05)
    t.fd(1)
