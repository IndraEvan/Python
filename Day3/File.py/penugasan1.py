# Bendera Indonesia modif poland
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(5)
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

# Posisi awal
t.penup()
t.goto(-150, 100)
t.pendown()

# Merah (atas)
persegi_panjang("white", 300, 100)

# Putih (bawah)
t.penup()
t.goto(-150, 0)
t.pendown()
persegi_panjang("red", 300, 100)

turtle.done()
