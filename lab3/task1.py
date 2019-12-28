from graph import *

penColor("black")
penSize(1)

def draw_circle(col, x, y, r):
    """Рисуем окружность.
    Цвет заливки - col
    Координаты центра - x,y
    Радиус - r
    """
    brushColor(col)
    circle(x, y, r)

draw_circle("yellow", 300, 300, 100)
draw_circle("red", 260, 270, 10)
draw_circle("red", 340, 270, 20)
draw_circle("black", 260, 270, 5)
draw_circle("black", 340, 270, 5)

brushColor("black")
rectangle(250, 350, 350, 340)

polygon([(200,200), (190,210), (280,270), (290,260)])

run()
