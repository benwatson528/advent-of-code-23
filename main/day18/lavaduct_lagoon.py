DIRECTIONS = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}
DIRECTIONS_NUMERIC = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def solve(instructions, transformed=False) -> int:
    if transformed:
        instructions = transform_instructions(instructions)
    current = (0, 0)
    points = [current]
    for instruction in instructions:
        current = move(current, instruction[0], instruction[1], points)
    boundary_size = sum(instruction[1] for instruction in instructions)
    return shoelace(points, boundary_size)


def transform_instructions(instructions):
    updated_instructions = []
    for instruction in instructions:
        direction = DIRECTIONS_NUMERIC[instruction[2][-1]]
        num_steps = int(instruction[2][1:-1], 16)
        updated_instructions.append((direction, num_steps, instruction[2]))
    return updated_instructions


def move(current, direction, num_steps, points):
    direction_mover = DIRECTIONS[direction]
    next_coord = current[0] + (direction_mover[0] * num_steps), current[1] + (direction_mover[1] * num_steps)
    points.append(next_coord)
    return next_coord


def shoelace(points, boundary_size):
    s1 = s2 = 0
    for i in range(len(points) - 1):
        s1 += points[i][0] * points[i + 1][1]
        s2 += points[i][1] * points[i + 1][0]
    return ((abs(s1 - s2) + boundary_size) // 2) + 1
