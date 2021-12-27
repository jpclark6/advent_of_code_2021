with open('puzzle.txt') as f:
    lines = f.read().split('\n')


class Cucumber:
    def __init__(self, x, y, c_type):
        self.x = x
        self.y = y
        self.type = c_type
        self.x_potential = x
        self.y_potential = y
        self.valid = False

    def check_move(self, locations):
        if self.type == '>':
            self.x_potential = (self.x_potential + 1) % x_length
        else:
            self.y_potential = (self.y_potential + 1) % y_length

        if (self.x_potential, self.y_potential) not in locations:
            self.valid = True

    def commit_move(self):
        self.x = self.x_potential
        self.y = self.y_potential
        self.valid = False

    def reset_move(self):
        self.x_potential = self.x
        self.y_potential = self.y
        self.valid = False


cucumbers = []

for y, line in enumerate(lines):
    l = list(line)
    for x, l in enumerate(l):
        if l in ['>', 'v']:
            cucumbers.append(Cucumber(x, y, l))

x_length = len(lines[0])
y_length = len(lines)


def print_board():
    c_right = [(c.x, c.y) for c in cucumbers if c.type == '>']
    c_down = [(c.x, c.y) for c in cucumbers if c.type == 'v']
    for y in range(y_length):
        yline = ''
        for x in range(x_length):
            ch = '.'
            if (x, y) in c_right:
                ch = '>'
            elif (x, y) in c_down:
                ch = 'v'
            yline += ch
        print(yline)
    print()

total = 0
moved_right = moved_down = True
while moved_right or moved_down:
    # print("Step", total)
    # print_board()

    moved_right = False
    moved_down = False
    for c_type in ['>', 'v']:
        current_locations = {(c.x, c.y) for c in cucumbers}
        for cucumber in cucumbers:
            if cucumber.type == c_type:
                cucumber.check_move(current_locations)
        for cucumber in cucumbers:
            if cucumber.valid:
                cucumber.commit_move()
                if c_type == '>':
                    moved_right = True
                else:
                    moved_down = True
            else:
                cucumber.reset_move()

    total += 1

print("Part 1:", total)
