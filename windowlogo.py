import turtle
t= turtle.Turtle()
screen = turtle.Screen()
screen.title("Microsoft Windows Logo")
screen.bgcolor("black")
t.color("blue")
t.up()
t.goto(-50,60)
t.down()
t.begin_fill()
t.fillcolor("blue")
t.goto(100,100)
t.goto(100,-100)
t.goto(-50,-60)
t.goto(-50,60)
t.end_fill()
t.color("black")
t.up()
t.goto(-50,0)
t.down()
t.width(10)
t.goto(100,0)

t.up()
t.goto(25,80)
t.down()
t.goto(25,-80)
t.hideturtle()
turtle.done()