import os
import re
from pathlib import Path

from main.day03.gear_ratios import solve_p1, solve_p2


def test_p1_simple():
    numbers, symbols = read_input("data/test_input.txt")
    assert solve_p1(numbers, symbols) == 4361


def test_p1_real():
    numbers, symbols = read_input("data/input.txt")
    assert solve_p1(numbers, symbols) == 535351


def test_p2_simple():
    numbers, symbols = read_input("data/test_input.txt")
    assert solve_p2(numbers, symbols) == 467835


def test_p2_real():
    numbers, symbols = read_input("data/input.txt")
    assert solve_p2(numbers, symbols) == 87287096


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        numbers = {}
        symbols = {}
        for j, row in enumerate(f.read().splitlines()):
            for m in re.finditer(r'\d+', row):
                numbers[(m.start(), j)] = m.group()
            for i, c in enumerate(row):
                if not c.isalnum() and c != '.':
                    symbols[(i, j)] = c
    return numbers, symbols
