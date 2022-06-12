import math

class Polygon:
    def __init__(self, radius, num_sides, color=(255, 0, 0)):
        self.num_sides = num_sides
        self.color = color
        self.radius = radius

    def __repr__(self):
        return (
            f"A polygon with {self.num_sides} sides and radius {self.radius} that is {self.color}"
        )

    def generate_vertices(self, x: int, y: int):
        # figure out how to calc line locations based on center point
        a = math.acos(1 / self.radius)
        # top_vertex = (y, x - self.radius)
        # vertices = [top_vertex]
        vertices = []

        for s in range(0, self.num_sides):
            new_x = x + self.radius * math.cos(a + 2 * math.pi * s / self.num_sides)
            new_y = y + self.radius * math.sin(a + 2 * math.pi * s / self.num_sides)
            new_x, new_y = int(new_x), int(new_y)
            vertices.append((new_y, new_x))

        # print(vertices)
        return vertices