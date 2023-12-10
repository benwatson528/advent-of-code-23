import os
from pathlib import Path

from main.day10.pipe_maze import solve_p1, solve_p2


def test_p1_simple():
    assert len(solve_p1(read_input("data/test_input.txt"))) // 2 == 8


def test_p1_real():
    assert len(solve_p1(read_input("data/input.txt"))) // 2 == 6979


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 443


def read_input(file_name):
    pipes = {}
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for j, row in enumerate(f.read().splitlines()):
            for i, cell in enumerate(row):
                if cell != '.':
                    pipes[(i, j)] = cell
        return pipes
