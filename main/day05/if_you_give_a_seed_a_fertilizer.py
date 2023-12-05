def solve(seeds, conversions) -> int:
    return min(process_seed(conversions, seed) for seed in seeds)


def process_seed(conversions, source):
    for _, rows in conversions:
        for row in rows:
            if source in range(row[1], row[1] + row[2]):
                source = row[0] + (source - row[1])
                break
    return source
