import os
from pathlib import Path

from main.day13.point_of_incidence import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 405


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 33047


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 400


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 28806


def read_input(file_name):
    patterns = []
    rocks = set()
    y_ctr = 0
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for y, row in enumerate(f.read().splitlines()):
            if len(row) == 0 and len(rocks) != 0:
                patterns.append(rocks)
                y_ctr = -1
                rocks = set()
            for x, c in enumerate(row):
                if c == '#':
                    rocks.add((x, y_ctr))
            y_ctr += 1
        patterns.append(rocks)
        return patterns
