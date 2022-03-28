import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("Indian Flag")
t.speed(10)
def draw_a_rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(50)
    t.end_fill()

def draw_circle():
    t.color("#000088")
    t.right(90)
    t.forward(100)
    t.circle(25)
    t.left(90)
    t.up()
    t.forward(24.5)
    t.down()

    for i in range(25):
        t.forward(24.5)
        t.up()
        t.backward(24.5)
        t.down()
        t.right(15)

t.setheading(270)
t.up()
t.goto(0,-200)
t.down()
t.setheading(90)
t.forward(400)
draw_a_rectangle("#FF9933")
t.backward(50)
draw_a_rectangle("white")
t.backward(50)
draw_a_rectangle("#128807")

draw_circle()
t.hideturtle()

turtle.done()