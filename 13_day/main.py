from copy import deepcopy

with open("puzzle.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# points = [{'x': '6', 'y': '10'}, ....]
points = [
    {"x": int(p.split(",")[0]), "y": int(p.split(",")[1])}
    for p in lines[: lines.index("")]
]

# folds = [{'direction': 'y', 'location': 7}, ....]
folds = [
    {"direction": f.split("=")[0], "location": int(f.split("=")[1])}
    for f in [f.split(" ")[2] for f in lines[lines.index("") + 1 :]]
]


def print_map(points):
    max_x = max([p["x"] for p in points])
    max_y = max([p["y"] for p in points])
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if any([p["x"] == x and p["y"] == y for p in points]):
                line += "#"
            else:
                line += " "
        print(line)


def fold_map(points, fold):
    other_dir = {'x': 'y', 'y': 'x'}
    new_points = []
    location = fold['location']
    for point in points:
        direction = fold['direction']
        if point[direction] < location:
            if point not in new_points:
                new_points.append(point)
        else:
            new_loc = 2 * location - point[direction]
            new_point = {direction: new_loc, other_dir[direction]: point[other_dir[direction]]}
            if new_point not in new_points:
                new_points.append(new_point)

    return new_points


# part 1
points_copy = deepcopy(points)
answer = len(fold_map(points_copy, folds[0]))
print("Part 1:", answer)


# part 2
for fold in folds:
    points = fold_map(points, fold)

print('\nPart 2:\n')
print_map(points)
print()
