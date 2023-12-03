from itertools import product

ADJACENT_CELLS = set(product([-1, 0, 1, -1, 0, 1], repeat=2))


def solve(numbers, symbols) -> int:
    return sum(int(num_val) for num_coord, num_val in numbers.items() if process_number(num_coord, num_val, symbols))


def process_number(num_coord, num_val, symbols):
    return any(is_adjacent_symbol((i, num_coord[1]), symbols) for i in range(num_coord[0], num_coord[0] + len(num_val)))


def is_adjacent_symbol(coord, symbols):
    return len(symbols.intersection([(coord[0] + adj[0], coord[1] + adj[1]) for adj in ADJACENT_CELLS])) > 0
