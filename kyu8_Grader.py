def grader(score):
    return 'F' if score < 0.6 or score > 1 else "D" if score < 0.7 else "C" if score < 0.8 else "B" if score < 0.9 else "A"