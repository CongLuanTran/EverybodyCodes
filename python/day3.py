from collections import Counter

from utils import read_text, test


def get_test(filename):
    return list(map(int, read_text(filename).split(",")))


def part1():
    numbers = get_test(test(3, 1))
    print("\tPart 1:", sum(set(numbers)))


def part2():
    numbers = get_test(test(3, 2))
    print("\tPart 2:", sum(sorted(set(numbers))[:20]))


def part3():
    numbers = get_test(test(3, 3))
    print("\tPart 3:", max(Counter(numbers).values()))


def day3():
    print("Day 3:")
    part1()
    part2()
    part3()


if __name__ == "__main__":
    day3()
