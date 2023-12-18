import os
from pathlib import Path

import pytest

from main.day17.clumsy_crucible import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 102


@pytest.mark.skip(reason="14 seconds")
def test_p1_real():
    assert solve(read_input("data/input.txt")) == 1238


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), ultra=True) == 94


@pytest.mark.skip(reason="2.5 mins")
def test_p2_real():
    assert solve(read_input("data/input.txt"), ultra=True) == 1362


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        grid = {}
        for y, row in enumerate(f.read().splitlines()):
            for x, cell in enumerate(row):
                grid[(x, y)] = int(cell)
        return grid
