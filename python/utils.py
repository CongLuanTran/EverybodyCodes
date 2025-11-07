from pathlib import Path
from typing import List

basename = "everybody_codes_e2025"
test_folder = Path("../test/")


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
