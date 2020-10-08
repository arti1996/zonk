import random

class Dice:
    currentSide = None

    def __init__(self, currentSide = None):

        if currentSide == None:
            currentSide = random.randint(1,6)

        self.currentSide = currentSide

    def __lt__(self, instance):
        return self.currentSide < instance.currentSide

    def __str__(self):
        return "Dado(Face: %d)" % (self.currentSide)
