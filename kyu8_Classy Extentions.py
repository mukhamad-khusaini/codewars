from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."