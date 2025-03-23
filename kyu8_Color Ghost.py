import random
class Ghost():
    color=""
    def __init__(self):
        self.color=['white', 'yellow', 'purple', 'red'][random.randint(0,3)]
    
ghost=[Ghost().color for _ in range(10)]

print(ghost)