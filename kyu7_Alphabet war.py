def alphabet_war(fight):
    powA={
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }
    powB={
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }

    left=sum([powA[i] for i in fight if i in powA])
    right=sum([powB[i] for i in fight if i in powB])

    return "Right side wins!" if right>left else "Left side wins!" if left>right else "Let's fight again!"