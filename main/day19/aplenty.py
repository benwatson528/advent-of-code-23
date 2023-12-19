import operator
from dataclasses import dataclass

OPPOSITE_CONDITIONS = {operator.lt: ">=", operator.gt: "<="}
STR_CONDITIONS = {operator.lt: "<", operator.gt: ">", operator.ge: ">=", operator.le: "<="}


def solve_p1(workflows, parts) -> int:
    return sum(sum(part.values()) for part in parts if process_part(part, "in", workflows))


def solve_p2(workflows) -> int:
    accepted_paths = chase_path("in", workflows)
    num_accepted_paths = 0
    for path in accepted_paths:
        upper = {'x': 4001, 'm': 4001, 'a': 4001, 's': 4001}
        lower = {'x': 1, 'm': 1, 'a': 1, 's': 1}
        for c in "xmas":
            new_upper, new_lower = identify_ranges(c, path, upper[c], lower[c])
            upper[c] = new_upper
            lower[c] = new_lower
        num_accepted_paths += ((upper['x'] - lower['x'])
                               * (upper['m'] - lower['m'])
                               * (upper['a'] - lower['a'])
                               * (upper['s'] - lower['s']))
    return num_accepted_paths


def chase_path(start_workflow, workflows):
    accepted_paths = []

    def chase_path_helper(workflow_name, conditions):
        if workflow_name in ('A', 'R'):
            if workflow_name == 'A':
                accepted_paths.append(conditions)
            return
        for rule in workflows[workflow_name][:-1]:
            chase_path_helper(rule.jump_to,
                              conditions + [(rule.category, STR_CONDITIONS[rule.condition], rule.threshold)])
            conditions.append((rule.category, OPPOSITE_CONDITIONS[rule.condition], rule.threshold))
        chase_path_helper(workflows[workflow_name][-1], conditions)

    chase_path_helper(start_workflow, [])
    return accepted_paths


def identify_ranges(c, path, upper, lower):
    for y in [category for category in path if category[0] == c]:
        if y[1] == '<=':
            upper = y[2] + 1 if upper == 4001 else min(upper, y[2] + 1)
        elif y[1] == '<':
            upper = y[2] if upper == 4001 else min(upper, y[2])
        elif y[1] == '>=':
            lower = y[2] if lower == 1 else max(lower, y[2])
        elif y[1] == '>':
            lower = y[2] + 1 if lower == 1 else max(lower, y[2] + 1)
    return upper, lower


def process_part(part, workflow_name, workflows):
    if workflow_name in ('A', 'R'):
        return workflow_name == 'A'
    for rule in workflows[workflow_name][:-1]:
        if rule.condition(part[rule.category], rule.threshold):
            return process_part(part, rule.jump_to, workflows)
    return process_part(part, workflows[workflow_name][-1], workflows)


@dataclass(frozen=True)
class Rule:
    category: str
    condition: operator
    threshold: int
    jump_to: str
