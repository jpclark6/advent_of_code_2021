from itertools import product
from functools import cache


with open('puzzle.txt') as f:
    p1_loc = int(f.readline().strip().split(' ')[-1])
    p2_loc = int(f.readline().strip().split(' ')[-1])


rolls = [sum(x) for x in product([1, 2, 3], repeat=3)]

score_to_beat = 21

p1_score = 0
p2_score = 0

p1_turn = True


def pseudo_mod(loc):
    if loc == 10:
        return loc
    else:
        return loc % 10

@cache
def play_games(p1_loc, p1_score, p2_loc, p2_score, p1_turn):
    if p1_score >= score_to_beat:
        return 1, 0
    if p2_score >= score_to_beat:
        return 0, 1

    loc = p1_loc if p1_turn else p2_loc
    new_locs = [pseudo_mod(loc + roll ) for roll in rolls]

    if p1_turn:
        games = [play_games(p1_new_loc, p1_score + p1_new_loc, p2_loc, p2_score, False) for p1_new_loc in new_locs]
    else:
        games = [play_games(p1_loc, p1_score, p2_new_loc, p2_score + p2_new_loc, True) for p2_new_loc in new_locs]

    return sum([p1 for p1, _ in games]), sum(p2 for _, p2 in games)


wins = play_games(p1_loc, p1_score, p2_loc, p2_score, p1_turn)
print("Part 2:", max(wins))
