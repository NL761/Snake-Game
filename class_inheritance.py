"""just for learning and reference about class inheritance property"""

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhales, exhales.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water.")

    def swim(self):
        print("Moving in water")

fish = Fish()
print(fish.num_eyes)
fish.breathe()
fish.swim()