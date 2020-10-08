import collections

class ScoreTable:
    _scoreTable = [
        # 1 Dado
        {
            "score": 100,
            "dices": [ 1 ]
        },
        {
            "score": 50,
            "dices": [ 5 ]
        },

        # 2 Dados
        {
            "score": 200,
            "dices": [ 1, 1 ]
        },
        {
            "score": 100,
            "dices": [ 5, 5 ]
        },

        # 3 Dados
        {
            "score": 1000,
            "dices": [ 1, 1, 1 ]
        },
        {
            "score": 200,
            "dices": [ 2, 2, 2 ]
        },
        {
            "score": 300,
            "dices": [ 3, 3, 3 ]
        },
        {
            "score": 400,
            "dices": [ 4, 4, 4 ]
        },
        {
            "score": 500,
            "dices": [ 5, 5, 5 ]
        },
        {
            "score": 600,
            "dices": [ 6, 6, 6 ]
        },

        # 4 Dados
        {
            "score": 2000,
            "dices": [ 1, 1, 1, 1 ]
        },
        {
            "score": 400,
            "dices": [ 2, 2, 2, 2 ]
        },
        {
            "score": 600,
            "dices": [ 3, 3, 3, 3 ]
        },
        {
            "score": 800,
            "dices": [ 4, 4, 4, 4 ]
        },
        {
            "score": 1000,
            "dices": [ 5, 5, 5, 5 ]
        },
        {
            "score": 1200,
            "dices": [ 6, 6, 6, 6 ]
        },

        # 5 Dados
        {
            "score": 4000,
            "dices": [ 1, 1, 1, 1, 1 ]
        },
        {
            "score": 800,
            "dices": [ 2, 2, 2, 2, 2 ]
        },
        {
            "score": 1200,
            "dices": [ 3, 3, 3, 3, 3 ]
        },
        {
            "score": 1600,
            "dices": [ 4, 4, 4, 4, 4 ]
        },
        {
            "score": 2000,
            "dices": [ 5, 5, 5, 5, 5 ]
        },
        {
            "score": 2400,
            "dices": [ 6, 6, 6, 6, 6 ]
        },

        # 6 Dados
        {
            "score": 8000,
            "dices": [ 1, 1, 1, 1, 1, 1 ]
        },
        {
            "score": 1600,
            "dices": [ 2, 2, 2, 2, 2, 2 ]
        },
        {
            "score": 2400,
            "dices": [ 3, 3, 3, 3, 3, 3 ]
        },
        {
            "score": 3200,
            "dices": [ 4, 4, 4, 4, 4, 4 ]
        },
        {
            "score": 4000,
            "dices": [ 5, 5, 5, 5, 5, 5 ]
        },
        {
            "score": 4800,
            "dices": [ 6, 6, 6, 6, 6, 6 ]
        }
    ]

    _scoreTableSpecial = [
        # Combinações especiais
        {
            "score": 500,
            "dices": [ 1, 2, 3, 4, 5 ]
        },
        {
            "score": 750,
            "dices": [ 2, 3, 4, 5, 6 ]
        },
        {
            "score": 1500,
            "dices": [ 1, 2, 3, 4, 5, 6 ]
        },
    ]

    def __init__(self):
        pass

    def mostCommon(self, diceList):
        # primeiro parâmetro: número da face
        # segundo parâmetro: número de occorências
        counter = collections.Counter(getattr(d, 'currentSide') for d in diceList)
        common_list = counter.most_common()
        common_list.sort(key=lambda x: x[1], reverse=True)
        return common_list

    def removeUsedDices(self, diceList, foundScore):
        foundedList = []
        newList = diceList.copy()

        for score in foundScore:
            for dice in score["dices"]:
                foundedList.append(dice)

        for diceObj in diceList:
            if diceObj.currentSide in foundedList:
                foundedList.remove(diceObj.currentSide)
                newList.remove(diceObj)

        return newList

    def calculate(self, diceList):
        diceList.sort()
        foundScore = []

        # Condição especial
        for scoreSpecial in self._scoreTableSpecial:
            contains = all(x in (getattr(d, 'currentSide') for d in diceList) for x in scoreSpecial["dices"])
            if contains:
                foundScore.append(scoreSpecial)

        if len(foundScore) > 0: 
            foundScore = [max(foundScore, key=lambda p: p['score'])]

        diceList = self.removeUsedDices(diceList, foundScore)
        
        # Condição geral
        # (...)

        return (foundScore, diceList)