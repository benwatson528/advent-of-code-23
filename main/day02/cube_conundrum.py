def solve(games, max_cubes) -> int:
    return sum([i + 1 for i, game in enumerate(games) if play_round(game, max_cubes)])


def play_round(game, max_cubes):
    for subset in game:
        for colour, num_in_bag in subset.items():
            if max_cubes[colour] < num_in_bag:
                return False
    return True
