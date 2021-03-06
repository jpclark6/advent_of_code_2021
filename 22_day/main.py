from uuid import uuid4
from pprint import pprint as pp

with open("puzzle.txt") as f:
    lines = f.read().split("\n")


# part_1 = True
part_1 = False


class Square:
    def __init__(self, dims):
        self.x_min = dims["x_min"]
        self.x_max = dims["x_max"]
        self.y_min = dims["y_min"]
        self.y_max = dims["y_max"]
        self.z_min = dims["z_min"]
        self.z_max = dims["z_max"]

        self.id = str(uuid4())
        self.instruction = dims.get("instruction", "off")

    def __repr__(self) -> str:
        return f"<{self.instruction}({self.x_min}..{self.x_max}, {self.y_min}..{self.y_max}, {self.z_min}..{self.z_max})>"

    @property
    def volume(self):
        return (self.x_max - self.x_min) * (self.y_max - self.y_min) * (self.z_max - self.z_min)



class MiniSquare(Square):
    def __init__(self, dims):
        super().__init__(dims)
        self.squares = None


def count_ons(mini_squares):
    running_total = 0
    for mini_square in mini_squares:
        if mini_square.instruction == 'on':
            running_total += mini_square.volume
    return running_total


lines = [line.split("=") for line in lines]
squares = []
for line_raw in lines:
    line = line_raw[1:]
    square = []
    for l in line:
        square.append(l.split(",")[0])
    square_obj = Square(
        {
            "x_min": int(square[0].split("..")[0]) - .5,
            "x_max": int(square[0].split("..")[1]) + .5,
            "y_min": int(square[1].split("..")[0]) - .5,
            "y_max": int(square[1].split("..")[1]) + .5,
            "z_min": int(square[2].split("..")[0]) - .5,
            "z_max": int(square[2].split("..")[1]) + .5,
            "instruction": line_raw[0].split(" ")[0],
        }
    )
    dims = [int(square[0].split("..")[0]),
            int(square[0].split("..")[1]),
            int(square[1].split("..")[0]),
            int(square[1].split("..")[1]),
            int(square[2].split("..")[0]),
            int(square[2].split("..")[1])]
    if part_1:
        if any([(abs(x) > 50) for x in dims]):
            continue
        else:
            squares.append(square_obj)
    else:
        squares.append(square_obj)

all_x = set()
all_y = set()
all_z = set()

for square in squares:
    all_x.add(square.x_min)
    all_x.add(square.x_max)
    all_y.add(square.y_min)
    all_y.add(square.y_max)
    all_z.add(square.z_min)
    all_z.add(square.z_max)

print("x", len(all_x))
print("y", len(all_y))
print("z", len(all_z))

all_x = sorted(list(all_x))
all_y = sorted(list(all_y))
all_z = sorted(list(all_z))

mini_squares = []

for i, x in enumerate(all_x):
    print(round(i / len(all_x), 5), "%", "Finished", len(mini_squares), "mini squares")
    if i == len(all_x) - 1:
        continue
    for j, y in enumerate(all_y):
        if j == len(all_y) - 1:
            continue
        for k, z in enumerate(all_z):
            if k == len(all_z) - 1:
                continue
            x_min = x
            x_max = all_x[i + 1]
            y_min = y
            y_max = all_y[j + 1]
            z_min = z
            z_max = all_z[k + 1]

            ids = set()
            for square in squares:
                if (
                    x_min >= square.x_min
                    and x_max <= square.x_max
                    and y_min >= square.y_min
                    and y_max <= square.y_max
                    and z_min >= square.z_min
                    and z_max <= square.z_max
                ):
                    ids.add(square.id)
            if ids:
                mini_square = MiniSquare(
                    {
                        "x_min": x_min,
                        "x_max": x_max,
                        "y_min": y_min,
                        "y_max": y_max,
                        "z_min": z_min,
                        "z_max": z_max,
                    }
                )
                mini_square.squares = ids
                mini_squares.append(mini_square)

print("Mini squares", len(mini_squares))

for square in squares:
    for mini_square in mini_squares:
        if square.id in mini_square.squares:
            mini_square.instruction = square.instruction



print("Part 1:", count_ons(mini_squares))

