depths = []
with open('puzzle.txt', 'r') as f:
    for l in f:
        depths.append(int(l.strip()))

def count_increases(depths, rolling_window=1):
    increases = 0
    prev = sum(depths[0:rolling_window])
    for i, d in enumerate(depths[1:]):
        if sum(depths[i:i+rolling_window]) > prev:
            increases += 1
        prev = sum(depths[i:i+rolling_window])
    return increases

# part 1
print("Part 1:", count_increases(depths))

# part 2
rolling_window = 3
print("Part 2:", count_increases(depths, rolling_window=3))
