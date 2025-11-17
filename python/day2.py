from multiprocessing import Pool

from utils import file, read_text, time_taken


def get_test(part: int):
    data = read_text(file(2, part))
    x, y = data[3:-1].split(",")
    return int(x), int(y)


def check_valid(P: complex) -> bool:
    res = 0 + 0j
    for _ in range(100):
        res *= res
        res = complex(int(res.real / 100_000), int(res.imag / 100_000))
        res += P
        if abs(res.real) > 1_000_000 or abs(res.imag) > 1_000_000:
            return False
    return True


def part1(x: int, y: int):
    a = complex(x, y)
    res = 0 + 0j

    for _ in range(3):
        res *= res
        res = complex(int(res.real / 10), int(res.imag / 10))
        res += a

    return f"{int(res.real)} {int(res.imag)}"


def part2(x: int, y: int):
    a = complex(x, y)

    inputs = [
        complex(a.real + i, a.imag + j)
        for i in range(0, 1001, 10)
        for j in range(0, 1001, 10)
    ]

    return sum(map(check_valid, inputs))


def part3(x: int, y: int):
    a = complex(x, y)

    inputs = [
        complex(a.real + i, a.imag + j)
        for i in range(0, 1001)
        for j in range(0, 1001)
    ]

    pool = Pool()
    ans = pool.map(check_valid, inputs)
    pool.close()

    return sum(ans)


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(*get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(*get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(*get_test(3)))
