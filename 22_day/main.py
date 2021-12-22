with open('puzzle.txt') as f:
    lines = f.read().split('\n')

lines = [line.split('=') for line in lines]
squares = []
for line in lines:
    line = line[1:]
    square = []
    for l in line:
        square.append(l.split(',')[0])
    squares.append(square)

import pdb; pdb.set_trace()