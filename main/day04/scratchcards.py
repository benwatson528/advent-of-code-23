def solve_p1(games) -> int:
    return sum(int(pow(2, find_matches(game) - 1)) for game in games)


def solve_p2(games) -> int:
    cards = {i: 1 for i in range(len(games))}
    for i, game in enumerate(games):
        num_matches = find_matches(game)
        for j in range(i + 1, i + 1 + num_matches):
            cards[j] = (cards[i] + cards[j])
    return sum(cards.values())


def find_matches(game):
    return len(game[0].intersection(game[1]))
