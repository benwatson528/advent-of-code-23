import os
from pathlib import Path

from main.day02.cube_conundrum import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt"), {"red": 12, "green": 13, "blue": 14}) == 8


def test_p1_real():
    assert solve_p1(read_input("data/input.txt"), {"red": 12, "green": 13, "blue": 14}) == 2164


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 2286


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 69929


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        games = []
        for line in f.read().splitlines():
            game = []
            for subsets in line.split(": ")[1].split("; "):
                game.append({cubes.split(" ")[1]: int(cubes.split(" ")[0]) for cubes in subsets.split(", ")})
            games.append(game)
        return games
