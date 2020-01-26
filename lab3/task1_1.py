from graph import *

def draw_rectangle(col, x1, y1, x2, y2):
    """ Рисуем прямоугольник.
    Цвет - col
    (x1,y1) - координаты левого верхнего угла
    (x2,y2) - координаты правого нижнего угла
    """
    brushColor(col)
    rectangle(x1,y1,x2,y2)

def draw_circle(h, l_col, col, x, y, r):
    """Рисуем круг цвета col с центром в (x,y) радиуса r
       h - толщина контура
       l_col - цвет контура
    """
    penColor(l_col)
    penSize(h)
    brushColor(col)
    circle(x, y, r)

def draw_cloud(m, x, y):
    """Рисуем облако масштаба m, и с координатами x, y
    """
    
    draw_circle(1, "black", "white", x + 40 * m, y + 20 * m, 20 * m)
    draw_circle(1, "black", "white", x + 60 * m, y + 20 * m, 20 * m)
    draw_circle(1, "black", "white", x + 80 * m, y + 20 * m, 20 * m)
    draw_circle(1, "black", "white", x + 20 * m, y + 28 * m, 20 * m)
    draw_circle(1, "black", "white", x + 40 * m, y + 28 * m, 20 * m)
    draw_circle(1, "black", "white", x + 60 * m, y + 28 * m, 20 * m)
    draw_circle(1, "black", "white", x + 80 * m, y + 28 * m, 20 * m)
    draw_circle(1, "black", "white", x + 100 * m, y + 28 * m, 20 * m)

def draw_ship(x, y, m):
    """
    рисуем корабль.
    Точка привязки - корма
    m - масштаб

    """
    brushColor("brown")
    penColor("brown")
    penSize(1)
    arc(x, y - m / 2, x + m, y + m / 2, 180, 270, PIESLICE)
    rectangle(x + m / 2, y, x + 1.5 * m, y + m / 2)
    polygon([(x + 1.5 * m, y),
            (x + 2.5 * m, y),
            (x + 1.5 * m, y + m / 2),
            (x + 1.5 * m, y)])
    brushColor("black")
    penColor("black")
    rectangle(x + m, y, x + 1.1 * m, y - 1.5 * m)
    brushColor("white")
    penColor("black")
    penSize(1)
    polygon([(x + 1.1 * m, y - 1.5 * m),
            (x + 1.8 * m, y - m),
            (x + 1.1 * m, y - 0.2 * m),
            (x + 1.4 * m, y - m),
            (x + 1.1 * m, y - 1.5 * m)])

def main():
    """Основная функция"""
    draw_rectangle("cyan", 0, 0, 500, 300)
    draw_rectangle("blue", 0, 300, 500, 400)
    draw_rectangle("yellow", 0, 400, 500, 600)
    draw_cloud(1, 30, 35)
    draw_cloud(0.7, 150, 20)
    draw_cloud(0.4, 260, 43)
    draw_circle(1, "black", "yellow", 430, 70, 50)
    draw_ship(200, 320, 50)
    draw_ship(50, 350, 70)
    run()

main()
