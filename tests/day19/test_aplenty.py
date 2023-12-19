import operator
import os
import re
from pathlib import Path

from main.day19.aplenty import solve_p1, solve_p2, Rule


def test_p1_simple():
    workflows, parts = read_input("data/test_input.txt")
    assert solve_p1(workflows, parts) == 19114


def test_p1_real():
    workflows, parts = read_input("data/input.txt")
    assert solve_p1(workflows, parts) == 395382


def test_p2_simple():
    workflows, parts = read_input("data/test_input.txt")
    assert solve_p2(workflows) == 167409079868000


def test_p2_real():
    workflows, parts = read_input("data/input.txt")
    assert solve_p2(workflows) == 103557657654583


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        splitter = lines.index('')
        workflows = process_workflows(lines[:splitter])
        parts = process_parts(lines[splitter + 1:])
        return workflows, parts


def process_workflows(lines):
    workflows = {}
    for line in lines:
        workflow_name = line.split('{')[0]
        rules = line.split('{')[1][:-1].split(',')
        parsed_rules = []
        for rule in rules:
            if ':' not in rule:
                parsed_rules.append(rule)
            else:
                category = rule[0]
                condition = operator.lt if rule[1] == '<' else operator.gt
                threshold = int(rule[2:].split(':')[0])
                jump_to = rule.split(':')[1]
                parsed_rules.append(Rule(category, condition, threshold, jump_to))
        workflows[workflow_name] = parsed_rules
    return workflows


def process_parts(lines):
    parts = []
    for part in lines:
        parts.append({rating.split('=')[0]: int(rating.split('=')[1]) for rating in re.findall(r'(.=\d+)', part)})
    return parts
