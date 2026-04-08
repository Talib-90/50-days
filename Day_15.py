# Inheritance
class Animal:
    def __init__(self):
        self.eyees = 2

    def breath(self):
        print("Inhale | Exhale")


# Child Class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("breath under water.")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.eyees)
