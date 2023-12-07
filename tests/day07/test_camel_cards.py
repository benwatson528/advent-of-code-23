import os
from pathlib import Path

from main.day07.camel_cards import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 6440


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 248422077


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), joker_mode=True) == 5905


def test_p2_real():
    assert solve(read_input("data/input.txt"), joker_mode=True) == 249817836


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return {line.split(" ")[0]: int(line.split(" ")[1]) for line in f.read().splitlines()}
