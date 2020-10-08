from Dice import Dice
from ScoreTable import ScoreTable

dado1 = Dice(4)
dado2 = Dice(3)


obj = ScoreTable()
dices = [ Dice(5), Dice(2), Dice(3), Dice(4), Dice(2), Dice(6) ]
for dice in dices:
    print(dice)

score = obj.calculate(dices)
print("")
print(score)
