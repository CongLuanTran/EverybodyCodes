from functools import reduce
from math import ceil

from utils import Solution, read_lines, test


def get_test(filename):
    return read_lines(filename)


class Day4(Solution):
    @staticmethod
    def part1():
        gears = get_test(test(4, 1))
        teeth = int(gears[0]) * 2025

        return teeth // int(gears[-1])

    @staticmethod
    def part2():
        gears = get_test(test(4, 2))
        teeth = int(gears[-1]) * 10_000_000_000_000

        return ceil(teeth / int(gears[0]))

    @staticmethod
    def part3():
        gears = get_test(test(4, 3))
        start = int(gears[0])
        end = int(gears[-1])
        end_teeth = reduce(
            lambda acc, line: acc * line[-1] // line[0],
            map(lambda line: list(map(int, line.split("|"))), gears[1:-1]),
            start * 100,
        )

        return end_teeth // end


if __name__ == "__main__":
    Day4.run()
