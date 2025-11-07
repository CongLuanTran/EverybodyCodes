from functools import reduce
from math import ceil

from utils import read_lines, test


def get_test(filename):
    return read_lines(filename)


def part1():
    gears = get_test(test(4, 1))
    teeth = int(gears[0]) * 2025

    print("\tPart 1:", teeth // int(gears[-1]))


def part2():
    gears = get_test(test(4, 2))
    teeth = int(gears[-1]) * 10_000_000_000_000

    print("\tPart 2:", ceil(teeth / int(gears[0])))


def part3():
    gears = get_test(test(4, 3))
    start = int(gears[0])
    end = int(gears[-1])
    end_teeth = reduce(
        lambda acc, line: acc * line[-1] // line[0],
        map(lambda line: list(map(int, line.split("|"))), gears[1:-1]),
        start * 100,
    )

    print("\tPart 3:", end_teeth // end)


def day4():
    print("Day 4:")
    part1()
    part2()
    part3()


if __name__ == "__main__":
    day4()
