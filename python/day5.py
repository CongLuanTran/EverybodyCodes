from functools import total_ordering

from utils import read_lines, file, time_taken


@total_ordering
class Segment:
    def __init__(self, mid):
        self.mid = mid
        self.left = None
        self.right = None

    def insert(self, num):
        if num < self.mid and not self.left:
            self.left = num
            return True
        if num > self.mid and not self.right:
            self.right = num
            return True
        return False

    def __score(self):
        return int(
            (str(self.left) if self.left else "")
            + str(self.mid)
            + (str(self.right) if self.right else "")
        )

    def __lt__(self, other):
        if not isinstance(other, Segment):
            return NotImplemented
        return self.__score() < other.__score()

    def __eq__(self, other):
        if not isinstance(other, Segment):
            return NotImplemented
        return self.__score() == other.__score()


@total_ordering
class Spine:
    def __init__(self):
        self.segments = []

    @classmethod
    def from_list(cls, list):
        spine = cls()
        for i in list:
            spine.insert(i)
        return spine

    def insert(self, num):
        for seg in self.segments:
            if seg.insert(num):
                return
        self.segments.append(Segment(num))

    def quality(self):
        return int("".join(map(lambda seg: str(seg.mid), self.segments)))

    def __lt__(self, other):
        if not isinstance(other, Spine):
            return NotImplemented
        if self.quality() == other.quality():
            return self.segments < other.segments
        return self.quality() < other.quality()

    def __eq__(self, other):
        if not isinstance(other, Spine):
            return NotImplemented
        if self.quality() == other.quality():
            return self.segments == other.segments
        return False


def get_test(part):
    return read_lines(file(5, part))


def part1(note: list[str]):
    _, nums = note[0].split(":")
    nums = list(map(int, nums.split(",")))
    spine = Spine.from_list(nums)

    return spine.quality()


def part2(note: list[str]):
    swords = []
    for line in note:
        _, nums = line.split(":")
        swords.append(Spine.from_list(list(map(int, nums.split(",")))).quality())

    best_sword = max(swords)
    worst_sword = min(swords)

    return best_sword - worst_sword


def part3(note: list[str]):
    swords = {}
    for line in note:
        i, nums = line.split(":")
        swords[int(i)] = Spine.from_list(list(map(int, nums.split(","))))
    swords = dict(
        sorted(
            swords.items(),
            key=lambda item: (item[1], item[0]),
            reverse=True,
        )
    )

    return sum([p * i for p, i in enumerate(swords.keys(), start=1)])


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3)))
