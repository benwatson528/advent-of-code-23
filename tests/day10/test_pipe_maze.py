import os
from pathlib import Path

from main.day10.pipe_maze import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 8


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 6979


def read_input(file_name):
    pipes = {}
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for j, row in enumerate(f.read().splitlines()):
            for i, cell in enumerate(row):
                if cell != '.':
                    pipes[(i, j)] = cell
        return pipes
