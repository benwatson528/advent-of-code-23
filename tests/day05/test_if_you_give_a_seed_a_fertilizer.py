import os
import re
from pathlib import Path

from main.day05.if_you_give_a_seed_a_fertilizer import solve_p1, solve_p2


def test_p1_simple():
    seeds, conversions = read_input("data/test_input.txt")
    assert solve_p1(seeds, conversions) == 35


def test_p1_real():
    seeds, conversions = read_input("data/input.txt")
    assert solve_p1(seeds, conversions) == 650599855


def test_p2_simple():
    seeds, conversions = read_input("data/test_input.txt")
    assert solve_p2(seeds, conversions) == 46


def test_p2_real():
    seeds, conversions = read_input("data/input.txt")
    assert solve_p2(seeds, conversions) == 1240035


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        seeds = set()
        conversions = []
        line_iter = iter(f.read().splitlines())
        line = next(line_iter)
        while line is not None:
            if line.startswith("seeds:"):
                seeds = [int(x) for x in re.findall(r'\d+', line)]
            elif "map:" in line:
                conversions.append(process_map(line_iter, line))
            line = next(line_iter, None)
        return seeds, conversions


def process_map(line_iter, line):
    rows = []
    map_name = (line.split("-")[0], line.split("-")[2].split(" ")[0])
    next_line = next(line_iter)
    while next_line and len(next_line) != 0:
        rows.append([int(x) for x in re.findall(r'\d+', next_line)])
        next_line = next(line_iter, None)
    return map_name, rows
