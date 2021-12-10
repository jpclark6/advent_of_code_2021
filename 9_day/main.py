with open('puzzle.txt', 'r') as f:
    text = f.readlines()
PUZZLE = [[int(x) for x in list(t.strip())] for t in text]


def get_loc(x, y, puzzle):
    if x < 0 or y < 0:
        loc = 9
    else:
        try:
            loc = puzzle[y][x]
        except IndexError:
            loc = 9
    return loc

def get_surrounding(x, y, puzzle):
    px = get_loc(x + 1, y, puzzle)
    nx = get_loc(x - 1, y, puzzle)
    py = get_loc(x, y + 1, puzzle)
    ny = get_loc(x, y - 1, puzzle)
    return [px, nx, py, ny]

def is_minima(x, y, puzzle):
    loc = get_loc(x, y, puzzle)
    surrounding = get_surrounding(x, y, puzzle)
    for s in surrounding:
        if loc >= s:
            return False
    return True

minima = []

answer = 0
for y in range(len(PUZZLE)):
    for x in range(len(PUZZLE[y])):
        if is_minima(x, y, PUZZLE):
            minima.append((x, y))
            answer += get_loc(x, y, PUZZLE) + 1

print("Part 1:", answer)


# part 2

def traverse_outwards(minima, puzzle):
    basins = []

    for basin_minimum in minima:
        visited = set()
        to_look_at_next = set()
        to_look_at_next.add(basin_minimum)
        while len(to_look_at_next) != 0:
            current_loc = to_look_at_next.pop()
            for x_diff, y_diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = current_loc
                while x >= 0 and y >= 0 and x <= len(puzzle[0]) and y <= len(puzzle):
                    x += x_diff
                    y += y_diff
                    if (x, y) in visited or get_loc(x, y, puzzle) == 9:
                        break
                    to_look_at_next.add((x, y))
                x, y = current_loc
            visited.add(current_loc)
        basins.append(len(visited))
    largest_basins = sorted(basins, reverse=True)[:3]
    return largest_basins[0] * largest_basins[1] * largest_basins[2]


print("Part 2:", traverse_outwards(minima, PUZZLE))
