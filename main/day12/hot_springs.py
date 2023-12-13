def solve(springs, multiplication_factor=1) -> int:
    expanded_springs = (expanded_spring(s, multiplication_factor) for s in springs)
    return sum(solve_spring(conditions, damaged_runs) for conditions, damaged_runs in expanded_springs)


def expanded_spring(spring, multiplication_factor):
    return ((spring[0] + '?') * multiplication_factor)[:-1], spring[1] * multiplication_factor


def solve_spring(original_conditions, original_damaged_runs):
    cache = {}

    def solve_spring_rec(conditions, damaged_runs):
        if (conditions, tuple(damaged_runs)) in cache:
            return cache[(conditions, tuple(damaged_runs))]

        if len(damaged_runs) == 0:
            return 0 if '#' in conditions else 1

        if sum(int(x) for x in damaged_runs) > len(conditions):
            return 0

        ret = 0
        if can_place_run(conditions, damaged_runs[0]):
            if conditions[0] == '?':
                ret += solve_spring_rec(conditions[1:], damaged_runs)
            ret += solve_spring_rec(conditions[damaged_runs[0] + 1:], damaged_runs[1:])
        else:
            if conditions[0] == '#':
                return 0
            ret += solve_spring_rec(conditions[1:], damaged_runs)

        cache[(conditions, tuple(damaged_runs))] = ret
        return ret

    return solve_spring_rec(original_conditions, original_damaged_runs)


def can_place_run(conditions, damaged_run):
    # if the element after isn't a broken spring
    if damaged_run < len(conditions) and conditions[damaged_run] == '#':
        return False

    # if any of the characters in the window are working springs
    if '.' in conditions[:damaged_run]:
        return False
    return True
