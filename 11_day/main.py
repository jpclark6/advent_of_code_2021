from copy import deepcopy

with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')
lines = [[int(x) for x in list(l)] for l in lines]


def add_one(lines):
    return [[x + 1 for x in line] for line in lines]


def flash(x, y, lines):
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
    ]
    for x_diff, y_diff in directions:
        new_x = x + x_diff
        new_y = y + y_diff
        if new_x < 0 or new_y < 0 or new_x >= len(lines[0]) or new_y >= len(lines):
            continue
        if lines[y + y_diff][x + x_diff] != -1:
           lines[y + y_diff][x + x_diff] += 1
    lines[y][x] = -1

    return lines


def reset(lines):
    new_flashes = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == -1:
                lines[y][x] = 0
                new_flashes += 1
    return lines, new_flashes


def count_flashes(lines):
    new_flashes = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == -1:
                new_flashes += 1
    return new_flashes


def find_9_plus_and_flash(lines):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] > 9:
                return flash(x, y, lines)


def step(lines, steps):
    flashes = 0
    for step in range(1, steps + 1):
        lines = add_one(lines)
        while any([item > 9 for sublist in lines for item in sublist]):
            lines = find_9_plus_and_flash(lines)
        lines, new_flashes = reset(lines)
        flashes += new_flashes
        if all([item == 0 for sublist in lines for item in sublist]):
            print("Part 2:", step)
            return
    print("Part 1:", flashes)
    return


def print_map(lines):
    for y in lines:
        y = [(' ' + str(x))[-2:] for x in y]
        print(','.join(y))
    print()


# part 1
step(lines, 100)

# part 2
step(lines, 2000)
