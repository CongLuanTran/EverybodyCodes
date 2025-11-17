from bisect import bisect_left, bisect_right, insort
from collections import defaultdict
from itertools import pairwise

from utils import file, read_text, time_taken


def get_test(part):
    return read_text(file(8, part))


def cross(a, b, c, d):
    a, b = sorted([a, b])
    c, d = sorted([c, d])
    return a < c < b < d or c < a < d < b


def part1(note: str, nails: int):
    sequence = map(int, note.split(","))
    return sum([1 for a, b in pairwise(sequence) if abs(b - a) == nails // 2])


def part2(note: str, nails: int):
    sequence = map(int, note.split(","))
    threads = defaultdict(list)
    for a, b in pairwise(sequence):
        insort(threads[a], b)
        insort(threads[b], a)
    total_knots = 0
    for a in range(1, nails + 1):
        if a not in threads:
            continue
        knot = 0
        for b in range(a + 2, nails + 1):
            upper_in = bisect_left(threads[b], b - 1)
            lower_in = bisect_right(threads[b], a)
            knot -= upper_in - lower_in
            upper_out = len(threads[b - 1]) - bisect_right(threads[b - 1], b)
            knot += upper_out
            if b in threads[a]:
                total_knots += knot
    return total_knots


def part3(note: str, nails: int):
    sequence = map(int, note.split(","))
    threads = defaultdict(list)
    for a, b in pairwise(sequence):
        insort(threads[a], b)
        insort(threads[b], a)
    max_cuts = 0
    for a in range(1, nails + 1):
        cuts = 0
        for b in range(a + 2, nails + 1):
            upper_in = bisect_left(threads[b], b - 1)
            lower_in = bisect_right(threads[b], a)
            cuts -= upper_in - lower_in
            upper_out = len(threads[b - 1]) - bisect_right(threads[b - 1], b)
            lower_out = bisect_left(threads[b - 1], a)
            cuts += upper_out + lower_out
            max_cuts = max(max_cuts, cuts + threads[a].count(b))

    return max_cuts


def test_part1():
    example = """1,5,2,6,8,4,1,7,3"""
    assert part1(example, 8) == 4, "Should be 4"


def test_part2():
    example = """1,5,2,6,8,4,1,7,3,5,7,8,2"""
    assert part2(example, 8) == 21, "Should be 21"


def test_part3():
    example = """1,5,2,6,8,4,1,7,3,6"""
    assert part3(example, 8) == 7, "Should be 7"


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1), 32))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2), 256))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3), 256))
