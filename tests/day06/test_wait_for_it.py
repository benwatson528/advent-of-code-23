import os
import re
from pathlib import Path

from main.day06.wait_for_it import solve


def test_p1_simple():
    times, distances = read_input("data/test_input.txt")
    assert solve(zip([int(x) for x in times], [int(x) for x in distances])) == 288


def test_p1_real():
    times, distances = read_input("data/input.txt")
    assert solve(zip([int(x) for x in times], [int(x) for x in distances])) == 1083852


def test_p2_simple():
    times, distances = read_input("data/test_input.txt")
    time = int(''.join(time for sublist in times for time in sublist))
    distance = int(''.join(distance for sublist in distances for distance in sublist))
    assert solve(zip([time], [distance])) == 71503


def test_p2_real():
    times, distances = read_input("data/input.txt")
    time = int(''.join(time for sublist in times for time in sublist))
    distance = int(''.join(distance for sublist in distances for distance in sublist))
    assert solve(zip([time], [distance])) == 23501589


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        return re.findall(r'\d+', lines[0]), re.findall(r'\d+', lines[1])
