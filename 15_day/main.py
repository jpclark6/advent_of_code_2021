from math import inf

with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')

nodes = {}
distances = {}
for y, line in enumerate(lines):
    for x, val in enumerate(line):
        nodes[(x, y)] = int(val)
        distances[(x, y)] = inf

distances[(0, 0)] = 0
visited = set()
x_size = len(lines[0])
y_size = len(lines)

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


def find_min_node(distances, visited):
    min_nodes = sorted(distances.items(), key=lambda x: x[1])
    for node in min_nodes:
        if node[0] not in visited:
            return node[0]


# loop
current_node = (0, 0)
while len(visited) < len(distances):
    surrounding_nodes = calculate_surrounding_nodes(current_node, visited, x_size, y_size)

    for node in surrounding_nodes:
        possible_distance = distances[current_node] + nodes[node]
        if possible_distance < distances[node]:
            distances[node] = possible_distance

    visited.add(current_node)

    current_node = find_min_node(distances, visited)

    if len(visited) % x_size == 0:
        print("Visited", len(visited), "/", x_size * y_size)


ending_node = (x_size - 1, y_size - 1)

print("Part 1:", distances[ending_node], distances[ending_node] == 613)

# real    0m33.875s