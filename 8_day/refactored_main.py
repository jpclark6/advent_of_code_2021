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
# SEGMENTS_KEY = {
#     0: [True, True, True, False, True, True, True],
#     1: [False, False, True, False, False, True, False],
#     2: [True, False, True, True, True, False, True],
#     3: [True, False, True, True, False, True, True],
#     4: [False, True, True, True, False, True, False],
#     5: [True, True, False, True, False, True, True],
#     6: [True, True, False, True, True, True, True],
#     7: [True, False, True, False, False, True, False],
#     8: [True, True, True, True, True, True, True],
#     9: [True, True, True, True, False, True, True],
# }

"""
The SEGMENTS_KEY is set up to represent which
bars need to be turned on to display the number.
It goes from top to bottom, left to right. First
digit in the binary is top, next is left top half,
then right top half, then middle, etc.

A "bar" is the LCD piece, such as top, or left top
half.
"""

NUMBER_TO_BARS = {
    0: '1110111',
    1: '0010010',
    2: '1011101',
    3: '1011011',
    4: '0111010',
    5: '1101011',
    6: '1101111',
    7: '1010010',
    8: '1111111',
    9: '1111011',
}
BARS_TO_NUMBER = {
    bar: number for number, bar in NUMBER_TO_BARS.items()
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
print("Part 1:", answer == 294)


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

def multiply_bars(bar_1, bar_2):
    new_bars = ''
    for i, b in enumerate(bar_1):
        if b == '1' and b == bar_2[i]:
            new_bars += '1'
        else:
            new_bars += '0'
    return new_bars

def eliminate_bars(remaining_bars, digits, number):
    rb = []
    bars_in_number = NUMBER_TO_BARS[number]
    for bars in remaining_bars:
        rb.append(multiply_bars(bars_in_number, bars))
        bars_in_number = bars_in_number[-1] + bars_in_number[:-1]
    return rb

digits_list = [line.replace(" |", "").split(" ") for line in lines]

answer = 0


for digits in digits_list:

    digits_possibilities = []
    for digit in digits:
        digits_possibilities.append(
            (
                "".join(sorted(list(digit))),
                [k for k, v in NUMBER_TO_BARS.items() if sum([int(x) for x in list(v)]) == len(digit)]
            )
        )
    remaining_bars = [string.ascii_lowercase[:7]] * 7

    digits_possibilities = sorted(digits_possibilities, key=lambda x: len(x[0]))

    for digit, possibilities in digits_possibilities:
        if possibilities == [1]:
            remaining_bars = eliminate_bars(remaining_bars, digits, 1)
        elif possibilities == [7]:
           remaining_bars = eliminate_bars(remaining_bars, digits, 7)
        elif possibilities == [4]:
            remaining_bars = eliminate_bars(remaining_bars, digits, 4)
        elif len(digit) == 5:
            if in_digit(remaining_bars[2], digit) and in_digit(remaining_bars[5], digit):
                # it's a 3
                remaining_bars = eliminate_bars(remaining_bars, digits, 3)
            elif in_digit(remaining_bars[1], digit) and in_digit(remaining_bars[3], digit):
                # it's a 5
                remaining_bars = eliminate_bars(remaining_bars, digits, 5)
            else:  # it's a 2
                remaining_bars = eliminate_bars(remaining_bars, digits, 2)


    final_four = digits[-4:]
    final_number = ""
    for number in final_four:
        bars_in_number = list(number)
        bars_binary = ''.join(['1' if x in bars_in_number else '0' for x in remaining_bars])
        final_number += str(BARS_TO_NUMBER[bars_binary])
    answer += int(final_number)

print("Part 2:", answer)
print("Part 2:", answer == 973292)
