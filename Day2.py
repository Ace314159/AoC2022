with open("input/2.txt") as f:
    moves = list(map(lambda x: x.split(" "), f.read().splitlines()))


move_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

draw = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}


def part_one():
    score = 0
    for opponent, your in moves:
        score += move_scores[your]
        if draw[opponent] == your:
            score += 3
        elif win[opponent] == your:
            score += 6
    return score


def part_two():
    endings = {
        "X": lose,
        "Y": draw,
        "Z": win,
    }

    score = 0
    for opponent, ending in moves:
        ending_moves = endings[ending]
        score += move_scores[ending_moves[opponent]]
        if ending == "Y":
            score += 3
        elif ending == "Z":
            score += 6
    return score


print(part_one())
print(part_two())
