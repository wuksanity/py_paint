import turtle

import main

colors = ["Black","Red", "Blue", "Yellow", "Green", "Orange", "Purple"]
current_color = 0

# initializing paint window
window = turtle.Screen()
window.title("Python Pixel Paint")
window.bgcolor("white")
window.setup(width=1000, height=700)
window.tracer(0)


# creating paint cursor
cursor = turtle.Turtle()
cursor.speed(5)
cursor.shape("square")
cursor.color("black")
cursor.shapesize(stretch_wid=1, stretch_len=1)
cursor.penup()
cursor.goto(0, 15)
cursor.write("Pixel On!", align="center", font=("Courier", 24, "normal"))
cursor.goto(0, -40)
cursor.write("Press D to draw, A to erase", align="center", font=("Courier", 16, "normal"))
cursor.goto(0, 0)


# cursor functions
def cursor_up():
    y = cursor.ycor()
    y += 5
    cursor.sety(y)
    cursor.clear()


def cursor_down():
    y = cursor.ycor()
    y -= 5
    cursor.sety(y)
    cursor.clear()


def cursor_right():
    x = cursor.xcor()
    x += 5
    cursor.setx(x)
    cursor.clear()


def cursor_left():
    x = cursor.xcor()
    x -= 5
    cursor.setx(x)
    cursor.clear()


# game functions
def draw():
    x = cursor.xcor()
    y = cursor.ycor()

    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.color(colors[current_color])
    pixel.shapesize(stretch_wid=1, stretch_len=1)
    pixel.penup()
    pixel.goto(x, y)


def erase():
    x = cursor.xcor()
    y = cursor.ycor()

    pixel = turtle.Turtle()
    pixel.speed(0)
    pixel.shape("square")
    pixel.color("white")
    pixel.shapesize(stretch_wid=1, stretch_len=1)
    pixel.penup()
    pixel.goto(x, y)


def change_color():
    x = cursor.xcor()
    y = cursor.ycor()
    if main.current_color == len(colors) -1 :
        main.current_color = 0
        cursor.goto(0, 300)
        cursor.write(f"Current Color Changed to {colors[main.current_color]}", align="center", font=("Courier", 16, "normal"))
        cursor.goto(x, y)
    else:
        main.current_color += 1
        cursor.goto(0, 300)
        cursor.write(f"Current Color Changed to {colors[main.current_color]}", align="center",
                     font=("Courier", 16, "normal"))
        cursor.goto(x, y)
    cursor.color(colors[main.current_color])


# keyboard bindings
window.listen()
window.onkeypress(cursor_up, "Up")
window.onkeypress(cursor_down, "Down")
window.onkeypress(cursor_right, "Right")
window.onkeypress(cursor_left, "Left")
window.onkeypress(draw, "d")
window.onkeypress(erase, "a")
window.onkeypress(change_color, "w")


# game loop
while True:
    window.update()