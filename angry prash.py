import turtle
t1=turtle.Turtle()
#t1.color("white")
t1.pensize(5)
t1.left(180)
t1.up()
t1.fd(15)
t1.down()
t1.begin_fill()
t1.fillcolor("white")
turtle.bgcolor("black")
for i in range(1,230):
    t1.fd(1.3)
    t1.right(1)
t1.right(290)
t1.fd(80)
t1.right(138)
t1.fd(126)
for i in range(90):
    t1.fd(1.3)
    t1.right(1)
t1.end_fill()
t1.up()
t1.goto(-30,80)
t1.down()
t1.right(121)
t1.fd(80)
t1.up()
t1.goto(-50,115)
t1.down()
t1.right(45)
t1.fd(35)
t1.right(90)
t1.pensize(2)
for i in range(0,180):
    t1.fd(0.27)
    t1.right(1)
t1.up()
t1.goto(-10,110)
t1.down()
t1.pensize(5)
t1.right(30)
t1.fd(28)
t1.right(90)
t1.up()
t1.goto(-10,110)
t1.down()
t1.pensize(2)
for i in range(180):
    t1.fd(0.20)
    t1.left(1)
t1.up()
t1.goto(-20,20)
t1.right(45)
t1.down()
for i in range(1,150):
    if i<=110:
        t1.fd(0.8)
        t1.right(1)
    else:
        t1.fd(0.3)
        t1.right(1)
t1.hideturtle()






