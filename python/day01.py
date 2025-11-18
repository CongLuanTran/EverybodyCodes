from utils import file, read_blocks, time_taken


def get_test(part: int):
    [names, moves] = read_blocks(file(1, part))
    names = names.split(",")
    moves = moves.split(",")
    return names, moves


def part1(names: list[str], moves: list[str]):
    index = 0
    length = len(names) - 1

    for move in moves:
        if move[0] == "R":
            index = min(index + int(move[1:]), length)
        else:
            index = max(index - int(move[1:]), 0)

    return names[index]


def part2(names: list[str], moves: list[str]):
    index = 0
    length = len(names)

    for move in moves:
        if move[0] == "R":
            index = index + int(move[1:])
        else:
            index = index - int(move[1:])
    index %= length if index >= 0 else -length

    return names[index]


def part3(names: list[str], moves: list[str]):
    length = len(names)

    for move in moves:
        if move[0] == "R":
            index = int(move[1:])
        else:
            index = -int(move[1:])
        index %= length if index >= 0 else -length
        names[0], names[index] = names[index], names[0]

    return names[0]


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(*get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(*get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(*get_test(3)))
