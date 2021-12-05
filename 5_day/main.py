from pprint import pprint as pp
import re

filename = 'puzzle.txt'
with open(filename, 'r') as f:
    lines = f.readlines()
lines = [l.strip() for l in lines]

def pull_xy(line):
    m = re.match(r'(.*),(.*) -> (.*),(.*)', line)
    return [i for i in map(int, m.groups())]

# part 1
hv_lines = []
for line in lines:
    x1, y1, x2, y2 = pull_xy(line)
    if x1 == x2 or y1 == y2:
        hv_lines.append({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})

# part 2
hvd_lines = []
for line in lines:
    x1, y1, x2, y2 = pull_xy(line)
    hvd_lines.append({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2})

def add_points(lines, part):
    points = {}
    for line in lines:
        x1, x2, y1, y2 = line['x1'], line['x2'], line['y1'], line['y2']
        # import pdb; pdb.set_trace()
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for i in range(y2 - y1 + 1):
                points[f"{x1},{i + y1}"] = points.get(f"{x1},{i + y1}", 0) + 1
        elif y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for i in range(x2 - x1 + 1):
                points[f"{x1 + i},{y1}"] = points.get(f"{x1 + i},{y1}", 0) + 1
        else:
            if x2 < x1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            for i in range(x2 - x1 + 1):
                if y1 > y2:
                    points[f"{x1 + i},{y1 - i}"] = points.get(f"{x1 + i},{y1 - i}", 0) + 1
                else:
                    points[f"{x1 + i},{y1 + i}"] = points.get(f"{x1 + i},{y1 + i}", 0) + 1

    amount = 0
    for p, n in points.items():
        if n > 1:
            amount += 1
    print(f"Part {part}:", amount)

add_points(hv_lines, 1)
add_points(hvd_lines, 2)
