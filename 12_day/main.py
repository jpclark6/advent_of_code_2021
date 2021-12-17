from collections import defaultdict, namedtuple, deque

with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')

map = defaultdict(list)
for line in lines:
    p1, p2 = line.split('-')
    map[p1].append(p2)
    map[p2].append(p1)

Path = namedtuple('Path', ['location', 'visited', 'twice'])

visited = set()
start = 'start'
end = 'end'
unvisited = set()
path_options = 0

visited.add(start)
to_check = deque()
to_check.append(Path(start, visited, False))

while to_check:
    current = to_check.pop()
    connected_caves = map[current.location]
    for cave in connected_caves:
        if cave in current.visited:
            continue
        if cave == end:
            path_options += 1
            continue
        visited = set(current.visited)
        if cave.islower():
            visited.add(cave)
        to_check.append(Path(cave, visited, True))

print("Part 1:", path_options)


visited = set()
start = 'start'
end = 'end'
unvisited = set()
path_options = 0

visited.add(start)
to_check = [Path(start, visited, False)]

while to_check:
    current = to_check.pop()
    connected_caves = map[current.location]
    for cave in connected_caves:
        visited = set(current.visited)
        twice = current.twice
        if cave in visited and twice:
            continue
        if cave == end:
            path_options += 1
            continue
        if cave == start:
            continue
        if cave.islower():
            if cave in visited:
                twice = cave
            visited.add(cave)
        to_check.append(Path(cave, visited, twice))

print("Part 2:", path_options)