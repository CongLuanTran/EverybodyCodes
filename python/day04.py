from functools import reduce
from math import ceil

from utils import file, read_lines, time_taken


def get_test(part: int):
    return read_lines(file(4, part))


def part1(gears: list[str]):
    return int(gears[0]) * 2025 // int(gears[-1])


def part2(gears: list[str]):
    return ceil(int(gears[-1]) * 10_000_000_000_000 / int(gears[0]))


def part3(gears: list[str]):
    start = int(gears[0])
    end = int(gears[-1])
    end_teeth = reduce(
        lambda acc, line: acc * line[-1] // line[0],
        map(lambda line: list(map(int, line.split("|"))), gears[1:-1]),
        start * 100,
    )

    return end_teeth // end


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3)))
