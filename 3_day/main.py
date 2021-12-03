filename = 'puzzle.txt'
binary_text = []
with open(filename, 'r') as f:
    for l in f:
        binary_text.append(l.strip())

final_binary = ''
for i in range(len(binary_text[0])):
    ones = 0
    for y in range(len(binary_text)):
        ones += int(binary_text[y][i])
    if ones > 1/2 * len(binary_text):
        final_binary += '1'
    else:
        final_binary += '0'

gamma = int(final_binary, 2)

final_epsilon = ''
for x in final_binary:
    if x == '1':
        final_epsilon += '0'
    else:
        final_epsilon += '1'

epsilon = int(final_epsilon, 2)

print('Part 1:', gamma * epsilon)

# part 2
from copy import copy
ans = []
for b in ['1', '0']:
    binary_copy = copy(binary_text)
    found = False
    while not found:
        for i in range(len(binary_copy[0])):
            binary_ones_rows = []
            zeros_or_ones = 0
            for y in range(len(binary_copy)):
                zeros_or_ones += int(binary_copy[y][i])
                if binary_copy[y][i] == b:
                    binary_ones_rows.append(y)
            new_binary = []
            if zeros_or_ones >= 1/2 * len(binary_copy):
                for loc in binary_ones_rows:
                    new_binary.append(binary_copy[loc])
            else:
                for y in range(len(binary_copy)):
                    if y not in binary_ones_rows:
                        new_binary.append(binary_copy[y])
            binary_copy = new_binary
            if len(binary_copy) == 1:
                found = True
                break

    ans.append(int(binary_copy[0], 2))

print("Part 2:", ans[0] * ans[1])

