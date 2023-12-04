import os
import re
from pathlib import Path

from main.day04.scratchcards import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 13


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 21959


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 30


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 5132675


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        games = []
        for game in f.read().splitlines():
            sides = game.split(": ")[1].split(" | ")
            games.append((parse_nums(sides[0]), parse_nums(sides[1])))
        return games


def parse_nums(s):
    return {int(x) for x in re.findall(r'\d+', s)}
