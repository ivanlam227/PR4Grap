class Point:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        self.canvas.create_oval(self.x - 2, self.y - 2, self.x + 2, self.y + 2, fill=self.color)
