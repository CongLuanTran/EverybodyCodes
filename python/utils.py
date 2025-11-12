from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

basename = "everybody_codes_e2025"
test_folder = Path("../test/")


class Solution(ABC):
    @staticmethod
    @abstractmethod
    def part1():
        pass

    @staticmethod
    @abstractmethod
    def part2():
        pass

    @staticmethod
    @abstractmethod
    def part3():
        pass

    @classmethod
    def run(cls):
        print(f"{cls.__name__}:")
        print("\tPart1:", cls.part1())
        print("\tPart2:", cls.part2())
        print("\tPart3:", cls.part3())


def read_lines(filename: str | Path) -> List[str]:
    lines = Path(filename).read_text().splitlines()
    return [line.strip() for line in lines]


def read_text(filename: str | Path) -> str:
    return Path(filename).read_text().strip("\n")


def read_blocks(filename: str | Path) -> List[str]:
    text = read_text(filename)
    return text.split("\n\n")


def test(day: int, part: int):
    return test_folder / f"{basename}_q{day:02d}_p{part}.txt"
