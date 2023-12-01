import os
from pathlib import Path

from main.day01.trebuchet import solve


def test_p1_simple():
    assert solve(read_input("data/test_input_numbers.txt"), is_words=False) == 142


def test_p1_real():
    assert solve(read_input("data/input.txt"), is_words=False) == 54081


def test_p2_simple():
    assert solve(read_input("data/test_input_words.txt"), is_words=True) == 281


def test_p2_real():
    assert solve(read_input("data/input.txt"), is_words=True) == 54649


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
