def solve_p1(seeds, conversions) -> int:
    return min(process_seed(conversions, seed) for seed in seeds)


def solve_p2(seeds, conversions) -> int:
    reversed_conversions = reverse_conversions(conversions)
    seed_ranges = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    i = 0
    while True:
        seed_val = process_seed(reversed_conversions, i)
        if any(seed_val in r for r in seed_ranges):
            return i
        i += 1


def reverse_conversions(conversions):
    reversed_conversions = []
    for conversion_name, conversion in reversed(conversions):
        reversed_conversions.append((conversion_name, [(row[1], row[0], row[2]) for row in conversion]))
    return reversed_conversions


def process_seed(conversions, source):
    for _, rows in conversions:
        for row in rows:
            if source in range(row[1], row[1] + row[2]):
                source = row[0] + (source - row[1])
                break
    return source
