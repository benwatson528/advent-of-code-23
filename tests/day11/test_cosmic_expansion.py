import os
from pathlib import Path

from main.day11.cosmic_expansion import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 2) == 374


def test_p1_real():
    assert solve(read_input("data/input.txt"), 2) == 9403026


def test_p2_simple_10():
    assert solve(read_input("data/test_input.txt"), 10) == 1030


def test_p2_simple_100():
    assert solve(read_input("data/test_input.txt"), 100) == 8410


def test_p2_real():
    assert solve(read_input("data/input.txt"), 1000000) == 543018317006


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        galaxies = set()
        for y, row in enumerate(f.read().splitlines()):
            for x, cell in enumerate(row):
                if cell == '#':
                    galaxies.add((x, y))
        return galaxies
