target = {"xmin": 60, "xmax": 94, "ymin": -171, "ymax": -136}


class Probe:
    def __init__(self, xvel, yvel, x=0, y=0):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel

    def __repr__(self):
        return f"Probe loc {self.x},{self.y} at vel {self.xvel},{self.yvel}"

    def iterate(self):
        self.x += self.xvel
        self.y += self.yvel
        if self.xvel > 0:
            self.xvel -= 1
        self.yvel -= 1


def probe_in_target(probe):
    return (
        probe.x >= target["xmin"]
        and probe.x <= target["xmax"]
        and probe.y <= target["ymax"]
        and probe.y >= target["ymin"]
    )


x_intervals_min = 5
x_intervals_max = 96

y_intervals_min = -175
y_intervals_max = 175


max_y = 0
all_ys = {}


for y in range(y_intervals_min, y_intervals_max):
    for x in range(x_intervals_min, x_intervals_max):
        probe = Probe(x, y)
        possible_max_y = 0
        for t in range(2 * (y_intervals_max - y_intervals_min)):
            if probe.y > possible_max_y:
                possible_max_y = probe.y
            if probe_in_target(probe):
                all_ys[f"{x},{y}"] = all_ys.get(f"{x},{y}", 0) + 1
                if possible_max_y > max_y:
                    max_y = possible_max_y
            probe.iterate()


print("Part 1:", max_y)
print("Part 2:", len(all_ys))
