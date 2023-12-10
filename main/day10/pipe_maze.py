from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

DIRECTIONS = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE', 'S': 'NESW'}


def solve_p1(pipes):
    start = next(coord for coord, pipe in pipes.items() if pipe == 'S')
    valid_movements = {coord: get_pipe_connections(pipes, coord) for coord, pipe in pipes.items()}
    current = start
    visited = []
    while True:
        for adjacent_pipe in valid_movements[current]:
            if adjacent_pipe not in visited and current in valid_movements[adjacent_pipe]:
                visited.append(adjacent_pipe)
                current = adjacent_pipe
                if pipes[current] == 'S':
                    return visited


def solve_p2(pipes) -> int:
    loop_pipes = solve_p1(pipes)
    polygon = Polygon(loop_pipes)
    x_bounds = max(x for x, _ in pipes.keys())
    y_bounds = max(y for _, y in pipes.keys())
    enclosed = set()
    for x in range(x_bounds):
        for y in range(y_bounds):
            if (x, y) not in loop_pipes and polygon.contains(Point(x, y)):
                enclosed.add((x, y))
    return len(enclosed)


def get_pipe_connections(pipes, coord):
    return {move_coord(coord, direction) for direction in DIRECTIONS[pipes[coord]] if
            move_coord(coord, direction) in pipes.keys()}


def move_coord(coord, direction):
    match direction:
        case 'N':
            return coord[0], coord[1] - 1
        case 'E':
            return coord[0] + 1, coord[1]
        case 'S':
            return coord[0], coord[1] + 1
        case 'W':
            return coord[0] - 1, coord[1]
        case _:
            return coord
