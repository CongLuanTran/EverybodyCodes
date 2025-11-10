from functools import total_ordering

from utils import read_lines, test


@total_ordering
class Spine:
    def __init__(self):
        self.left = None
        self.mid = None
        self.right = None
        self.next = None

    @classmethod
    def from_list(cls, list):
        spine = cls()
        for i in list:
            spine.insert(i)
        return spine

    def insert(self, num):
        if not self.mid:
            self.mid = num
        elif num < self.mid and not self.left:
            self.left = num
        elif num > self.mid and not self.right:
            self.right = num
        else:
            if not self.next:
                self.next = Spine()
            self.next.insert(num)

    def __quality(self):
        if not self.next:
            return str(self.mid)
        return str(self.mid) + self.next.__quality()

    def quality(self):
        return int(self.__quality())

    def __score(self):
        score = str(self.mid)
        if self.left:
            score = str(self.left) + score
        if self.right:
            score += str(self.right)
        return int(score)

    def __lt__(self, other):
        if not isinstance(other, Spine):
            return NotImplemented
        if self.quality() == other.quality():
            a = self
            b = other
            while a and b:
                if a.__score() == b.__score():
                    a = a.next
                    b = b.next
                    continue
                return a.__score() < b.__score()
        return self.quality() < other.quality()

    def __eq__(self, other):
        if not isinstance(other, Spine):
            return NotImplemented
        if self.quality() != other.quality():
            return False
        a = self
        b = other
        while a and b:
            if a.__score() != b.__score():
                return False
            a = a.next
            b = b.next
        return True


def get_item(filename):
    return read_lines(filename)


def part1():
    data = get_item(test(5, 1))
    _, nums = data[0].split(":")
    nums = list(map(int, nums.split(",")))
    spine = Spine.from_list(nums)

    return spine.quality()


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


def part3():
    data = get_item(test(5, 3))
    swords = {}
    for line in data:
        i, nums = line.split(":")
        swords[int(i)] = Spine.from_list(list(map(int, nums.split(","))))
    swords = dict(
        sorted(
            swords.items(), key=lambda item: (item[1], item[0]), reverse=True
        )
    )

    return sum([p * i for p, i in enumerate(swords.keys(), start=1)])


def day5():
    print("Day 5:")
    print("\tPart 1:", part1())
    print("\tPart 2:", part2())
    print("\tPart 3:", part3())


if __name__ == "__main__":
    day5()
