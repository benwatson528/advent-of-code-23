import math


def solve_p1(games, max_cubes) -> int:
    return sum([i + 1 for i, game in enumerate(games) if play_round(game, max_cubes)])


def solve_p2(games) -> int:
    return sum(play_max_round(game) for game in games)


def play_round(game, max_cubes):
    return all(all(num_in_bag <= max_cubes[colour] for colour, num_in_bag in subset.items()) for subset in game)


def play_max_round(game):
    max_vals = {"red": 0, "green": 0, "blue": 0}
    for subset in game:
        for colour, num_in_bag in subset.items():
            max_vals[colour] = max(num_in_bag, max_vals[colour])
    return math.prod(max_vals.values())
