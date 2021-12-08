lanternfish = {x: 0 for x in range(9)}

with open('puzzle.py', 'r') as f:
    for fish in f.read().split(','):
        lanternfish[int(fish.strip())] += 1

def age_fish(lanternfish, days):
    for _ in range(days):
        new_lanternfish = {x: 0 for x in range(9)}
        for f in range(9):
            new_lanternfish[8 - f] = lanternfish[(9 - f) % 9]
        new_lanternfish[6] = new_lanternfish[6] + lanternfish[0]
        lanternfish = new_lanternfish
    return sum(lanternfish.values())

part_1 = age_fish(lanternfish, 80)
print("Part 1:", part_1)

part_2 = age_fish(lanternfish, 256)
print("Part 2:", part_2)
