import os
from pathlib import Path

from main.day20.pulse_propagation import solve_p1, solve_p2, NodeType


def test_p1_simple():
    assert solve_p1(read_input("data/test_input_1.txt"), 1000) == 32000000


def test_p1_complex():
    assert solve_p1(read_input("data/test_input_2.txt"), 1000) == 11687500


def test_p1_real():
    assert solve_p1(read_input("data/input.txt"), 1000) == 899848294


def test_p2_real():
    assert solve_p2(read_input("data/input.txt"), {"xp": 0, "fc": 0, "fh": 0, "dd": 0}) == 247454898168563


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        nodes = {}  # abc: (&, state, [inv, con])
        for line in f.read().splitlines():
            key = line.split()[0].replace('%', '').replace('&', '')
            node_type = get_node_type(line.split()[0])
            children = line.split(" -> ")[1].split(", ")
            state = {} if node_type == NodeType.CONJUNCTION else False
            nodes[key] = (node_type, state, children)
        populate_conjunction_starting_states(nodes)
        nodes["output"] = (NodeType.OUTPUT, False, [])
        nodes["rx"] = (NodeType.OUTPUT, False, [])
        return nodes


def populate_conjunction_starting_states(nodes):
    for node_name, node_info in nodes.items():
        if node_info[0] == NodeType.CONJUNCTION:
            for other_node_name, other_node_info in nodes.items():
                _, _, other_children = other_node_info
                if node_name in other_children:
                    node_info[1][other_node_name] = False


def get_node_type(key):
    if key.startswith('%'):
        return NodeType.FLIP_FLOP
    elif key.startswith('&'):
        return NodeType.CONJUNCTION
    else:
        return NodeType.BROADCAST
