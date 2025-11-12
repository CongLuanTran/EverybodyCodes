import bisect
from itertools import accumulate
from utils import Solution, read_text, test


def get_item(filename):
    return read_text(filename).strip()


class Day6(Solution):
    @staticmethod
    def part1():
        data = get_item(test(6, 1))
        pairs = sum(accumulate(map(lambda p: p.count("a"), data.split("A")[:0:-1])))
        return pairs

    @staticmethod
    def part2():
        data = get_item(test(6, 2))
        pairs = sum(
            sum(accumulate(map(lambda p: p.count(ch), data.split(ch.upper())[:0:-1])))
            for ch in "abc"
        )
        return pairs

    @staticmethod
    def part3():
        data = get_item(test(6, 3))
        repeat = 1000
        data *= repeat
        distance = 1000
        pairs = 0

        mentor = {ch: [] for ch in "ABC"}
        novice = {ch: [] for ch in "abc"}
        for i, ch in enumerate(data):
            if ch in mentor:
                mentor[ch].append(i)
            elif ch in novice:
                novice[ch].append(i)

        for kind in novice:
            for n in novice[kind]:
                mentor_pos = mentor[kind.upper()]

                left = bisect.bisect_left(mentor_pos, max(0, n - distance))
                right = bisect.bisect_right(mentor_pos, min(len(data), n + distance))
                pairs += right - left

        return pairs


if __name__ == "__main__":
    Day6.run()
