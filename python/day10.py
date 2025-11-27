import sys
from collections import deque
from functools import cache
from typing import Tuple

from utils import file, read_lines, time_taken

sys.setrecursionlimit(10**9)


def get_test(part: int):
    return read_lines(file(10, part))


moves = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]


def part1(note: list[str], lim: int):
    visited = [[False] * len(note[0]) for _ in range(len(note))]
    for i, line in enumerate(note):
        if "D" in line:
            mid_y = i
            mid_x = line.index("D")
    qu = deque()
    qu.append((0, mid_y, mid_x))
    visited[mid_y][mid_x] = True
    cnt = 0
    while qu:
        n, y, x = qu.popleft()
        for dy, dx in moves:
            if (
                y + dy < 0
                or y + dy >= len(note)
                or x + dx < 0
                or x + dx >= len(note[0])
                or visited[y + dy][x + dx]
            ):
                continue
            if n + 1 > lim:
                continue
            qu.append((n + 1, y + dy, x + dx))
            visited[y + dy][x + dx] = True
            if note[y + dy][x + dx] == "S":
                cnt += 1

    return cnt


def part2(note: list[str], lim: int):
    matrix = [list(line) for line in note]
    for i, line in enumerate(matrix):
        if "D" in line:
            sy = i
            sx = line.index("D")
    qu = deque()
    qu.append((0, sy, sx))
    s = set()
    cnt = 0
    while qu:
        n, y, x = qu.popleft()
        for dy, dx in moves:
            if (
                y + dy < 0
                or y + dy >= len(matrix)
                or x + dx < 0
                or x + dx >= len(matrix[0])
            ):
                continue
            if n + 1 > lim:
                continue
            if (n + 1, y + dy, x + dx) not in s:
                qu.append((n + 1, y + dy, x + dx))
                s.add((n + 1, y + dy, x + dx))

    for n, y, x in s:
        if matrix[y][x] == "#":
            continue
        if y >= n - 1 and matrix[y - n + 1][x] == "S":
            cnt += 1
            matrix[y - n + 1][x] = "."
        if y >= n and matrix[y - n][x] == "S":
            cnt += 1
            matrix[y - n][x] = "."

    return cnt


GameState = Tuple[Tuple[int, int], Tuple[int | None, ...]]


def part3(note: list[str]):
    matrix = [list(line) for line in note]
    hideouts = []
    for y, line in enumerate(matrix):
        if "D" in line:
            sy = y
            sx = line.index("D")
        for x, c in enumerate(line):
            if c == "#":
                hideouts.append((x, y))
    sheeps = [0 if c == "S" else None for c in matrix[0]]

    inti_state = ((sx, sy), tuple(sheeps))

    @cache
    def move(state: GameState):
        drx, dry = state[0]
        sheeps = list(state[1])

        for x, s in enumerate(sheeps):
            if s is None:
                continue
            if s >= len(matrix):
                return 0
            if all((x, y) in hideouts for y in range(s, len(matrix))):
                return 0

        if sheeps[drx] == dry and (drx, dry) not in hideouts:
            sheeps[drx] = None

        if all(s is None for s in sheeps):
            return 1

        if all(s == len(matrix) - 1 for s in sheeps if s is not None):
            return 0

        possible_sheep_moves = []
        for x, y in enumerate(sheeps):
            if y is None:
                continue
            sx, sy = x, y + 1
            if sx == drx and sy == dry and (sx, sy) not in hideouts:
                continue
            nsheeps = list(sheeps)
            nsheeps[sx] = sy
            possible_sheep_moves.append(nsheeps)

        possible_dragon_moves = []
        for dy, dx in moves:
            nx = drx + dx
            ny = dry + dy
            if 0 > nx or nx >= len(matrix[0]) or 0 > ny or ny >= len(matrix):
                continue
            possible_dragon_moves.append((nx, ny))

        if not possible_sheep_moves:
            return sum(
                move((dmove, tuple(sheeps))) for dmove in possible_dragon_moves
            )

        return sum(
            move((dmove, tuple(smove)))
            for smove in possible_sheep_moves
            for dmove in possible_dragon_moves
        )

    return move(inti_state)


def test_part1():
    data = """...SSS.......
    .S......S.SS.
    ..S....S...S.
    ..........SS.
    ..SSSS...S...
    .....SS..S..S
    SS....D.S....
    S.S..S..S....
    ....S.......S
    .SSS..SS.....
    .........S...
    .......S....S
    SS.....S..S.. """.splitlines()
    data = [line.strip() for line in data]
    assert part1(data, 3) == 27, "Should be 27"


def test_part2():
    data = """...SSS##.....
    .S#.##..S#SS.
    ..S.##.S#..S.
    .#..#S##..SS.
    ..SSSS.#.S.#.
    .##..SS.#S.#S
    SS##.#D.S.#..
    S.S..S..S###.
    .##.S#.#....S
    .SSS.#SS..##.
    ..#.##...S##.
    .#...#.S#...S
    SS...#.S.#S..""".splitlines()
    data = [line.strip() for line in data]
    assert part2(data, 3) == 27, "Should be 27"


def test_part3_1():
    data = """SSS
..#
#.#
#D.""".splitlines()
    data = [line.strip() for line in data]
    assert part3(data) == 15, "Should be 15"


def test_part3_2():
    data = """SSS
..#
..#
.##
.D#""".splitlines()
    data = [line.strip() for line in data]
    assert part3(data) == 8, "Should be 8"


def test_part3_3():
    data = """..S..
.....
..#..
.....
..D..""".splitlines()
    data = [line.strip() for line in data]
    assert part3(data) == 44, "Should be 44"


def test_part3_4():
    data = """.SS.S
#...#
...#.
##..#
.####
##D.#""".splitlines()
    data = [line.strip() for line in data]
    assert part3(data) == 4406, "Should be 4406"


def test_part3_5():
    data = """SSS.S
.....
#.#.#
.#.#.
#.D.#""".splitlines()
    data = [line.strip() for line in data]
    assert part3(data) == 13033988838, "Should be 13033988838"


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1), 4))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2), 20))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3)))
