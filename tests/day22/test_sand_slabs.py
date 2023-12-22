import os
import re
from pathlib import Path

import pytest

from main.day22.sand_slabs import solve


def test_p1_simple():
    bricks, num_bricks = read_input("data/test_input.txt")
    assert solve(bricks, num_bricks) == 5


def test_p1_real():
    bricks, num_bricks = read_input("data/input.txt")
    assert solve(bricks, num_bricks) == 477


def test_p2_simple():
    bricks, num_bricks = read_input("data/test_input.txt")
    assert solve(bricks, num_bricks, chain_reaction=True) == 7


@pytest.mark.skip(reason="15 minutes")
def test_p2_real():
    bricks, num_bricks = read_input("data/input.txt")
    assert solve(bricks, num_bricks, chain_reaction=True) == 61555


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        bricks = {}
        brick_num = 0
        for line in f.read().splitlines():
            positions = [int(x) for x in re.findall(r'\d+', line)]
            bricks.update(populate_all_brick_coords(positions, brick_num))
            brick_num += 1
    return bricks, brick_num


def populate_all_brick_coords(b, brick_num):
    all_coords = {}
    if b[0] == b[3] and b[1] == b[4]:  # x and y are the same
        all_coords.update({(b[0], b[1], z): brick_num for z in range(b[2], b[5] + 1)})
    elif b[1] == b[4] and b[2] == b[5]:  # y and z are the same
        all_coords.update({(x, b[1], b[2]): brick_num for x in range(b[0], b[3] + 1)})
    elif b[0] == b[3] and b[2] == b[5]:  # x and z are the same
        all_coords.update({(b[0], y, b[2]): brick_num for y in range(b[1], b[4] + 1)})
    return all_coords
