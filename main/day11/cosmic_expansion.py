import itertools


def solve(galaxies, expansion_factor) -> int:
    expanded_galaxies = expand_galaxies(galaxies, expansion_factor - 1)
    return sum([abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
                for g1, g2 in itertools.combinations(expanded_galaxies, 2)])


def expand_galaxies(galaxies, expansion_factor):
    max_galaxies = max(g[0] for g in galaxies), max(g[1] for g in galaxies)
    updated_galaxies = galaxies.copy()
    for row in [row for row in reversed(range(max_galaxies[1]))
                if row not in (y for _, y in galaxies)]:
        updated_galaxies = {(g[0], g[1] + expansion_factor)
                            if g[1] > row else (g[0], g[1])
                            for g in updated_galaxies}
    for col in [col for col in reversed(range(max_galaxies[0]))
                if col not in (x for x, _ in galaxies)]:
        updated_galaxies = {(g[0] + expansion_factor, g[1])
                            if g[0] > col else (g[0], g[1])
                            for g in updated_galaxies}
    return updated_galaxies
