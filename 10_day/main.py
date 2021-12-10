with open('puzzle.txt', 'r') as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]


openings = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def find_bad_chars(line):
    stack = []
    for char in list(line):
        if char in openings:
            stack.append(char)
        else:
            valid_close = openings[stack.pop(-1)]
            if char != valid_close:
                return char

corrupted_chars = []
for line in lines:
    bad_char = find_bad_chars(line)
    if bad_char:
        corrupted_chars.append(bad_char)
answer = sum([points[char] for char in corrupted_chars])

print("Part 1:", answer)


# part 2

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def find_unfinished_lines(line):
    stack = []
    for char in list(line):
        if char in openings:
            stack.append(char)
        else:
            valid_close = openings[stack.pop(-1)]
            if char != valid_close:
                return None
    if stack:
        stack.reverse()
        return [openings[char] for char in stack]


unfinished_lines = []
for line in lines:
    unfinished_line = find_unfinished_lines(line)
    if unfinished_line:
        unfinished_lines.append(unfinished_line)

line_points_list = []
for unfinished_line in unfinished_lines:
    line_points = 0
    for char in unfinished_line:
        line_points *= 5
        line_points += points[char]
    line_points_list.append(line_points)

line_points_list = sorted(line_points_list)

middle = round(len(line_points_list) / 2)

middle_score = line_points_list[middle]

print("Part 2:", middle_score)
