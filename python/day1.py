from utils import Solution, read_blocks, test


def get_test(filename):
    [names, moves] = read_blocks(filename)
    names = names.split(",")
    moves = moves.split(",")
    return names, moves


class Day1(Solution):
    @staticmethod
    def part1():
        names, moves = get_test(test(1, 1))
        index = 0
        length = len(names) - 1

        for move in moves:
            if move[0] == "R":
                index = min(index + int(move[1:]), length)
            else:
                index = max(index - int(move[1:]), 0)

        return names[index]

    @staticmethod
    def part2():
        names, moves = get_test(test(1, 2))
        index = 0
        length = len(names)

        for move in moves:
            if move[0] == "R":
                index = index + int(move[1:])
            else:
                index = index - int(move[1:])
        index %= length if index >= 0 else -length

        return names[index]

    @staticmethod
    def part3():
        names, moves = get_test(test(1, 3))
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
    Day1.run()
