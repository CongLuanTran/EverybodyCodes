from functools import total_ordering

from utils import Solution, read_lines, test


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


def get_item(filename):
    return read_lines(filename)


class Day5(Solution):
    @staticmethod
    def part1():
        data = get_item(test(5, 1))
        _, nums = data[0].split(":")
        nums = list(map(int, nums.split(",")))
        spine = Spine.from_list(nums)

        return spine.quality()

    @staticmethod
    def part2():
        data = get_item(test(5, 2))
        swords = []
        for line in data:
            _, nums = line.split(":")
            swords.append(
                Spine.from_list(list(map(int, nums.split(",")))).quality()
            )

        best_sword = max(swords)
        worst_sword = min(swords)

        return best_sword - worst_sword

    @staticmethod
    def part3():
        data = get_item(test(5, 3))
        swords = {}
        for line in data:
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
    Day5.run()
