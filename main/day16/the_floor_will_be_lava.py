from enum import Enum


def solve_p1(tiles) -> int:
    start = ((0, 0), Direction.R)
    return len(fire_beam(start, tiles))


def solve_p2(tiles) -> int:
    max_x, max_y = max(x for x, y in tiles), max(y for x, y in tiles)
    left_entries = [((0, y), Direction.R) for y in range(max_y + 1)]
    right_entries = [((max_x, y), Direction.L) for y in range(max_y + 1)]
    top_entries = [((x, 0), Direction.D) for x in range(max_x + 1)]
    bottom_entries = [((x, max_y), Direction.U) for x in range(max_x + 1)]
    return max(len(fire_beam(start, tiles)) for start in left_entries + right_entries + top_entries + bottom_entries)


def fire_beam(start, tiles):
    visited = set()
    to_visit = [start]
    while to_visit:
        coord, direction = to_visit.pop()
        visited.add((coord, direction))
        if coord not in tiles:
            continue
        for new_coord, new_direction in move(coord, direction, tiles):
            if new_coord in tiles.keys() and (new_coord, new_direction) not in visited:
                to_visit.append((new_coord, new_direction))
    return {coord for coord, direction in visited}


def move(coord, direction, tiles):
    match tiles[coord]:
        case '.':
            return [step_coord(coord, direction)]
        case '/':
            return [traverse_diagonal_splitter(coord, direction, is_reversed=True)]
        case '\\':
            return [traverse_diagonal_splitter(coord, direction, is_reversed=False)]
        case '-':
            return traverse_straight_splitter(coord, direction, is_horizontal=True)
        case '|':
            return traverse_straight_splitter(coord, direction, is_horizontal=False)


def traverse_diagonal_splitter(coord, direction, is_reversed):
    match direction:
        case Direction.R:
            return step_coord(coord, Direction.U if is_reversed else Direction.D)
        case Direction.L:
            return step_coord(coord, Direction.D if is_reversed else Direction.U)
        case Direction.U:
            return step_coord(coord, Direction.R if is_reversed else Direction.L)
        case Direction.D:
            return step_coord(coord, Direction.L if is_reversed else Direction.R)


def traverse_straight_splitter(coord, direction, is_horizontal):
    pass_through_directions = (Direction.L, Direction.R) if is_horizontal else (Direction.U, Direction.D)
    if direction in pass_through_directions:
        return [step_coord(coord, direction)]
    else:
        return [step_coord(coord, new_direction) for new_direction in pass_through_directions]


def step_coord(coord, direction):
    return add_coords(coord, direction.value), direction


def add_coords(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


class Direction(Enum):
    R = (1, 0)
    L = (-1, 0)
    U = (0, -1)
    D = (0, 1)
