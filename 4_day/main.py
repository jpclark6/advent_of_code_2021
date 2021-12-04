filepath = 'puzzle.txt'
lines = []
with open(filepath, 'r') as f:
    for l in f:
        lines.append(l)

drawings = [int(x) for x in lines[0].split(',')]
boards = []
try:
    b = 0
    while True:
        lines[b + 2]
        board = [[int(x) for x in r.strip().replace('  ', ' ').split(' ')] for r in lines[b + 2:b + 7]]
        boards.append(board)
        b += 6
except:
    pass

def winner(board, called_numbers):
    for r in board:
        if all([n in called_numbers for n in r]):
            return True
    for r in range(len(board)):
        if all([n[r] in called_numbers for n in board]):
            return True

finished = False
for n in range(len(drawings)):
    if finished:
        break
    for board in boards:
        called_numbers = drawings[:n]
        if winner(board, called_numbers):
            board_numbers = []
            for r in board:
                [board_numbers.append(x) for x in r]
            uncalled_numbers = [x for x in board_numbers if x not in called_numbers]
            print("Part 1:", sum(uncalled_numbers) * called_numbers[-1])
            finished = True
            break

# Part 2
finished = False
won_boards = []
for n in range(len(drawings)):
    if finished:
        break
    for board in boards:
        called_numbers = drawings[:n]
        if winner(board, called_numbers):
            if str(board) not in won_boards:
                won_boards.append(str(board))
            if len(won_boards) == len(boards):
                board_numbers = []
                for r in board:
                    [board_numbers.append(x) for x in r]
                uncalled_numbers = [x for x in board_numbers if x not in called_numbers]
                print("Part 2:", sum(uncalled_numbers) * called_numbers[-1])
                finished = True
                break