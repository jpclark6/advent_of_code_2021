from copy import deepcopy
import string


SEGMENTS = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

# segment values top to bottom, left to right
SEGMENTS_KEY = {
    0: [True, True, True, False, True, True, True],
    1: [False, False, True, False, False, True, False],
    2: [True, False, True, True, True, False, True],
    3: [True, False, True, True, False, True, True],
    4: [False, True, True, True, False, True, False],
    5: [True, True, False, True, False, True, True],
    6: [True, True, False, True, True, True, True],
    7: [True, False, True, False, False, True, False],
    8: [True, True, True, True, True, True, True],
    9: [True, True, True, True, False, True, True],
}

POSSIBILITIES = {}
for num, segment in SEGMENTS.items():
    POSSIBILITIES[segment] = 1 + POSSIBILITIES.get(segment, 0)

with open("puzzle.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

# part 1
answer = 0
outputs = [line.split(" | ")[1].strip().split(" ") for line in lines]
for line in outputs:
    for output in line:
        if POSSIBILITIES[len(output)] == 1:
            answer += 1

print("Part 1:", answer)


# part 2


def found_locations(bars):
    for v in bars.values():
        if sum(v) != 1:
            return False
    return True


def combine(one, two):
    combined = [x[0] and x[1] for x in zip(one, two)]
    # print(f'{one}\n{two}\n{combined}')
    return combined


def keep_bars(bars, digits):
    return "".join([b for b in bars if b in digits])


def remove_bars(bars, digits):
    return "".join([b for b in bars if b not in digits])


def in_digit(letters, digit):
    for letter in letters:
        if letter not in digit:
            return False
    return True


KEY = list(SEGMENTS_KEY.values())

digits_list = [line.replace(" |", "").split(" ") for line in lines]

answer = 0

for digits in digits_list:

    digits_possibilities = []
    for digit in digits:
        digits_possibilities.append(
            (
                "".join(sorted(list(digit))),
                [k for k, v in SEGMENTS_KEY.items() if sum(v) == len(digit)],
            )
        )
    bars = [string.ascii_lowercase[:7]] * 7

    digits_possibilities = sorted(digits_possibilities, key=lambda x: len(x[0]))

    for digit, possibilities in digits_possibilities:
        if possibilities == [1]:
            bars[2] = keep_bars(bars[2], digit)
            bars[5] = keep_bars(bars[5], digit)
            bars[0] = remove_bars(bars[0], digit)
            bars[1] = remove_bars(bars[1], digit)
            bars[3] = remove_bars(bars[3], digit)
            bars[4] = remove_bars(bars[4], digit)
            bars[6] = remove_bars(bars[6], digit)

        elif possibilities == [7]:
            bars[0] = keep_bars(bars[0], digit)
            bars[1] = remove_bars(bars[1], digit)
            bars[3] = remove_bars(bars[3], digit)
            bars[4] = remove_bars(bars[4], digit)
            bars[6] = remove_bars(bars[6], digit)

            bars[2] = keep_bars(bars[2], digit)
            bars[5] = keep_bars(bars[5], digit)

        elif possibilities == [4]:
            bars[1] = keep_bars(bars[1], digit)
            bars[2] = keep_bars(bars[2], digit)
            bars[3] = keep_bars(bars[3], digit)
            bars[5] = keep_bars(bars[5], digit)
            bars[4] = remove_bars(bars[4], digit)
            bars[6] = remove_bars(bars[6], digit)

            bars[0] = remove_bars(bars[0], digit)
        elif len(digit) == 5:
            if in_digit(bars[2], digit) and in_digit(bars[5], digit):
                # it's a 3
                bars[3] = keep_bars(bars[3], digit)
                bars[6] = keep_bars(bars[6], digit)
                bars[1] = remove_bars(bars[1], digit)
                bars[4] = remove_bars(bars[4], digit)
            elif in_digit(bars[1], digit) and in_digit(bars[3], digit):
                # it's a 5
                bars[5] = keep_bars(bars[5], digit)
                bars[6] = keep_bars(bars[6], digit)
                bars[2] = remove_bars(bars[2], digit)
                bars[4] = remove_bars(bars[4], digit)
            else:  # it's a 2
                bars[2] = keep_bars(bars[2], digit)
                bars[3] = keep_bars(bars[3], digit)
                bars[1] = remove_bars(bars[1], digit)
                bars[5] = remove_bars(bars[5], digit)

    for bar in bars:
        if len(bar) != 1:
            import pdb

            pdb.set_trace()

    final_four = digits[-4:]
    number = ""
    for fin in final_four:
        fin = list(fin)
        truth_map = [x in fin for x in bars]
        number += str(KEY.index(truth_map))
    answer += int(number)

print("Part 2:", answer)
