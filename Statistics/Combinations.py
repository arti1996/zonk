from itertools import product

from Game.Dice import Dice

class Combinations:

    @staticmethod
    def calc(dices = 6):
        sorted_combinations = []
        for combination in list(product(range(1, 7), repeat=dices)):
            combination = list(combination)
            combination.sort()
            for dice_index in range(len(combination)):
                combination[dice_index] = Dice(combination[dice_index])
            sorted_combinations.append(combination)
        return sorted_combinations