# Importacao
from random import randint, choice

# Diretorio
from Pokemon_Game.Pessoa_Files.pessoa import Pessoa, lista_pokemons_aleatorios

"""
# SUB CLASSE: INIMIGO
"""

class Inimigo(Pessoa):

    def __init__(self, nome=None, pokemons=None, dinheiro=100):
        super().__init__(nome=nome, pokemons=pokemons, dinheiro=dinheiro)

        self.tipo = "inimigo"

        if pokemons is None:

            self.pokemons = list()
            pokemons_disponiveis = lista_pokemons_aleatorios()

            for i in range(randint(1, 6)):

                escolha_pokemon_random = choice(pokemons_disponiveis)
                self.pokemons.append(escolha_pokemon_random)

                # Remove o pokemon da lista de opcoes
                pokemons_disponiveis.remove(escolha_pokemon_random)

        else:
            self.pokemons = pokemons