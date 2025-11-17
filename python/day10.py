from collections import deque

from utils import file, read_lines, time_taken


def get_test(part: int):
    return read_lines(file(10, part))


moves = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]


def part1(matrix, lim):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    for i, line in enumerate(matrix):
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
                or y + dy >= len(matrix)
                or x + dx < 0
                or x + dx >= len(matrix[0])
                or visited[y + dy][x + dx]
            ):
                continue
            if n + 1 > lim:
                continue
            qu.append((n + 1, y + dy, x + dx))
            visited[y + dy][x + dx] = True
            if matrix[y + dy][x + dx] == "S":
                cnt += 1

    return cnt


def part2(matrix, lim):
    matrix = [list(line) for line in matrix]
    for i, line in enumerate(matrix):
        if "D" in line:
            mid_y = i
            mid_x = line.index("D")
    qu = deque()
    qu.append((0, mid_y, mid_x))
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


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1), 4))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2), 20))
