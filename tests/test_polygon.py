import pytest

from polygon import Polygon


def test_polygon_default():
    bob = Polygon(50, 5)

    assert bob.radius == 50
    assert bob.num_sides == 5

    printed_bob = bob.__repr__()
    assert printed_bob == "A polygon with 5 sides and radius 50 that is (255, 0, 0)"

    assert bob.generate_vertices(0, 0) == [
        (49, 0),
        (16, -47),
        (-39, -30),
        (-41, 28),
        (14, 47),
    ]
