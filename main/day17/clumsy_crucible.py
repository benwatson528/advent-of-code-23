from enum import Enum


def solve(grid, ultra=False) -> int:
    end = max(x for x, y in grid.keys()), max(y for x, y in grid.keys())
    visited = set()
    distances = {((0, 1), Direction.R, 1): grid[(0, 1)],
                 ((1, 0), Direction.D, 1): grid[(1, 0)]}
    to_visit = [(((0, 1), Direction.D, 1), grid[(0, 1)]),
                (((1, 0), Direction.R, 1), grid[(1, 0)])]
    while to_visit:
        to_visit.sort(key=lambda x: -x[1])
        current, heat_loss = to_visit.pop()
        if current in visited:
            continue
        visited.add(current)
        if current[2] > 3 and current[0] == end:
            continue
        for next_move in get_next_moves(current, end, ultra):
            if next_move in visited:
                continue
            new_heat_loss = heat_loss + grid[next_move[0]]
            if next_move not in distances or new_heat_loss < distances[next_move]:
                if ultra and next_move[0] == end and next_move[2] < 4:
                    continue
                to_visit.append((next_move, new_heat_loss))
                distances[next_move] = new_heat_loss
    ends = [(k, v) for k, v in distances.items() if k[0] == end]
    return min(v for k, v in ends)


def get_next_moves(current, end, ultra):
    max_steps = 10 if ultra else 3
    next_moves = []
    new_directions = [current[1]] if ultra and current[2] < 4 else [Direction.R, Direction.D, Direction.L, Direction.U]
    for new_direction in new_directions:
        if new_direction == Direction.R and current[1] == Direction.L:
            continue
        if new_direction == Direction.L and current[1] == Direction.R:
            continue
        if new_direction == Direction.U and current[1] == Direction.D:
            continue
        if new_direction == Direction.D and current[1] == Direction.U:
            continue

        new_coord = current[0][0] + new_direction.value[0], current[0][1] + new_direction.value[1]
        new_num_steps_in_direction = current[2] + 1 if current[1] == new_direction else 1
        new_ptr = (new_coord, new_direction, new_num_steps_in_direction)
        if 0 <= new_coord[0] <= end[0] and 0 <= new_coord[1] <= end[1] and new_num_steps_in_direction <= max_steps:
            next_moves.append(new_ptr)
    return next_moves


class Direction(Enum):
    R = (1, 0)
    D = (0, 1)
    L = (-1, 0)
    U = (0, -1)
