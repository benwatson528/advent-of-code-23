import os
from pathlib import Path

from main.day12.hot_springs import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 21


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 7843


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), 5) == 525152


def test_p2_real():
    assert solve(read_input("data/input.txt"), 5) == 10153896718999


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [(line.split()[0], [int(x) for x in line.split()[1].split(',')])
                for line in f.read().splitlines()]
