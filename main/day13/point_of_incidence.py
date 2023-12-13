def solve_p1(patterns) -> int:
    return sum(find_reflection(rock) for rock in patterns)


def solve_p2(patterns) -> int:
    score = 0
    for pattern in patterns:
        score += change_pattern(pattern)
    return score


def change_pattern(pattern):
    previous_score = find_reflection(pattern)

    # try changing a rock to space
    for rock in pattern:
        changed_pattern = pattern.copy()
        changed_pattern.remove(rock)
        reflection = find_reflection(changed_pattern, previous_score)
        if reflection:
            return reflection

    # try changing a space to a rock
    max_x, max_y = max(x for x, y in pattern), max(y for x, y in pattern)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) not in pattern:
                changed_pattern = pattern.copy()
                changed_pattern.add((x, y))
                reflection = find_reflection(changed_pattern, previous_score)
                if reflection:
                    return reflection


def find_reflection(rock, previous_to_ignore=None):
    max_x, max_y = max(x for x, y in rock), max(y for x, y in rock)
    for reflection_line_y in range(max_y):
        if is_horizontal_reflection_line(reflection_line_y, rock, max_y):
            score = 100 * (reflection_line_y + 1)
            if previous_to_ignore != score:
                return score

    for reflection_line_x in range(max_x):
        if is_vertical_reflection_line(reflection_line_x, rock, max_x):
            score = reflection_line_x + 1
            if previous_to_ignore != score:
                return score


def is_horizontal_reflection_line(reflection_line_y, rock, max_y):
    line_above_ptr = reflection_line_y
    line_below_ptr = reflection_line_y + 1
    while line_above_ptr >= 0 and line_below_ptr <= max_y:
        if get_x_in_row(line_above_ptr, rock) != get_x_in_row(line_below_ptr, rock):
            return False
        line_above_ptr -= 1
        line_below_ptr += 1
    return True


def is_vertical_reflection_line(reflection_line_x, rock, max_x):
    left_ptr = reflection_line_x
    right_ptr = reflection_line_x + 1
    while left_ptr >= 0 and right_ptr <= max_x:
        if get_y_in_col(left_ptr, rock) != get_y_in_col(right_ptr, rock):
            return False
        left_ptr -= 1
        right_ptr += 1
    return True


def get_x_in_row(row, rock):
    return {x for x, y in rock if y == row}


def get_y_in_col(col, rock):
    return {y for x, y in rock if x == col}
