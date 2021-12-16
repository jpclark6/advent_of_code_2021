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


# loop
current_node = (0, 0)
while len(visited) < len(distances):
    surrounding_nodes = calculate_surrounding_nodes(current_node, visited, x_size, y_size)
    import pdb; pdb.set_trace()

    right_node = (1, 0)
    bottom_node = (0, 1)
    # left & top N/A

    distances[right_node] = nodes[right_node]
    distances[bottom_node] = nodes[bottom_node]

    visited.add(current_node)

    # next node with lowest value is (0, 1)
    # visit surrounding nodes that haven't been visited
    current_node = (0, 1)

    right_node = (1, 1)
    # not top node because it is in the list of visited nodes

    # add the distance to the next node to current node's distance
    distances[right_node] = distances[current_node] + nodes[right_node]

    visited.add(current_node)

    # next node with lowest value is (1, 0)
    # visit surrounding nodes that haven't been visited
    current_node = (1, 0)

    bottom_node = (1, 1)

    possible_distance = distances[current_node] + nodes[bottom_node]
    if possible_distance < distances[bottom_node]:
        distances[bottom_node] = possible_distance

    visited.add(current_node)

    # next node that hasn't been visited is (1, 1)
    # has no neighbors that haven't been visited
    # break

    # min distance will be the goal's coordinate value

    import pdb; pdb.set_trace()
