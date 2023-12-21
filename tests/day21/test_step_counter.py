import os
from pathlib import Path

import pytest

from main.day21.step_counter import solve_p1, solve_p2


def test_p1_simple():
    start, rocks = read_input("data/test_input.txt")
    assert solve_p1(start, rocks, 6) == 16


def test_p1_real():
    start, rock = read_input("data/input.txt")
    assert solve_p1(start, rock, 64) == 3816


@pytest.mark.skip(reason="10 seconds")
def test_p2_real():
    start, rock = read_input("data/input.txt")
    assert solve_p2(start, rock, 26501365) == 634549784009844


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        rocks = set()
        for y, row in enumerate(f.read().splitlines()):
            for x, c in enumerate(row):
                if c == '#':
                    rocks.add((x, y))
                elif c == 'S':
                    start = (x, y)
        return start, rocks
