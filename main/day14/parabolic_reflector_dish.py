def solve_p1(moving_rocks, static_rocks) -> int:
    platform_height = (max(y for x, y in static_rocks.union(set(moving_rocks))))
    return sum(platform_height - rock[1] + 1 for rock in tilt_north(moving_rocks, static_rocks))


def solve_p2(moving_rocks, static_rocks, total_cycles) -> int:
    platform_height = max(y for x, y in static_rocks.union(set(moving_rocks)))
    platform_width = max(x for x, y in static_rocks.union(set(moving_rocks)))
    end_states = {tuple(moving_rocks): 0}
    moved_rocks = moving_rocks
    for cycle in range(1, total_cycles + 1):
        moved_rocks = tilt_north(moved_rocks, static_rocks)
        moved_rocks = tilt_west(moved_rocks, static_rocks)
        moved_rocks = tilt_south(moved_rocks, static_rocks, platform_height)
        moved_rocks = tilt_east(moved_rocks, static_rocks, platform_width)
        moved_rocks_tuple = tuple(moved_rocks)
        if moved_rocks_tuple in end_states:
            start_of_loop = end_states[moved_rocks_tuple]
            wrapped_cycle = (total_cycles - start_of_loop) % (cycle - start_of_loop)
            end_state = next(
                rocks for rocks, cycle_num in end_states.items() if cycle_num == start_of_loop + wrapped_cycle)
            return sum(platform_height - rock[1] + 1 for rock in end_state)
        end_states[moved_rocks_tuple] = cycle


def tilt_north(moving_rocks, static_rocks):
    moved_rocks = set()
    for moving_rock in sorted(list(moving_rocks), key=lambda x: x[1]):
        moved_rocks.add(find_north_resting_spot(moving_rock, moved_rocks.union(static_rocks)))
    return moved_rocks


def find_north_resting_spot(moving_rock, static_rocks):
    next_rock_north = max([static_rock[1] for static_rock in static_rocks
                           if static_rock[0] == moving_rock[0] and moving_rock[1] > static_rock[1]],
                          default=-1)
    return moving_rock[0], max(next_rock_north + 1, 0)


def tilt_south(moving_rocks, static_rocks, platform_height):
    moved_rocks = set()
    for moving_rock in sorted(list(moving_rocks), key=lambda x: x[1], reverse=True):
        moved_rocks.add(find_south_resting_spot(moving_rock, moved_rocks.union(static_rocks), platform_height))
    return moved_rocks


def find_south_resting_spot(moving_rock, static_rocks, platform_height):
    next_rock_south = min([static_rock[1] for static_rock in static_rocks
                           if static_rock[0] == moving_rock[0] and moving_rock[1] < static_rock[1]],
                          default=platform_height + 1)
    return moving_rock[0], min(next_rock_south - 1, platform_height)


def tilt_west(moving_rocks, static_rocks):
    moved_rocks = set()
    for moving_rock in sorted(list(moving_rocks), key=lambda x: x[0]):
        moved_rocks.add(find_west_resting_spot(moving_rock, moved_rocks.union(static_rocks)))
    return moved_rocks


def find_west_resting_spot(moving_rock, static_rocks):
    next_rock_west = max([static_rock[0] for static_rock in static_rocks
                          if static_rock[1] == moving_rock[1] and moving_rock[0] > static_rock[0]],
                         default=-1)
    return max(next_rock_west + 1, 0), moving_rock[1]


def tilt_east(moving_rocks, static_rocks, platform_width):
    moved_rocks = set()
    for moving_rock in sorted(list(moving_rocks), key=lambda x: x[0], reverse=True):
        moved_rocks.add(find_east_resting_spot(moving_rock, moved_rocks.union(static_rocks), platform_width))
    return moved_rocks


def find_east_resting_spot(moving_rock, static_rocks, platform_width):
    next_rock_east = min([static_rock[0] for static_rock in static_rocks
                          if static_rock[1] == moving_rock[1] and moving_rock[0] < static_rock[0]],
                         default=platform_width + 1)
    return min(next_rock_east - 1, platform_width), moving_rock[1]
