from utils import file, read_text, time_taken


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.numbers = list(range(n + 1))
        self.size = [1] * (n + 1)

    def make_set(self, v):
        self.parent[v] = v

    def find_set(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]
            self.numbers[a] += self.numbers[b]


def get_test(part: int):
    return read_text(file(9, part))


def is_child(c: str, p1: str, p2: str):
    return all([c[i] == p1[i] or c[i] == p2[i] for i in range(len(c))])


def similarity(s1: str, s2: str):
    return sum([1 for i in range(len(s1)) if s1[i] == s2[i]])


def part1(note: str):
    dnas = list(map(lambda s: s.split(":")[1], note.splitlines()))
    for i in range(len(dnas)):
        for j in range(i + 1, len(dnas)):
            for k in range(j + 1, len(dnas)):
                a, b, c = dnas[i], dnas[j], dnas[k]
                if is_child(c, a, b):
                    return similarity(c, a) * similarity(c, b)
                elif is_child(b, a, c):
                    return similarity(b, a) * similarity(b, c)
                elif is_child(a, b, c):
                    return similarity(a, b) * similarity(a, c)


def part2(note: str):
    dnas = list(map(lambda s: s.split(":")[1], note.splitlines()))
    total = 0
    for i in range(len(dnas)):
        for j in range(i + 1, len(dnas)):
            for k in range(j + 1, len(dnas)):
                a, b, c = dnas[i], dnas[j], dnas[k]
                if is_child(c, a, b):
                    total += similarity(c, a) * similarity(c, b)
                elif is_child(b, a, c):
                    total += similarity(b, a) * similarity(b, c)
                elif is_child(a, b, c):
                    total += similarity(a, b) * similarity(a, c)

    return total


def part3(note: str):
    dnas = list(map(lambda s: s.split(":")[1], note.splitlines()))
    dsu = DSU(len(dnas))
    for i in range(len(dnas)):
        for j in range(i + 1, len(dnas)):
            for k in range(j + 1, len(dnas)):
                a, b, c = dnas[i], dnas[j], dnas[k]
                if is_child(c, a, b) or is_child(b, a, c) or is_child(a, b, c):
                    dsu.union_sets(i + 1, j + 1)
                    dsu.union_sets(j + 1, k + 1)

    return max(dsu.numbers)


def test_part1():
    note = """1:CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG
2:CTTGAATTGGGCCGTTTACCTGGTTTAACCAT
3:CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG"""
    assert part1(note) == 414, "Should be 414"


def test_part2():
    note = """1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG"""
    assert part2(note) == 1245, "Should be 1245"


def test_part3():
    note = """1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG
8:GGCGTAAAGTATGGATGCTGGCTAGGCACCCG"""
    assert part3(note) == 36, "Should be 36"


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3)))
