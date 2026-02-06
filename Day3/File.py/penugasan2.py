# Buat gambar bebas
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(10)
t.hideturtle()

def persegi_panjang(warna, lebar, tinggi):
    t.fillcolor(warna)
    t.begin_fill()
    for _ in range(2):
        t.forward(lebar)
        t.right(90)
        t.forward(tinggi)
        t.right(90)
    t.end_fill()

t.penup()
t.goto(-150, 100)
t.pendown()
persegi_panjang("black", 300, 300)

t.penup()
t.goto(-150, 0)
t.pendown()
persegi_panjang("red", 300, 100)

y = turtle.Turtle()
y.speed(0)
y.penup()
y.goto(90, -80)
y.pendown()

y.fillcolor("white")
y.begin_fill()

y.circle(30)
y.end_fill()
y.hideturtle()

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.pendown()
pen.goto(-90, -80)

pen.fillcolor("white")
pen.begin_fill()

pen.circle(30)
pen.end_fill()
pen.hideturtle()

turtle.done()