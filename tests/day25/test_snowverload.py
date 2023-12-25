import os
from collections import defaultdict
from pathlib import Path

from main.day25.snowverload import solve


def test_p1_real():
    # mostly solved by hand (by visualising the graph and deleting the three connections)
    assert solve(read_input("data/input.txt")) == 619225


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        connections = defaultdict(set)
        for line in f.read().splitlines():
            nodes = line.split(": ")
            for child in nodes[1].split():
                connections[nodes[0]].add(child)
                connections[child].add(nodes[0])
    return connections
