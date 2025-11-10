from utils import Solution, read_text, test


def get_test(filename):
    data = read_text(filename)
    x, y = data[3:-1].split(",")
    return complex(int(x), int(y))


def check_valid(P: complex) -> bool:
    res = 0 + 0j
    for _ in range(100):
        res *= res
        res = complex(int(res.real / 100000), int(res.imag / 100000))
        res += P
        if abs(res.real) > 1_000_000 or abs(res.imag) > 1_000_000:
            return False
    return True


class Day2(Solution):
    @staticmethod
    def part1():
        a = get_test(test(2, 1))
        res = 0 + 0j

        for _ in range(3):
            res *= res
            res = complex(int(res.real / 10), int(res.imag / 10))
            res += a

        print("\tPart 1:", res)

    @staticmethod
    def part2():
        a = get_test(test(2, 2))

        inputs = [
            complex(i, j)
            for i in range(int(a.real), int(a.real) + 1001, 10)
            for j in range(int(a.imag), int(a.imag) + 1001, 10)
        ]

        return sum(map(check_valid, inputs))

    @staticmethod
    def part3():
        a = get_test(test(2, 2))

        inputs = [
            complex(i, j)
            for i in range(int(a.real), int(a.real) + 1001)
            for j in range(int(a.imag), int(a.imag) + 1001)
        ]

        return sum(map(check_valid, inputs))


if __name__ == "__main__":
    Day2.run()
