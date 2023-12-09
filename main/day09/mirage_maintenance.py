def solve_p1(oasises) -> int:
    return sum(predict_right(oasis) for oasis in oasises)


def solve_p2(oasises) -> int:
    return sum(predict_left(oasis) for oasis in oasises)


def predict_right(oasis):
    return sum([ls[-1] for ls in build_sequences(oasis)])


def predict_left(oasis):
    current_first = 0
    for x in reversed([ls[0] for ls in build_sequences(oasis)]):
        current_first = x - current_first
    return current_first


def build_sequences(oasis):
    stack = [oasis]
    while len(set(stack[-1])) != 1:
        stack.append([b - a for a, b in zip(stack[-1], stack[-1][1:])])
    return stack
