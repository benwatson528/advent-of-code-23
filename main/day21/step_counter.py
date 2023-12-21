from math import ceil


def solve_p1(start, rocks, step_limit) -> int:
    return len(move_frontier(start, rocks, step_limit))


def solve_p2(start, rocks, step_limit) -> int:
    return solve_quadratic(rocks, start, step_limit)


def move_frontier(start, rocks, step_limit):
    grid_width = max(x for x, y in rocks) + 1
    frontier_coords = {start}
    for i in range(step_limit):
        new_coords = set()
        for coord in frontier_coords:
            new_coords.update(get_adjacent_moves(coord, rocks, grid_width))
        frontier_coords = new_coords
    return frontier_coords


def get_adjacent_moves(current, rocks, grid_width):
    return set(move for move in ((current[0] - 1, current[1]),
                                 (current[0] + 1, current[1]),
                                 (current[0], current[1] - 1),
                                 (current[0], current[1] + 1))
               if (move[0] % grid_width, move[1] % grid_width) not in rocks)


def solve_quadratic(rocks, start, step_limit):
    grid_width = max(x for x, y in rocks) + 1  # H
    num_grids = step_limit % grid_width  # mod
    a = solve_p1(start, rocks, num_grids)
    b = solve_p1(start, rocks, num_grids + grid_width)
    c = solve_p1(start, rocks, num_grids + 2 * grid_width)
    diff_1 = b - a
    diff_2 = c - b
    diff_3 = diff_2 - diff_1
    final_a = diff_3 // 2
    final_b = diff_1 - 3 * final_a
    final_c = a - final_b - final_a
    n = ceil(step_limit / grid_width)
    ans = final_a * n ** 2 + final_b * n + final_c
    return ans
