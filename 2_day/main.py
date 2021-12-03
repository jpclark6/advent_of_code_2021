filename = 'puzzle.txt'
instructions = []
with open(filename, 'r') as f:
    for l in f:
        instructions.append(l)


class P1_Submarine:
    def __init__(self, horizontal=0, depth=0):
        self.horizontal = horizontal
        self.depth = depth

    def read_instruction(self, inst):
        direction, amount = inst.split(" ")
        amount = int(amount)
        if direction == 'forward':
            self.horizontal += amount
        elif direction == 'down':
            self.depth += amount
        elif direction == 'up':
            self.depth -= amount

    def read_instructions(self, instructions):
        for inst in instructions:
            self.read_instruction(inst)


sub = P1_Submarine()
sub.read_instructions(instructions)
message = f"Part 1: Depth: {sub.depth}, Horizontal: {sub.horizontal}, Answer: {sub.depth * sub.horizontal}"
print(message)


class P2_Submarine:
    def __init__(self, horizontal=0, depth=0, aim=0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def read_instruction(self, inst):
        direction, amount = inst.split(" ")
        amount = int(amount)
        if direction == 'forward':
            self.horizontal += amount
            self.depth += self.aim * amount
        elif direction == 'down':
            self.aim += amount
        elif direction == 'up':
            self.aim -= amount

    def read_instructions(self, instructions):
        for inst in instructions:
            self.read_instruction(inst)


sub = P2_Submarine()
sub.read_instructions(instructions)
message = f"Part 2: Depth: {sub.depth}, Horizontal: {sub.horizontal}, Answer: {sub.depth * sub.horizontal}"
print(message)