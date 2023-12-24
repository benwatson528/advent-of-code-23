from collections import deque

SLOPE_DIRS = {'<': (-1, 0), '>': (1, 0), 'v': (0, 1), '^': (0, -1)}


def solve(walkable, handle_slopes) -> int:
    start = next(k for k, v in walkable.items() if v == 'S')
    end = next(k for k, v in walkable.items() if v == 'E')
    return find_longest_path(start, end, walkable, handle_slopes)


def find_longest_path(start, end, walkable, handle_slopes):
    to_visit = deque([(start, set())])
    longest = 0
    while to_visit:
        current, visited = to_visit.popleft()
        if current == end:
            if len(visited) > longest:
                longest = len(visited)
            continue

        for neighbour in get_adjacent_cells(current, walkable.get(current, None), handle_slopes):
            if neighbour not in visited and neighbour in walkable:
                to_visit.append((neighbour, visited | {current}))

    return longest


def get_adjacent_cells(current, tile, handle_slopes):
    if handle_slopes and tile in ('<', '>', 'v', '^'):
        slope_direction = SLOPE_DIRS[tile]
        return [(current[0] + slope_direction[0], current[1] + slope_direction[1])]
    else:
        return [(current[0] + 1, current[1]),
                (current[0] - 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1)]
