import os
import re
from pathlib import Path

import pytest

from main.day24.never_tell_me_the_odds import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt"), 7, 27) == 2


@pytest.mark.skip(reason="1 minute")
def test_p1_real():
    assert solve_p1(read_input("data/input.txt"), 200000000000000, 400000000000000) == 16502


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 47


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == -1


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        hailstones = []
        for line in f.read().splitlines():
            nums = [int(x) for x in re.findall(r'-?\d+', line)]
            hailstones.append(((nums[0], nums[1], nums[2]), (nums[3], nums[4], nums[5])))
        return hailstones
