from collections import deque

DIRECTIONS = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE', 'S': 'NESW'}


def solve(pipes) -> int:
    start = next(coord for coord, pipe in pipes.items() if pipe == 'S')
    valid_movements = {coord: get_pipe_connections(pipes, coord) for coord, pipe in pipes.items()}
    return max(len(x) for x in bfs(start, valid_movements).values())


def bfs(start, valid_movements):
    visited = {start: []}
    to_visit = deque()
    to_visit.append((start, []))
    while to_visit:
        current, path = to_visit.popleft()
        for adjacent_pipe in valid_movements[current]:
            if adjacent_pipe not in visited and current in valid_movements[adjacent_pipe]:
                visited[adjacent_pipe] = path + [current]
                to_visit.append((adjacent_pipe, path + [current]))
    return visited


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
