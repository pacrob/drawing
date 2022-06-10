import pytest

from polygon import Polygon


def test_polygon():
    bob = Polygon(5, "red")

    assert bob.sides == 5
    assert bob.color == "red"
