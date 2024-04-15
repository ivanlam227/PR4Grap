class Line:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def draw(self):
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color)
