import turtle
from turtle import *
import random
import math

speed(0)
tracer(False)
b = turtle.Screen()
b.bgcolor("white")
t = turtle.Turtle()
turtle.colormode(255)  # autorise les couleurs RGB

# t.color("red")
# for i in range(3):
#     titi.right(90)
#     titi.circle(42)
# turtle.done()


# def draw_Poligone(sides: int):
#     cotes = 360 / sides
#     for i in range(sides):
#         forward(100)
#         right(cotes)
#     turtle.done()
# draw_Poligone(5)


# def spiral():
#     b.bgcolor("lightgray")
#     for avancer in range(600):
#         forward(avancer)
#         right(50)
#     for i in range(0, 3):
#         width(i)
# spiral()
# turtle.done()


# def rosace():
#     t = turtle.Turtle()
#     t.color("purple")
#     t.pensize(3)
#     turtle.bgcolor("white")

#     # Paramètres de la rosace
#     R = 155  # rayon du grand cercle (fixe)
#     r = 55  # rayon du petit cercle (mobile)
#     d = 80  # distance du crayon depuis le centre du petit cercle

#     t.penup()
#     t.goto(R - r + d, 0)
#     t.pendown()

#     for theta in range(0, 360 * 12):
#         angle = math.radians(theta)
#         x = (R - r) * math.cos(angle) + d * math.cos(((R - r) / r) * angle)
#         y = (R - r) * math.sin(angle) - d * math.sin(((R - r) / r) * angle)
#         t.goto(x, y)
# rosace()
# turtle.done()


# def couleur_aleatoire():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# def forme_special(): Pas fini !

#     speed(0)
#     tracer(False)
#     width(2)
#     for i in range(100):
#         t.color("black", couleur_aleatoire())
#         t.begin_fill()
#         for j in range(4):
#             i -= 1
#             t.forward(100 - i)
#             t.right(90)
#         t.end_fill()
#         t.right(15)
#         t.forward(5)

#     t.hideturtle()
#     update()
#     done()
# forme_pecial()


# def forme_triangle(t, order, size):
#     if order == 0:
#         for _ in range(3):
#             t.forward(size)
#             t.left(120)
#     else:
#         forme_triangle(t, order - 1, size / 2)
#         t.forward(size / 2)
#         forme_triangle(t, order - 1, size / 2)
#         t.backward(size / 2)
#         t.left(60)
#         t.forward(size / 2)
#         t.right(60)
#         forme_triangle(t, order - 1, size / 2)
#         t.left(60)
#         t.backward(size / 2)
#         t.right(60)
# t = turtle.Turtle()
# forme_triangle(t, 8, 400)
# turtle.done()


t.hideturtle()
update()
