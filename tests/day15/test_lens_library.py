import os
from pathlib import Path

from main.day15.lens_library import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 1320


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 514025


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 145


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 244461


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.readline().rstrip("\n").split(",")
