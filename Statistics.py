from itertools import product
class Statistics:

    @staticmethod
    def combinations(dices = 6):
        sorted_combinations = []
        for combination in list(product(range(1, 7), repeat=dices)):
            combination = list(combination)
            combination.sort()
            sorted_combinations.append(combination)
        return sorted_combinations