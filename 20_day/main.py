from copy import deepcopy

with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")

key = lines[0]
puzzle = [list(x) for x in lines[2:]]


def print_puzzle(puzzle):
    for y in puzzle:
        print("".join(y))
    print()


def add_padding(puzzle, size=3, padding="."):
    x = [padding] * len(puzzle[0])
    puzzle = [x] * size + puzzle + [x] * size
    new_puzzle = []
    for line in puzzle:
        x = [padding] * size
        new_line = x + line + x
        new_puzzle.append(new_line)
    return new_puzzle


def count_ons(puzzle):
    count = 0
    for line in puzzle:
        for c in line:
            if c == "#":
                count += 1
    return count


def find_letter(puzzle, x, y):
    line1 = puzzle[y - 1][x - 1 : x + 2]
    line2 = puzzle[y][x - 1 : x + 2]
    line3 = puzzle[y + 1][x - 1 : x + 2]
    code = "".join(line1 + line2 + line3).replace(".", "0").replace("#", "1")
    number = int(code, 2)
    return key[number]


def enhance(puzzle, steps):
    padding_size = 3
    for i in range(steps):
        if i % 2 == 0:
            padding = "."
        else:
            padding = "#"
        puzzle = add_padding(puzzle, size=padding_size, padding=padding)
        new_puzzle = deepcopy(puzzle)
        for y, line in enumerate(puzzle):
            for x, letter in enumerate(line):
                if y < 1 or y >= len(puzzle) - 1 or x < 1 or y >= len(line) - 1:
                    continue
                new_letter = find_letter(puzzle, x, y)
                new_puzzle[y][x] = new_letter

        if i % 2 == 0:
            padding = "#"
        else:
            padding = "."
        for y, line in enumerate(puzzle):
            for x, letter in enumerate(line):
                if (y > 1 and y < len(puzzle) - 2) and (x > 1 and x < len(line) - 2):
                    continue
                new_puzzle[y][x] = padding
        puzzle = new_puzzle
    return puzzle


puzzle = enhance(puzzle, 2)
print("Part 1:", count_ons(puzzle))

puzzle = [list(x) for x in lines[2:]]
puzzle = enhance(puzzle, 50)
print("Part 2:", count_ons(puzzle))
