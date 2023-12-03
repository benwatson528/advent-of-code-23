import math
from itertools import product

ADJACENT_CELLS = set(product([-1, 0, 1, -1, 0, 1], repeat=2))


def solve_p1(numbers, symbols) -> int:
    return sum(int(num_val) for num_coord, num_val in numbers.items() if process_number(num_coord, num_val, symbols))


def solve_p2(numbers, symbols) -> int:
    all_number_coords = {}
    for num_coord, num_val in numbers.items():
        for x_range in range(num_coord[0], num_coord[0] + len(num_val)):
            all_number_coords[(x_range, num_coord[1])] = num_val
    all_star_coords = {k for k, v in symbols.items() if v == '*'}
    return sum(find_adjacent_numbers(all_number_coords, star_coord) for star_coord in all_star_coords)


def find_adjacent_numbers(all_number_coords, star_coord):
    adjacent_nums = set()
    for adj in ADJACENT_CELLS:
        adjacent_cell = star_coord[0] + adj[0], star_coord[1] + adj[1]
        if adjacent_cell in all_number_coords.keys():
            adjacent_nums.add(int(all_number_coords[adjacent_cell]))
    return math.prod(adjacent_nums) if len(adjacent_nums) == 2 else 0


def process_number(num_coord, num_val, symbols):
    return any(is_adjacent_symbol((i, num_coord[1]), symbols) for i in range(num_coord[0], num_coord[0] + len(num_val)))


def is_adjacent_symbol(coord, symbols):
    return len(set(symbols.keys()).intersection([(coord[0] + adj[0], coord[1] + adj[1]) for adj in ADJACENT_CELLS])) > 0
