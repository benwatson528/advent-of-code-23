def solve(games) -> int:
    return sum(int(pow(2, len(game[0].intersection(game[1])) - 1)) for game in games)
