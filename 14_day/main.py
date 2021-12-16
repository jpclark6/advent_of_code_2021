with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')

start = lines[0]
keys = lines[2:]

#  keys = {'CH': 'B', 'HH': 'N', ...}
keys = {k[0]: k[1] for k in [k.split(' -> ') for k in keys]}


def insert_pairs(start, keys, number):
    start = '_' + start + '_'
    pairs = {}
    for i, x in enumerate(list(start)):
        if i == len(start) - 1:
            break
        pairs[x + start[i + 1]] = pairs.get(x + start[i + 1], 0) + 1

    for _ in range(number):
        next_pairs = {}
        for k, v in pairs.items():
            if keys.get(k):
                middle = keys[k]
                next_pairs[k[0] + middle] = next_pairs.get(k[0] + middle, 0) + pairs.get(k, 0)
                next_pairs[middle + k[1]] = next_pairs.get(middle + k[1], 0) + pairs.get(k, 0)
            else:
                next_pairs[k] = v
        pairs = next_pairs

    counts = make_counts(pairs)
    return max(counts.values()) - min(counts.values())


def make_counts(pairs):
    counts = {}
    for pair, count in pairs.items():
        letter = pair[0]
        if letter == '_':
            continue
        counts[letter] = counts.get(letter, 0) + count
    return counts

print("Part 1:", insert_pairs(start, keys, 10))
print("Part 2:", insert_pairs(start, keys, 40))
