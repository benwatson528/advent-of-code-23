import os
from pathlib import Path

from main.day02.cube_conundrum import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), {"red": 12, "green": 13, "blue": 14}) == 8


def test_p1_real():
    assert solve(read_input("data/input.txt"), {"red": 12, "green": 13, "blue": 14}) == 1950 # too low


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        games = []
        for line in f.read().splitlines():
            game = []
            for subsets in line.split(": ")[1].split("; "):
                game.append({cubes.split(" ")[1]: int(cubes.split(" ")[0]) for cubes in subsets.split(", ")})
            games.append(game)
        return games
