from math import inf

with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')

run_part_2 = True
if run_part_2:
    nodes = {}
    distances = {}
    unvisited = set()
    for i in range(5):
        for j in range(5):
            for y, line in enumerate(lines):
                for x, val in enumerate(line):
                    if (int(val) + i + j) % 10 != (int(val) + i + j):
                        node_val = (int(val) + i + j) % 10 + 1
                    else:
                        node_val = (int(val) + i + j)
                    nodes[(x + len(line) * i, y + len(lines) * j)] = node_val
                    distances[(x + len(line) * i, y + len(lines) * j)] = inf

    distances[(0, 0)] = 0
    unvisited.add((0, 0))

    visited = set()
    x_size = len(lines[0]) * 5
    y_size = len(lines) * 5
    total_size = x_size * y_size
else:
    nodes = {}
    distances = {}
    unvisited = set()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            nodes[(x, y)] = int(val)
            distances[(x, y)] = inf

    distances[(0, 0)] = 0
    unvisited.add((0, 0))

    visited = set()
    x_size = len(lines[0])
    y_size = len(lines)
    total_size = x_size * y_size

def calculate_surrounding_nodes(loc, visited, x_size, y_size):
    x = loc[0]
    y = loc[1]
    nodes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return remove_invalid_nodes(nodes, visited, x_size, y_size)


def remove_invalid_nodes(nodes, visited, x_size, y_size):
    valid_nodes = []
    for node in nodes:
        if node[0] < 0 or node[0] >= x_size or node[1] < 0 or node[1] >= y_size:
            continue
        if node in visited:
            continue
        valid_nodes.append(node)
    return valid_nodes


def find_min_node(distances, unvisited):
    min_node = ((), inf)
    for loc in unvisited:
        if distances[loc] < min_node[1]:
            min_node = (loc, distances[loc])

    return min_node[0]


starting_node = (0, 0)
ending_node = (x_size - 1, y_size - 1)

current_node = starting_node


while len(visited) < len(distances):
    surrounding_nodes = calculate_surrounding_nodes(current_node, visited, x_size, y_size)

    for node in surrounding_nodes:
        possible_distance = distances[current_node] + nodes[node]
        unvisited.add(node)
        if possible_distance < distances[node]:
            distances[node] = possible_distance

    visited.add(current_node)

    current_node = find_min_node(distances, unvisited)

    try:
        unvisited.remove(current_node)
    except:
        break
    if len(visited) % (x_size * 5) == 0:
        print("Visited", len(visited), "/", x_size * y_size)


if not run_part_2:
    print("Part 1:", distances[ending_node])
else:
    print("Part 2:", distances[ending_node])
