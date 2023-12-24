import itertools

import z3
from sympy import Point, Segment


def solve_p1(hailstones, min_test_area, max_test_area) -> int:
    lines = [build_line(hailstone) for hailstone in hailstones]
    return sum(
        is_intersection(pair[0], pair[1], min_test_area, max_test_area) for pair in itertools.combinations(lines, 2))


def solve_p2(hailstones) -> int:
    calculator = z3.Solver()

    rock_x0 = z3.BitVec("rock_x0", 64)
    rock_y0 = z3.BitVec("rock_y0", 64)
    rock_z0 = z3.BitVec("rock_z0", 64)
    rock_vx = z3.BitVec("rock_vx", 64)
    rock_vy = z3.BitVec("rock_vy", 64)
    rock_vz = z3.BitVec("rock_vz", 64)

    for i, hailstone in enumerate(hailstones):
        (x0, y0, z0), (xv, yv, zv) = hailstone
        t = z3.BitVec(f't{i}', 64)
        calculator.add(t >= 0)
        calculator.add(rock_x0 + t * rock_vx == x0 + t * xv)
        calculator.add(rock_y0 + t * rock_vy == y0 + t * yv)
        calculator.add(rock_z0 + t * rock_vz == z0 + t * zv)
    calculator.check()
    return calculator.model().eval(rock_x0 + rock_y0 + rock_z0).as_long()


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
