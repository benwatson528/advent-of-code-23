from enum import Enum


def solve(tiles) -> int:
    start = ((0, 0), Direction.R)
    visited = fire_beam(start, tiles)
    return len({coord for coord, direction in visited})


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
    return visited


def move(coord, direction, tiles):
    match tiles[coord]:
        case '.':
            return [step_coord(coord, direction)]
        case '/':
            return [traverse_left_splitter(coord, direction)]
        case '\\':
            return [traverse_right_splitter(coord, direction)]
        case '-':
            if direction in (Direction.L, Direction.R):
                return [step_coord(coord, direction)]
            else:
                return [step_coord(coord, Direction.L), step_coord(coord, Direction.R)]
        case '|':
            if direction in (Direction.U, Direction.D):
                return [step_coord(coord, direction)]
            else:
                return [step_coord(coord, Direction.U), step_coord(coord, Direction.D)]


def traverse_left_splitter(coord, direction):  # /
    match direction:
        case Direction.R:
            return step_coord(coord, Direction.U)
        case Direction.L:
            return step_coord(coord, Direction.D)
        case Direction.U:
            return step_coord(coord, Direction.R)
        case Direction.D:
            return step_coord(coord, Direction.L)


def traverse_right_splitter(coord, direction):  # \
    match direction:
        case Direction.R:
            return step_coord(coord, Direction.D)
        case Direction.L:
            return step_coord(coord, Direction.U)
        case Direction.U:
            return step_coord(coord, Direction.L)
        case Direction.D:
            return step_coord(coord, Direction.R)


def step_coord(coord, direction):
    return add_coords(coord, direction.value), direction


def add_coords(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


class Direction(Enum):
    R = (1, 0)
    L = (-1, 0)
    U = (0, -1)
    D = (0, 1)
