def warn_the_sheep(queue):
    if queue.index("wolf")==len(queue)-1: return "Pls go away and stop eating my sheep"
    else:
        q=queue[::-1]
        return f"Oi! Sheep number {str(q.index('wolf'))}! You are about to be eaten by a wolf!"
    

print(warn_the_sheep(["sheep", "sheep", "wolf", "sheep", "sheep"]))