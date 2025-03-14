# Importacao
from random import randint
from colorama import Fore, init

# Diretorio
from Pokemon_Game.Pokemon_Files.pokemon import Pokemon

# Inicializacao (colorama)
init(autoreset=True)

"""
# SUB CLASSE: POKEMON_AGUA
"""

class Pokemon_Agua(Pokemon):

    def __init__(self, especie, nome=None, level=None):

        super().__init__(especie=especie, nome=nome, level=level)

        self.tipo = "agua"


    def atacar(self, pokemon_rival):

        rand = randint(1, 5)

        if rand == 1:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou um {Fore.CYAN}Jato de Agua{Fore.RESET} em {pokemon_rival}")

        elif rand == 2:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou uma {Fore.CYAN}Bomba de Agua{Fore.RESET} em {pokemon_rival}")

        elif rand == 3:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou um {Fore.CYAN}Surf{Fore.RESET} em {pokemon_rival}")

        elif rand == 4:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou uma {Fore.CYAN}Hidro Bomba{Fore.RESET} em {pokemon_rival}")

        elif rand == 5:
            print(f"{self} {Fore.LIGHTBLUE_EX}lancou um {Fore.CYAN}Golpe de Agua{Fore.RESET} em {pokemon_rival}")

        # Chamada de metodo de ataque da classe pai (Pessoa ou outra classe)
        return super().atacar(pokemon_rival=pokemon_rival)
