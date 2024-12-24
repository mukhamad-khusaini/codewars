def uefa_euro_2016(teams, scores):
    return f"At match {teams[0]} - {teams[1]}, {teams[scores.index(max(scores))]} won!" if scores[0]!=scores[1] else f"At match {teams[0]} - {teams[1]}, teams played draw."

