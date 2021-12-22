from copy import deepcopy
from collections import defaultdict, deque, namedtuple


class Scanner:
    def __init__(self, scanner):
        self.scanner = scanner
        self.beacons = []
        self.rotations = ""
        self.found = False
        self.r_map = "zzzzxzzzzxzzzzxzzzzxyzzzzyyzzzzy"
        self.location = [0, 0, 0]

    def __repr__(self):
        return f"  <S.{self.scanner}->{self.rotations}>  "

    def copy_beacons(self):
        self.beacons_copy = deepcopy(self.beacons)

    def reset_beacons(self):
        self.beacons = self.beacons_copy
        self.rotations = ""
        self.location = [0, 0, 0]

    def rotate_x(self):
        for beacon in self.beacons:
            x, y, z = beacon
            beacon[0], beacon[1], beacon[2] = x, -z, y
        self.rotations += "x"

    def rotate_neg_x(self):
        for beacon in self.beacons:
            x, y, z = beacon
            beacon[0], beacon[1], beacon[2] = x, z, -y
        self.rotations += "-x"

    def rotate_y(self):
        for beacon in self.beacons:
            x, y, z = beacon
            beacon[0], beacon[1], beacon[2] = z, y, -x
        self.rotations += "y"

    def rotate_neg_y(self):
        for beacon in self.beacons:
            x, y, z = beacon
            beacon[0], beacon[1], beacon[2] = -z, y, x
        self.rotations += "-y"

    def rotate_z(self):
        for beacon in self.beacons:
            x, y, z = beacon
            beacon[0], beacon[1], beacon[2] = -y, x, z
        self.rotations += "z"

    def rotate_neg_z(self):
        for beacon in self.beacons:
            x, y, z = beacon
            beacon[0], beacon[1], beacon[2] = y, -x, z
        self.rotations += "-z"

    def rotate_none(self):
        pass

    def translate(self, coords):
        x, y, z = coords
        for beacon in self.beacons:
            beacon[0] += x
            beacon[1] += y
            beacon[2] += z
        self.location[0] += x
        self.location[1] += y
        self.location[2] += z

    def r_hard_map(self):
        for r in list(self.r_map):
            if r == "x":
                self.rotate_x()
            elif r == "y":
                self.rotate_y()
            elif r == "z":
                self.rotate_z()
            yield r

    def rotate_from_string(self, dir):
        if dir[0] == "-":
            self.neg_rotate_from_string(dir[1:])
        else:
            for r in list(dir):
                if r == "x":
                    self.rotate_x()
                if r == "y":
                    self.rotate_y()
                if r == "z":
                    self.rotate_z()

    def neg_rotate_from_string(self, dir):
        for r in list(dir):
            if r == "x":
                self.rotate_neg_x()
            if r == "y":
                self.rotate_neg_y()
            if r == "z":
                self.rotate_neg_z()


#  parse input
with open("puzzle.txt", "r") as f:
    lines = f.read().split("\n")

scanners = []
beacons = []
for line in lines:
    if not line:
        scanner.beacons = beacons
        scanners.append(scanner)
        beacons = []
    elif "---" in line:
        scanner = Scanner(int(line.split("scanner ")[1].split(" ")[0]))
    else:
        point = [int(x) for x in line.split(",")]
        beacons.append(point)
scanner.beacons = beacons
scanners.append(scanner)

## for part 2 since location isn't working for some reason
for scanner in scanners:
    scanner.beacons.append([0, 0, 0])

def compare_scanners(s1, s2):
    found = False
    rotations = s1.r_hard_map()
    for r in rotations:
        if found:
            continue
        for s1_beacon in s1.beacons:
            if found:
                continue
            for s2_beacon in s2.beacons:
                matches = 0

                x_diff = s2_beacon[0] - s1_beacon[0]
                y_diff = s2_beacon[1] - s1_beacon[1]
                z_diff = s2_beacon[2] - s1_beacon[2]

                for s2_beacon_check in s2.beacons:
                    x = s2_beacon_check[0] - x_diff
                    y = s2_beacon_check[1] - y_diff
                    z = s2_beacon_check[2] - z_diff
                    if [x, y, z] in s1.beacons:
                        matches += 1

                if matches >= 12:
                    # print("Found match", s1.scanner, s2.scanner)
                    found = [
                        {
                            "scanner": s1,
                            "scanner_id": s1.scanner,
                            "rotations": s1.rotations,
                            "translation": [x_diff, y_diff, z_diff],
                        },
                        {
                            "scanner": s2,
                            "scanner_id": s2.scanner,
                            "rotations": "-" + s1.rotations[::-1],
                            "translation": [-x_diff, -y_diff, -z_diff],
                        },
                    ]
                    break
    return found


combinations = []
relationships = []
for scanner1 in scanners:
    for scanner2 in scanners:
        if scanner1 == scanner2:
            continue

        scanner1.copy_beacons()
        scanner2.copy_beacons()
        found = compare_scanners(scanner1, scanner2)
        if found:
            relationships.append(found)
        scanner1.reset_beacons()
        scanner2.reset_beacons()


def find_combine_order(dependencies):
    scanner_ids = [scanner.scanner for scanner in scanners]
    paths = []
    for scanner_id in scanner_ids:
        path = find_combine_path(scanner_id, dependencies, end=0)
        paths.append(path)
    return paths


def find_combine_path(start, dependencies, end=0):
    if start == end:
        return [start]
    keys = dependencies.keys()
    map = defaultdict(list)
    for k, v in keys:
        map[k].append(v)

    Path = namedtuple('Path', ['location', 'visited'])

    visited = []
    start = start
    end = end

    visited.append(start)
    to_check = deque()
    to_check.append(Path(start, visited))

    while to_check:
        current = to_check.pop()
        connected_caves = map[current.location]
        for cave in connected_caves:
            visited = list(current.visited)
            if cave in current.visited:
                continue
            if cave == end:
                visited.append(cave)
                return visited
            visited.append(cave)
            to_check.append(Path(cave, visited))
    raise Exception(f"Not found!!! {start} to {end}")


def transform_scanner(scanner, rotation, translation):
    scanner.rotate_from_string(rotation)
    scanner.translate(translation)

dependencies = {(s1["scanner_id"], s2["scanner_id"]):
    {
        "ending_coordinate_frame": s2["scanner_id"],
        "starting_coordinate_frame": s1["scanner_id"],
        "rotation": s1["rotations"],
        "translation": s1["translation"],
    }
    for s1, s2 in relationships
}

paths = find_combine_order(dependencies)

for path in paths:
    scanner = [scanner for scanner in scanners if scanner.scanner == path[0]][0]
    if scanner.scanner == 0:
        continue
    for x in range(len(path) - 1):
        key = (path[x], path[x+1])
        directions = dependencies[key]
        rotation = directions['rotation']
        translation = directions['translation']
        transform_scanner(scanner, rotation, translation)

beacons = set()
from pprint import pprint as pp
for scanner in scanners:
    for beacon in scanner.beacons:
        x, y, z = beacon
        beacons.add((x, y, z))

print("Part 1:", len(beacons) - len(scanners)) # remove scanners since we added extra point to each scanner


max_dist = 0
for scanner in scanners:
    for other_scanner in scanners:
        location = scanner.beacons[-1]
        other_location = other_scanner.beacons[-1]
        dist = abs(location[0] - other_location[0]) + abs(location[1] - other_location[1]) + abs(location[2] - other_location[2])
        if dist > max_dist:
            max_dist = dist

print("Part 2:", max_dist)
