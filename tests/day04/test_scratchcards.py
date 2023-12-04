import os
from pathlib import Path

from main.day04.scratchcards import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 13


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        return lines
