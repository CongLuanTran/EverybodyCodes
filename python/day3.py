from collections import Counter

from utils import Solution, read_text, test


def get_test(filename):
    return list(map(int, read_text(filename).split(",")))


class Day3(Solution):
    @staticmethod
    def part1():
        numbers = get_test(test(3, 1))
        return sum(set(numbers))

    @staticmethod
    def part2():
        numbers = get_test(test(3, 2))
        return sum(sorted(set(numbers))[:20])

    @staticmethod
    def part3():
        numbers = get_test(test(3, 3))
        return max(Counter(numbers).values())


if __name__ == "__main__":
    Day3.run()
