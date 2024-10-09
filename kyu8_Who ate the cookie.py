def cookie(x):
    if type(x) == type("s"): return "Who ate the last cookie? It was Zach!"
    elif type(x) == type(2) or type(x) == type(1.1): return "Who ate the last cookie? It was Monica!"
    else: return "Who ate the last cookie? It was the dog!"