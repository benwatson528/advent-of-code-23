import os
from pathlib import Path

from main.day16.the_floor_will_be_lava import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 46


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 8098


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 51


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 8335


def read_input(file_name):
    tiles = {}
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for y, row in enumerate(f.read().splitlines()):
            for x, cell in enumerate(row):
                tiles[(x, y)] = cell
    return tiles
