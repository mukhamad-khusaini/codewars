def duck_duck_goose(players, goose):
    return players[goose-1 if goose<=len(players) else (goose%len(players))-1].name