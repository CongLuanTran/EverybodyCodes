from utils import read_text, file, time_taken


def get_test(part: int):
    return read_text(file(6, part)).strip()


def part1(note: str):
    mentors = 0
    pairs = 0
    for ch in note:
        if ch == "A":
            mentors += 1
        elif ch == "a":
            pairs += mentors
    return pairs


def part2(note: str):
    mentors = [0, 0, 0]
    pairs = 0
    for ch in note:
        if ch.isupper():
            mentors[ord(ch) - ord("A")] += 1
        else:
            pairs += mentors[ord(ch.upper()) - ord("A")]

    return pairs


def part3(note: str):
    rep = 1000
    dist = 1000
    pairs = 0
    for i, ch in enumerate(note):
        if ch.islower():
            mentor = ch.upper()

            for j in range(-dist, dist + 1):
                offset = i + j
                pos = offset if offset < len(note) else offset % len(note)
                if note[pos] == mentor:
                    pairs += rep - (1 if offset < 0 or offset > len(note) else 0)

    return pairs


if __name__ == "__main__":
    print("Part 1:")
    time_taken(lambda: part1(get_test(1)))
    print("Part 2:")
    time_taken(lambda: part2(get_test(2)))
    print("Part 3:")
    time_taken(lambda: part3(get_test(3)))
