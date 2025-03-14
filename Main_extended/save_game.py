"""
# Salvar Jogo
"""

# Importacao
from pickle import dump

def saving(player):

    memory_card = "Main_extended/memory_card.csv"

    try:
        with open(memory_card, "wb") as file:
            dump(player, file)

    except FileNotFoundError:
        print("Loading...Falhou !!!")