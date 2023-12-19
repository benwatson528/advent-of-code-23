import operator
from dataclasses import dataclass

OPPOSITE_CONDITIONS = {operator.lt: operator.ge, operator.gt: operator.le}


def solve_p1(workflows, parts) -> int:
    return sum(sum(part.values()) for part in parts if process_part(part, "in", workflows))


def solve_p2(workflows) -> int:
    accepted_paths = find_all_paths(workflows)
    return -1


def process_part(part, workflow_name, workflows):
    if workflow_name in ('A', 'R'):
        return workflow_name == 'A'
    for rule in workflows[workflow_name][:-1]:
        if rule.condition(part[rule.category], rule.threshold):
            return process_part(part, rule.jump_to, workflows)
    return process_part(part, workflows[workflow_name][-1], workflows)


def find_all_paths(workflows):
    # Each path only hits a max of one tile per destination, map out all destinations
    accepted_paths = []
    for workflow_name in workflows.keys():
        accepted_paths.extend(chase_path(workflow_name, workflows))
    return accepted_paths


def chase_path(workflow_name, workflows):
    accepted_paths = []
    rejected_paths = []

    def chase_path_helper(workflow_name, conditions):
        # our end case
        if workflow_name in ('A', 'R'):
            if workflow_name == 'A':
                accepted_paths.append(conditions)
                return
            else:
                rejected_paths.append(conditions)
                return

        for rule in workflows[workflow_name][:-1]:
            # we take the condition but we also continue
            chase_path_helper(rule.jump_to, conditions + [f'{rule.category}{str(rule.condition)}{rule.threshold}'])
            conditions.append(f'{rule.category}{OPPOSITE_CONDITIONS[rule.condition]}{rule.threshold}')

        # go to the end too
        chase_path_helper(workflows[workflow_name][-1], conditions)

    chase_path_helper(workflow_name, [])
    return accepted_paths


@dataclass(frozen=True)
class Rule:
    category: str
    condition: operator
    threshold: int
    jump_to: str
