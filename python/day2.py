from typing import Self

from utils import read_text, test

# TIL: Python int division round toward negative infinity, not zero


class ComplexNumber:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: Self):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __mul__(self, other: Self):
        return ComplexNumber(
            self.x * other.x - self.y * other.y,
            self.x * other.y + self.y * other.x,
        )

    def __truediv__(self, other: Self):
        return ComplexNumber(int(self.x / other.x), int(self.y / other.y))

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"

    @classmethod
    def unwrap(cls, expr: str) -> Self:
        x, y = expr.removeprefix("[").removesuffix("]").split(",")
        return cls(int(x), int(y))


def get_test(filename):
    return ComplexNumber.unwrap(read_text(filename).split("=")[1])


def part1():
    a = get_test(test(2, 1))
    res = ComplexNumber(0, 0)

    for _ in range(3):
        res *= res
        res /= ComplexNumber(10, 10)
        res += a

    print("\tPart 1:", res)


def check_valid(P) -> bool:
    res = ComplexNumber(0, 0)
    for _ in range(100):
        res *= res
        res /= ComplexNumber(100000, 100000)
        res += P
        if abs(res.x) > 1_000_000 or abs(res.y) > 1_000_000:
            return False
    return True


def part2():
    a = get_test(test(2, 2))

    cnt = 0
    inputs = [
        ComplexNumber(i, j)
        for i in range(a.x, a.x + 1001, 10)
        for j in range(a.y, a.y + 1001, 10)
    ]

    cnt = sum(map(check_valid, inputs))
    print("\tPart 2:", cnt)


def part3():
    a = get_test(test(2, 2))

    cnt = 0
    inputs = [
        ComplexNumber(i, j)
        for i in range(a.x, a.x + 1001)
        for j in range(a.y, a.y + 1001)
    ]

    cnt = sum(map(check_valid, inputs))
    print("\tPart 3:", cnt)


def day2():
    print("Day 2:")
    part1()
    part2()
    part3()


if __name__ == "__main__":
    day2()
