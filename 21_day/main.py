from collections import deque

with open("puzzle.txt") as f:
    player_1_loc = int(f.readline().strip().split(" ")[-1])
    player_2_loc = int(f.readline().strip().split(" ")[-1])

rolls = 0


def roll_dice_gen():
    global rolls
    i = 1
    while True:
        rolls += 1
        yield i
        if i == 100:
            i = 1
        else:
            i += 1


roll_dice = roll_dice_gen()

players = deque(
    [
        {"player": 1, "score": 0, "location": player_1_loc},
        {"player": 2, "score": 0, "location": player_2_loc},
    ]
)

while players[0]["score"] < 1000 and players[1]["score"] < 1000:
    forward = 0
    for _ in range(3):
        forward += next(roll_dice)
    players[0]["location"] = (players[0]["location"] + forward) % 10
    if players[0]["location"] == 0:
        players[0]["location"] = 10
    players[0]["score"] += players[0]["location"]
    players.rotate(1)

part_1 = min(players[0]["score"], players[1]["score"]) * rolls
print("Part 1:", part_1)

import part_2
