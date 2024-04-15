class Polygon:
    def __init__(self, canvas, points, color, filled=False):
        self.canvas = canvas
        self.points = points
        self.color = color
        self.filled = filled

    def draw(self):
        if self.filled:
            self.canvas.create_polygon(self.points, fill=self.color)
        else:
            self.canvas.create_polygon(self.points, outline=self.color)
