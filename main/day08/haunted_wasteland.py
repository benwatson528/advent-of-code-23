def solve(directions, movements) -> int:
    i = 0
    current = "AAA"
    while current != "ZZZ":
        direction = directions[i % len(directions)]
        current = movements[current][0 if direction == 'L' else 1]
        i += 1
    return i
