def solve(moving_bricks, num_bricks, chain_reaction=False) -> int:
    stationary_bricks = move_bricks(moving_bricks)
    if chain_reaction:
        return run_chain_reaction(num_bricks, stationary_bricks)
    else:
        return num_bricks - len(check_destroy_affected(stationary_bricks))


def run_chain_reaction(num_bricks, stationary_bricks):
    num_affected = 0
    starting_stationary_bricks = stationary_bricks.copy()
    for brick_num in range(num_bricks):
        unstable_bricks = {k: v for k, v in starting_stationary_bricks.items() if v != brick_num}
        stationary_bricks = move_bricks(unstable_bricks.copy())
        num_affected += get_moved_bricks(unstable_bricks, stationary_bricks)
    return num_affected


def get_moved_bricks(start_bricks, end_bricks):
    moved_bricks = 0
    for brick_num in set(start_bricks.values()):
        start_brick_coords = set(k for k, v in start_bricks.items() if v == brick_num)
        end_brick_coords = set(k for k, v in end_bricks.items() if v == brick_num)
        if start_brick_coords != end_brick_coords:
            moved_bricks += 1
    return moved_bricks


def move_bricks(moving_bricks):
    stationary_bricks = {}
    while moving_bricks:
        lowest_brick_num = find_lowest_brick(moving_bricks)
        place_on_floor(lowest_brick_num, moving_bricks, stationary_bricks)
    return stationary_bricks


def check_destroy_affected(stationary_bricks):
    # for each brick check if only one brick is below it (z - 1). If so then we can't destroy the brick below
    cant_destroy = set()
    for brick_num in set(stationary_bricks.values()):
        bricks_below = set()
        current_brick_coords = {brick_coord for brick_coord, stationary_brick_num in stationary_bricks.items()
                                if brick_num == stationary_brick_num}

        for c in current_brick_coords:
            below_coord = (c[0], c[1], c[2] - 1)
            if below_coord in stationary_bricks and stationary_bricks[below_coord] != brick_num:
                bricks_below.add(stationary_bricks[below_coord])
        if len(bricks_below) == 1:
            cant_destroy.add(next(iter(bricks_below)))
    return cant_destroy


def place_on_floor(lowest_brick_num, moving_bricks, stationary_bricks):
    # find the highest z of a stationary brick with the same x and y as any of the lowest brick's coords
    highest_stationary = 0
    for lowest_brick_coord in [k for k, v in moving_bricks.items() if v == lowest_brick_num]:
        highest_stationary = max(highest_stationary,
                                 max([k[2] for k, v in stationary_bricks.items()
                                      if k[0] == lowest_brick_coord[0] and k[1] == lowest_brick_coord[1]], default=0))
    to_move = [k for k, v in moving_bricks.items() if v == lowest_brick_num]
    height_diff = min(c[2] for c in to_move) - highest_stationary - 1
    for coord in to_move:
        moving_bricks.pop(coord)
        new_coord = (coord[0], coord[1], coord[2] - height_diff)
        stationary_bricks[new_coord] = lowest_brick_num


def find_lowest_brick(moving_bricks):
    # find the lowest z of any moving brick - this will land first
    min_z = 9999999
    min_brick_num = None
    for coord, brick_num in moving_bricks.items():
        if coord[2] < min_z:
            min_z = coord[2]
            min_brick_num = brick_num
    return min_brick_num
