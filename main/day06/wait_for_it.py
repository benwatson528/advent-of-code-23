import math


def solve(races) -> int:
    return math.prod(run_race(race_duration, record_distance) for race_duration, record_distance in races)


def run_race(race_duration, record_distance):
    return sum(1 for hold_time in range(race_duration + 1) if hold_time * (race_duration - hold_time) > record_distance)
