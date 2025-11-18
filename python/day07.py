from collections import deque
from itertools import pairwise

from utils import file, read_text, time_taken


def get_test(part):
    return read_text(file(7, part))


def check_name(name, rules_map):
    for a, b in pairwise(name):
        if b not in rules_map.get(a, []):
            return False
    return True


def parse_rules(rules: str):
    return dict(
        map(
            lambda a: (a[0].strip(), a[1].strip().split(",")),
            map(lambda line: line.strip().split(">"), rules.splitlines()),
        )
    )


def part1(data: str):
    names, rules = data.split("\n\n")
    name_list = names.strip().split(",")
    rules_map = parse_rules(rules)
    correct_name = filter(lambda name: check_name(name, rules_map), name_list)
    return next(correct_name)


def part2(data: str):
    names, rules = data.split("\n\n")
    name_list = names.strip().split(",")
    rules_map = parse_rules(rules)
    return sum(
        i for i, name in enumerate(name_list, 1) if check_name(name, rules_map)
    )


def part3(data: str):
    names, rules = data.split("\n\n")
    name_list = names.strip().split(",")
    rules_map = parse_rules(rules)
    name_list = [name for name in name_list if check_name(name, rules_map)]
    name_list.sort()
    prefix_names = []
    for name in name_list:
        if not prefix_names or not name.startswith(prefix_names[-1]):
            prefix_names.append(name)

    cnt = 0
    for name in prefix_names:
        q = deque([name])
        while q:
            cur = q.popleft()

            for c in rules_map.get(cur[-1], []):
                new_name = cur + c
                if len(new_name) >= 7:
                    cnt += 1
                if len(new_name) >= 11:
                    continue
                q.append(new_name)

    return cnt


def test_part1():
    example = """Oronris,Urakris,Oroneth,Uraketh

r > a,i,o
i > p,w
n > e,r
o > n,m
k > f,r
a > k
U > r
e > t
O > r
t > h""".strip()
    assert part1(example) == "Oroneth", "Should be Oroneth"


def test_part2():
    example = """Xanverax,Khargyth,Nexzeth,Helther,Braerex,Tirgryph,Kharverax

r > v,e,a,g,y
a > e,v,x,r
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i""".strip()
    assert part2(example) == 23, "Should be 23"


def test_part3_small():
    example_small = """Xaryt

X > a,o
a > r,t
r > y,e,a
h > a,e,v
t > h
v > e
y > p,t""".strip()

    assert part3(example_small) == 25, "Should be 25"


def test_part3_large():
    example_large = """Khara,Xaryt,Noxer,Kharax

r > v,e,a,g,y
a > e,v,x,r,g
e > r,x,v,t
h > a,e,v
g > r,y
y > p,t
i > v,r
K > h
v > e
B > r
t > h
N > e
p > h
H > e
l > t
z > e
X > a
n > v
x > z
T > i""".strip()

    assert part3(example_large) == 1154, "Should be 1154"


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3)))
