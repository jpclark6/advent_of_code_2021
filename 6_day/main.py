from copy import copy


lanternfish = {x: 0 for x in range(9)}

with open('puzzle.py', 'r') as f:
    for fish in f.read().split(','):
        lanternfish[int(fish.strip())] += 1

def age_fish(lanternfish, days):
    for _ in range(days):
        new_lanternfish = {x: 0 for x in range(9)}
        new_lanternfish[8] = lanternfish[0]
        new_lanternfish[7] = lanternfish[8]
        new_lanternfish[6] = lanternfish[7] + lanternfish[0]
        new_lanternfish[5] = lanternfish[6]
        new_lanternfish[4] = lanternfish[5]
        new_lanternfish[3] = lanternfish[4]
        new_lanternfish[2] = lanternfish[3]
        new_lanternfish[1] = lanternfish[2]
        new_lanternfish[0] = lanternfish[1]
        lanternfish = new_lanternfish

    return sum(lanternfish.values())

part_1 = age_fish(lanternfish, 80)
print("Part 1:", part_1)

part_2 = age_fish(lanternfish, 256)
print("Part 2:", part_2)