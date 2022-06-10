class Polygon:
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color

    def __repr__(self):
        return f"A polygon with {self.sides} sides that is {self.color}"
