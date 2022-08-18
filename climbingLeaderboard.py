def climbingLeaderboard(ranked, player):
    arr = []
    for p in player:
        arr.append(getPosition(ranked, p))
    return arr

def getPosition(ranked, s):
    position = 1
    prev_score = ranked[0]
    for index, score in enumerate(ranked[1:]):
        if score != prev_score:
            position += 1
        if s == score:
            return position
        elif s < score:
            return position + 1
        prev_score = score
    return 1 


#print(climbingLeaderboard([100,90,90,80], [70,80,105]))
print(getPosition([100,90,90,80],70))