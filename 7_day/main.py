with open('puzzle.txt', 'r') as f:
    crabs = sorted([int(loc) for loc in f.read().strip().split(',')])


def move_crab(loc, destination, part_1=True):
    distance = abs(destination - loc)
    if part_1:
        return distance
    else:
        return distance * (distance + 1) / 2


def move_crabs(crabs, destination, part_1=True):
    total_fuel = sum([move_crab(loc, destination, part_1=part_1) for loc in crabs])
    return total_fuel


def brute_force(crabs, part_1=True):
    mini = min(crabs)
    maxi = max(crabs)
    min_fuel = None
    for destination in range(mini, maxi):
        total = move_crabs(crabs, destination, part_1=part_1)
        if not min_fuel:
            min_fuel = total
            continue
        if total < min_fuel:
            min_fuel = total
        else:
            return min_fuel


print("Part 1:", brute_force(crabs))
print("Part 2:", int(brute_force(crabs, part_1=False))) #  int for formatting only
