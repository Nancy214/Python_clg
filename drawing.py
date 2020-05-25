import turtle
import random
board = turtle.Turtle()
board.speed(30)
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    board.color(R, G, B)

for i in range(100):
    change_color()
    board.circle(50,105)
    board.forward(i*3)
    board.right(10)

turtle.done()
