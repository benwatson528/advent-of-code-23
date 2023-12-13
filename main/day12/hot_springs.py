def solve(springs, multiplication_factor=1) -> int:
    expanded_springs = (expanded_spring(s, multiplication_factor) for s in springs)
    return sum(solve_spring([(conditions, damaged_runs)]) for conditions, damaged_runs in expanded_springs)


def expanded_spring(spring, multiplication_factor):
    return ((spring[0] + '?') * multiplication_factor)[:-1], spring[1] * multiplication_factor


def solve_spring(to_insert):
    solutions = set()
    print(to_insert[-1])
    seen = set()
    while to_insert:
        conditions, damaged_runs = to_insert.pop()
        if (conditions, len(damaged_runs)) in seen:
            continue
        seen.add((conditions, len(damaged_runs)))
        # if conditions.count('#') + conditions.count('?') < sum(damaged_runs):
        #     # kill a branch if there aren't enough #'s left to do all our remaining subs
        #     continue
        head, tail = damaged_runs[0], damaged_runs[1:]
        int_head = int(head)
        # P + 2 because we know we can't be touching a P directly
        for i in range(conditions.rindex('P') + 2 if 'P' in conditions else 0, len(conditions) - int_head + 1):
            if is_valid_placement(conditions, int_head, i):
                prefix = '' if i == 0 else conditions[:i - 1] + '.'
                suffix = '' if i + int_head == len(conditions) else '.' + conditions[i + int_head + 1:]
                updated_conditions = prefix + ('P' * int_head) + suffix
                if len(tail) == 0:
                    if '#' not in updated_conditions:
                        solutions.add(updated_conditions.replace('?', '.'))
                else:
                    to_insert.append((updated_conditions, tail))
            elif conditions[i] == '#':
                # we can kill a branch if we're not to place on a # - we must always place on the next #
                break
    return len(solutions)


def is_valid_placement(conditions, damaged_run, start_position):
    # (no P's in this method because we're always looking after the last P in the string)
    # if the element before isn't a broken spring
    if start_position > 0 and conditions[start_position - 1] == '#':
        return False

    end_position = start_position + damaged_run
    # if the element after isn't a broken spring
    if end_position < len(conditions) and conditions[end_position] == '#':
        return False

    # if any of the characters in the window are working springs
    if '.' in conditions[start_position:end_position]:
        return False
    return True

# FROM HERE BELOW IS A HALF-WORKING RECURSIVE SOLUTION
# def solve(springs, multiplication_factor=1) -> int:
#     print()
#     global SOLUTIONS
#     expanded_springs = (expanded_spring(s, multiplication_factor) for s in springs)
#     ans = 0
#     for conditions, damaged_runs in expanded_springs:
#         SOLUTIONS = set()
#         tmp = solve_spring_rec(conditions, damaged_runs, 0)
#         ans += len(SOLUTIONS)
#     return ans
#
#
# def expanded_spring(spring, multiplication_factor):
#     return ((spring[0] + '?') * multiplication_factor)[:-1], spring[1] * multiplication_factor
#
#
# @functools.cache
# def solve_spring_rec(conditions, damaged_runs, i):
#     if i >= len(conditions) or len(damaged_runs) == 0:
#         return set()
#
#     head, tail = damaged_runs[0], damaged_runs[1:]
#
#     if not can_place_run(conditions, head, i):
#         # we can't place anything in this position so keep looking
#         return solve_spring_rec(conditions, damaged_runs, i+1)
#     else:
#         head_int = int(head)
#         prefix = '' if i == 0 else conditions[:i - 1] + '.'
#         suffix = '' if i + head_int == len(conditions) else '.' + conditions[i + head_int + 1:]
#         updated_conditions = prefix + ('P' * head_int) + suffix
#         if len(tail) == 0:
#             SOLUTIONS.add(updated_conditions)
#         place_it = solve_spring_rec(updated_conditions, tail, i + head_int)
#         dont_place_it = solve_spring_rec(conditions, damaged_runs, i+1) if conditions[i] != '#' else set()
#         ret = place_it | dont_place_it
#         return ret
#
#
# def can_place_run(conditions, damaged_run, start_position):
#     trimmed_start = conditions[start_position:]
#     # if the element before isn't a broken spring
#     if start_position > 0 and conditions[start_position - 1] in ('#', 'P'):
#         return False
#
#     after_end = start_position + int(damaged_run)
#     # if the element after isn't a broken spring
#     if after_end < len(conditions) and conditions[after_end] == '#':
#         return False
#
#     # if any of the characters in the window are working springs
#     if '.' in conditions[start_position:after_end]:
#         return False
#     return True
