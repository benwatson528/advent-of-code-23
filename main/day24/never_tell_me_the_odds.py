import itertools

from sympy import Point, Segment


def solve_p1(hailstones, min_test_area, max_test_area) -> int:
    lines = [build_line(hailstone) for hailstone in hailstones]
    return sum(
        is_intersection(pair[0], pair[1], min_test_area, max_test_area) for pair in itertools.combinations(lines, 2))


def solve_p2(hailstones) -> int:


def build_line(hailstone):
    return Segment(Point(hailstone[0][0], hailstone[0][1]),
                   Point(hailstone[0][0] + (40000000000000000 * hailstone[1][0]),
                         hailstone[0][1] + (40000000000000000 * hailstone[1][1])))


def is_intersection(l1, l2, min_test_area, max_test_area):
    intersection = l1.intersection(l2)
    if len(intersection) == 0:
        return False
    x, y = float(intersection[0][0]), float(intersection[0][1])
    return min_test_area <= x <= max_test_area and min_test_area <= y <= max_test_area
