import os
from pathlib import Path

import pytest

from main.day14.parabolic_reflector_dish import solve_p1, solve_p2


def test_p1_simple():
    moving_rocks, static_rocks = read_input("data/test_input.txt")
    assert solve_p1(moving_rocks, static_rocks) == 136


def test_p1_real():
    moving_rocks, static_rocks = read_input("data/input.txt")
    assert solve_p1(moving_rocks, static_rocks) == 113078


def test_p2_simple():
    moving_rocks, static_rocks = read_input("data/test_input.txt")
    assert solve_p2(moving_rocks, static_rocks, 1000000000) == 64


@pytest.mark.skip(reason="Takes 90 seconds")
def test_p2_real():
    moving_rocks, static_rocks = read_input("data/input.txt")
    assert solve_p2(moving_rocks, static_rocks, 1000000000) == 94255


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        moving_rocks = []
        static_rocks = set()
        for y, row in enumerate(f.read().splitlines()):
            for x, c in enumerate(row):
                if c == 'O':
                    moving_rocks.append((x, y))
                elif c == '#':
                    static_rocks.add((x, y))
        return moving_rocks, static_rocks
