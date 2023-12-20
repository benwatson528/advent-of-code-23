from collections import deque, Counter
from enum import Enum

import math


def solve_p1(nodes, num_presses) -> int:
    initial_sent = Counter({False: 0, True: 0})
    for _ in range(num_presses):
        instruction_sender_helper("broadcaster", nodes, initial_sent)
    return math.prod(initial_sent.values())


def solve_p2(nodes, end_nodes) -> int:
    initial_sent = Counter({False: 0, True: 0})
    i = 0
    while True:
        i += 1
        instruction_sender_helper("broadcaster", nodes, initial_sent, end_nodes, i)
        if all(v != 0 for v in end_nodes.values()):
            return math.lcm(*end_nodes.values())


def instruction_sender_helper(start_node, nodes, num_sent, end_nodes=None, i=0):
    stack = deque([(start_node, None, False)])  # node_name, parent, is_high
    while stack:
        node_name, parent_node, incoming_pulse = stack.popleft()
        node_type, state, children = nodes[node_name]
        if end_nodes and node_name in end_nodes and not incoming_pulse and end_nodes[node_name] == 0:
            end_nodes[node_name] = i
        num_sent[incoming_pulse] += 1
        match node_type:
            case NodeType.BROADCAST:
                stack.extend((child, node_name, incoming_pulse) for child in children)
            case NodeType.FLIP_FLOP:
                if not incoming_pulse:
                    nodes[node_name] = (node_type, not state, children)
                    stack.extend((child, node_name, not state) for child in children)
            case NodeType.CONJUNCTION:
                state[parent_node] = incoming_pulse
                output_pulse = not all(s for s in state.values())
                stack.extend((child, node_name, output_pulse) for child in children)
            case NodeType.OUTPUT:
                continue


class NodeType(Enum):
    BROADCAST = 0
    FLIP_FLOP = 1
    CONJUNCTION = 2
    OUTPUT = 3
