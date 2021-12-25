from concurrent.futures import ProcessPoolExecutor
import time
from uuid import uuid4
from pprint import pprint as pp
from collections import deque


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


def get_squares():
    with open("puzzle.txt") as f:
        lines = f.read().split("\n")
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
        squares.append(square_obj)
    return squares



def something(i, x, squares, all_x, all_y, all_z):
    count = 0
    for j, y in enumerate(all_y):
        if j == len(all_y) - 1:
            continue
        for k, z in enumerate(all_z):
            if k == len(all_z) - 1:
                continue
            inst = None
            for square in squares:
                if (
                    x >= square.x_min
                    and all_x[i + 1] <= square.x_max
                    and y >= square.y_min
                    and all_y[j + 1] <= square.y_max
                    and z >= square.z_min
                    and all_z[k + 1] <= square.z_max
                ):
                    inst = square.instruction
            if inst == 'on':
                count += ((all_x[i + 1] - x) *
                          (all_y[j + 1] - y) * (all_z[k + 1] - z))
    return count

def run():
    squares = get_squares()

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

    count = 0
    start = time.time()
    percents = [0, .0001]

    tasks = []
    with ProcessPoolExecutor(max_workers=8) as exe:
        for i, x in enumerate(all_x):
            if i == len(all_x) - 1:
                continue
            task = exe.submit(something, i, x, squares, all_x, all_y, all_z)
            tasks.append(task)
            # print("Appended", i)
        count = 0
        task_count = 0
        for task in tasks:
            print("Finished", task_count, "out of", len(tasks), task_count / len(tasks) * 100, '%')
            count += task.result()
            task_count += 1

    print("Part 2:", count)
    print("Took", time.time() - start, 'seconds')

if __name__ == '__main__':
    run()




# print("Mini squares", len(mini_squares))

# for square in squares:
#     for mini_square in mini_squares:
#         if square.id in mini_square.squares:
#             mini_square.instruction = square.instruction



