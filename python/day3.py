from collections import Counter

from utils import file, read_text, time_taken


def get_test(part: int):
    return list(map(int, read_text(file(3, part)).split(",")))


def part1(numbers: list[int]):
    return sum(set(numbers))


def part2(numbers: list[int]):
    return sum(sorted(set(numbers))[:20])


def part3(numbers: list[int]):
    return max(Counter(numbers).values())


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3)))
