import os
from pathlib import Path

import pytest

from main.day23.a_long_walk import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), handle_slopes=True) == 94


def test_p1_real():
    assert solve(read_input("data/input.txt"), handle_slopes=True) == 2194


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), handle_slopes=False) == 154


@pytest.mark.skip(reason="Takes 60 seconds")
def test_p2_real():
    assert solve(read_input("data/input.txt"), handle_slopes=False) == 6410


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        walkable = {}
        for y, row in enumerate(f.read().splitlines()):
            for x, cell in enumerate(row):
                if cell != '#':
                    walkable[(x, y)] = cell
        return walkable
