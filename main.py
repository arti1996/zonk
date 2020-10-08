from Game.Dice import Dice
from Game.ScoreTable import ScoreTable
from Statistics.Combinations import Combinations

dado1 = Dice(4)
dado2 = Dice(3)


obj = ScoreTable()
dices = [ Dice(5), Dice(2), Dice(3), Dice(4), Dice(2), Dice(6) ]
score = obj.calculate(dices)

print(score)
#print(Combinations.calc(4))