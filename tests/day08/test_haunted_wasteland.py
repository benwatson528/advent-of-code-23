import os
import re
from pathlib import Path

from main.day08.haunted_wasteland import solve


def test_p1_simple():
    directions, movements = read_input("data/test_input.txt")
    assert solve(directions, movements) == 6


def test_p1_real():
    directions, movements = read_input("data/input.txt")
    assert solve(directions, movements) == 14257


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        directions = lines[0]
        movements = {}
        for line in lines[2:]:
            strs = re.findall(r'(\w+)', line)
            movements[strs[0]] = (strs[1], strs[2])
        return directions, movements
