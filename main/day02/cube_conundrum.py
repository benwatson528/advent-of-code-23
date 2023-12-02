def solve(games, max_cubes) -> int:
    return sum([i + 1 for i, game in enumerate(games) if play_round(game, max_cubes)])


def play_round(game, max_cubes):
    return all(all(num_in_bag <= max_cubes[colour] for colour, num_in_bag in subset.items()) for subset in game)
