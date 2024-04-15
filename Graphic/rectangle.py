class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2, color, filled=False):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.filled = filled

    def draw(self):
        if self.filled:
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)
        else:
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.color)
