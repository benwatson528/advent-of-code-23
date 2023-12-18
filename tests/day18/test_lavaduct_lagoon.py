import os
from pathlib import Path

from main.day18.lavaduct_lagoon import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 62


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 74074


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), transformed=True) == 952408144115


def test_p2_real():
    assert solve(read_input("data/input.txt"), transformed=True) == 112074045986829


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        instructions = []
        for line in f.read().splitlines():
            components = line.split()
            instructions.append((components[0], int(components[1]), components[2][1:-1]))
    return instructions
