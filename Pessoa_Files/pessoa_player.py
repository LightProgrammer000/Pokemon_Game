# Diretorio
import Pokemon_Files.pokemon_eletrico
from Pessoa_Files.pessoa import Pessoa

"""
# SUB CLASSE: PLAYER
"""

class Player(Pessoa):

    def __init__(self, nome=None, pokemons=None, dinheiro=100):
        super().__init__(nome=nome, pokemons=pokemons, dinheiro=dinheiro)

        self.tipo = "player"


    def escolher_pokemon(self):

        if len(self.pokemons) > 0:

            # Protecao contra escolha invalida
            while True:

                try:
                    escolha_indice_pokemon = int(input("Escolha o indice referente ao seu Pokemon: "))
                    pokemon_escolhido = self.pokemons[escolha_indice_pokemon]

                    print(f"{pokemon_escolhido} eu escolho voce !!!")
                    return pokemon_escolhido

                except (IndexError, ValueError):
                    print("Seleção invalida! Tente novamente.")

        else:
            print(f"{self} sem pokemon para a batalha !")


    def capturar_pokemon(self, pokemon):

        print(f"{self} capturou {pokemon}")
        self.pokemons.append(pokemon)


    def hack(self):

        zapdos = Pokemon_Game.Pokemon_Files.pokemon_eletrico.Pokemon_Eletrico(especie="Zapdos",level=100)
        self.pokemons.append(zapdos)