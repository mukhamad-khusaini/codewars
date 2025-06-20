class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        if self.lives==0: raise ValueError("Omae wa mo shindeiru")
        elif(n==self.number): 
            self.lives = self.lives-1
            return True
        else: return False