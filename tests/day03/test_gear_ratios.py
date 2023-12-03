import os
import re
from pathlib import Path

from main.day03.gear_ratios import solve


def test_p1_simple():
    numbers, symbols = read_input("data/test_input.txt")
    assert solve(numbers, symbols) == 4361


def test_p1_real():
    numbers, symbols = read_input("data/input.txt")
    assert solve(numbers, symbols) == 535351


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        numbers = {}
        symbols = set()
        for j, row in enumerate(f.read().splitlines()):
            for m in re.finditer(r'\d+', row):
                numbers[(m.start(), j)] = m.group()
            for i, c in enumerate(row):
                if not c.isalnum() and c != '.':
                    symbols.add((i, j))
    return numbers, symbols
