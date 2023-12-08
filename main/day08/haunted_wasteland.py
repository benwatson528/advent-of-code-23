from math import lcm


def solve_p1(directions, movements) -> int:
    i = 0
    current = ["AAA"]
    while current[0] != "ZZZ":
        current = move(directions, movements, current, i)
        i += 1
    return i


def solve_p2(directions, movements) -> int:
    i = 0
    current = [k for k in movements.keys() if k[2] == 'A']
    z_found = [0] * len(current)
    while True:
        for j, c in enumerate(current):
            if c[2] == 'Z' and z_found[j] == 0:
                z_found[j] = i
        if z_found.count(0) == 0:
            return lcm(*z_found)
        current = move(directions, movements, current, i)
        i += 1


def move(directions, movements, current, i):
    direction = directions[i % len(directions)]
    return [movements[c][0 if direction == 'L' else 1] for c in current]
