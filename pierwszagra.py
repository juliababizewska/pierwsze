import turtle
import random
import time


def intro():
    t.penup()
    t.setpos(0, -300)
    t.pendown()
    t.pensize(8)
    t.speed(0)
    for i in range(300, 0, -4):
        t.circle(i)
        t.pencolor(random.choice(
            ["indianred", "brown", "firebrick", "maroon", "darkred", "red", "mistyrose", "salmon", "tomato", "coral",
             "chocolate", "sienna", "lightsalmon", "orangered", "peachpuff"]))
    time.sleep(1)
    t.reset()
    t.penup()
    t.setpos(0, 200)
    t.pendown()


def changeshape(x, y):
    t.shape("triangle")


def changecolor():
    t.pencolor(random.choice(["red", "blue", "green", "yellow"]))


def reset():
    t.reset()
    time.sleep(1)
    t.penup()
    t.setpos(0, 200)
    t.pendown()
    t.pencolor("white")
    t.pensize(10)
    f = [jeden, dwa, trzy, cztery, piec]
    random.choice(f)()
    t1 = 0
    t.penup()
    t.setpos(0, -100)
    t.pendown()


def endtime(x, y):
    print(round(time.time() - t1, 2))


def close():
    turtle.Screen().bye()


def prawo():
    t.setheading(0)
    t.fd(50)


def lewo():
    t.setheading(180)
    t.fd(50)


def gora():
    t.setheading(90)
    t.fd(50)
def dol():
    t.setheading(270)
    t.fd(50)


def jeden():
    t.penup()
    t.setpos(0, 100)
    t.pendown()
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(150)
    for x in range(4):
        t.right(90)
        t.fd(100)


def dwa():
    t.penup()
    t.setpos(0, 100)
    t.pendown()
    t.fd(100)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.left(90)
    t.fd(100)


def trzy():
    t.penup()
    t.setpos(0, 150)
    t.pendown()
    t.left(90)
    t.fd(50)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(50)


def cztery():
    t.penup()
    t.setpos(0, 200)
    t.pendown()
    t.fd(50)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(100)
    t.right(90)
    t.fd(50)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.fd(200)


def piec():
    t.penup()
    t.setpos(0, 150)
    t.pendown()
    t.fd(50)
    t.right(90)
    t.fd(200)
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(250)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(50)


s = turtle.Screen()
s.setup(1000, 1000)
s.bgcolor("lightcoral")
s.title("moja pierwsza gra :)")
t = turtle.Turtle()
t.penup()
t.setpos(0, 50)
t.pendown()
intro()
time.sleep(2)
t.color("white")
t.write("Welcome!", font=("Times New Roman", 24, "normal"))
time.sleep(2)
t.reset()
t.color("white")
t.write("use r to draw another shape", font=("Times New Roman", 24, "normal"))
time.sleep(4)
t.reset()
t.color("white")
t.write("use e to end the game", font=("Times New Roman", 24, "normal"))
time.sleep(4)
t.reset()
t.color("white")
t.write("use left click and space to customise your player", font=("Times New Roman", 24, "normal"))
time.sleep(4)
t.reset()
t.color("white")
t.write("use right click to pause the time", font=("Times New Roman", 24, "normal"))
time.sleep(4)
t.reset()
t.color("white")
t.write("have fun :)", font=("Times New Roman", 24, "normal"))
time.sleep(4)
t.reset()
t.pencolor("white")
t.pensize(10)
f = [jeden, dwa, trzy, cztery, piec]
random.choice(f)()
t1 = time.time()
t.penup()
t.setpos(0, -100)
t.pendown()

turtle.listen()
turtle.onkey(gora, "Up")
turtle.onkey(dol, "Down")
turtle.onkey(prawo, "Right")
turtle.onkey(lewo, "Left")
turtle.onscreenclick(changeshape, 1)
turtle.onscreenclick(endtime, 3)
turtle.onkey(changecolor, "space")
turtle.onkey(reset, "r")
turtle.onkey(close, "e")

turtle.mainloop()
