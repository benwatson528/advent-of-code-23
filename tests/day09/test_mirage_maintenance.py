import os
import re
from pathlib import Path

from main.day09.mirage_maintenance import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 114


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 1853145119


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 2


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 923


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [[int(x) for x in re.findall(r'-?\d+', line)] for line in f.read().splitlines()]
