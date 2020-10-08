# System imports
import sys
import time
import pandas as pd

# App imports
from Game.Dice import Dice
from Game.ScoreTable import ScoreTable
from Statistics.Combinations import Combinations

def help():
    print("""
    Zonk - Um jogo de dados medieval baseado no jogo Kingdom Come Deliverance.

    Por favor execute o programa em combinação com argumentos:

    Argumentos:
        main.py statistics [número de dados] -> Cria um report com a nomenclatura de statistics_[número de dadis]_[data e hora atual].xlsx incluindo os pontos obtídos para cada combinação.
        main.py game [acordo pontuação] -> Inicia um novo jogo de zonk entre dois jogadores e ganha aquele que primeiro atingir a pontuação acordada.
    """)

if len(sys.argv) < 3:
    help()
    exit(0)

if sys.argv[1] == "statistics":
    print("Criando um report de combinações possíveis entre %s dados..." % sys.argv[2])
    combinations = Combinations.calc(int(sys.argv[2]))
    rows = []
    for combination in combinations:
        scores = ScoreTable().calculate(combination)
        row = {}
        for dice_index in range(len(combination)):
            row["d" + str(dice_index + 1)] = combination[dice_index].currentSide
        row["P(X)"] = float(1) / float(len(combinations))
        row["points"] = sum(s["score"] if "score" in s else 0 for s in scores[0])
        row["greedy"] = row["points"] * row["P(X)"]
        rows.append(row)
    df = pd.DataFrame.from_dict(rows)
    filename = "statistics_%s_%s.xlsx" % (int(sys.argv[2]), time.strftime("%Y%m%d-%H%M%S"))
    df.to_excel(filename)

elif sys.argv[1] == "game":
    print("Iniciando uma partida de zonk com pontuação total de %s..." % sys.argv[2])
else:
    print("Erro: Argumento '%s' não existe." % sys.argv[1])
    exit(0)