import tkinter as tk
from point import Point
from line import Line
from ellipse import Ellipse
from rectangle import Rectangle
from polygon import Polygon

def create_point(canvas):
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    color = input("Введите цвет точки (например, 'red', '#00FF00', 'rgb(0, 255, 0)': ").strip()
    point = Point(canvas, x, y, color)
    point.draw()

def create_line(canvas):
    x1 = int(input("Введите начальную координату x: "))
    y1 = int(input("Введите начальную координату y: "))
    x2 = int(input("Введите конечную координату x: "))
    y2 = int(input("Введите конечную координату y: "))
    color = input("Введите цвет линии: ").strip()
    line = Line(canvas, x1, y1, x2, y2, color)
    line.draw()

def create_ellipse(canvas):
    x1 = int(input("Введите координату x верхнего левого угла: "))
    y1 = int(input("Введите координату y верхнего левого угла: "))
    x2 = int(input("Введите координату x нижнего правого угла: "))
    y2 = int(input("Введите координату y нижнего правого угла: "))
    color = input("Введите цвет эллипса: ").strip()
    filled = input("Закрашенный эллипс (yes/no): ").lower() == "yes"
    ellipse = Ellipse(canvas, x1, y1, x2, y2, color, filled)
    ellipse.draw()

def create_rectangle(canvas):
    x1 = int(input("Введите координату x верхнего левого угла: "))
    y1 = int(input("Введите координату y верхнего левого угла: "))
    x2 = int(input("Введите координату x нижнего правого угла: "))
    y2 = int(input("Введите координату y нижнего правого угла: "))
    color = input("Введите цвет прямоугольника: ").strip()
    filled = input("Закрашенный прямоугольник (yes/no): ").lower() == "yes"
    rectangle = Rectangle(canvas, x1, y1, x2, y2, color, filled)
    rectangle.draw()

def create_polygon(canvas):
    points = []
    while True:
        x = int(input("Введите координату x (0 для завершения): "))
        if x == 0:
            break
        y = int(input("Введите координату y: "))
        points.append(x)
        points.append(y)
    color = input("Введите цвет полигона: ").strip()
    filled = input("Закрашенный полигон (yes/no): ").lower() == "yes"
    polygon = Polygon(canvas, points, color, filled)
    polygon.draw()

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()

    shapes = {
        "1": create_point,
        "2": create_line,
        "3": create_ellipse,
        "4": create_rectangle,
        "5": create_polygon
    }

    print("Выберите графический примитив:")
    print("1. Точка")
    print("2. Отрезок")
    print("3. Эллипс")
    print("4. Прямоугольник")
    print("5. Полигон")

    while True:
        choice = input("Введите номер (или 'q' для выхода): ")
        if choice == "q":
            break
        if choice in shapes:
            shapes[choice](canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
