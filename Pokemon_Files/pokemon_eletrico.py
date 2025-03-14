# Importacao
from random import randint
from colorama import Fore, init

# Diretorio
from Pokemon_Files.pokemon import Pokemon

# Inicializacao (colorama)
init(autoreset=True)

"""
# SUB CLASSE: POKEMON_ELETRICO
"""

class Pokemon_Eletrico(Pokemon):

    def __init__(self, especie, nome=None, level=None):
        super().__init__(especie=especie, nome=nome, level=level)

        self.tipo = "eletrico"


    def atacar(self, pokemon_rival):

        rand = randint(1, 5)

        if rand == 1:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTCYAN_EX}Choque do Trovao{Fore.RESET} em {pokemon_rival}")

        elif rand == 2:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTBLUE_EX}Raio{Fore.RESET} em {pokemon_rival}")

        elif rand == 3:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTMAGENTA_EX}Relampago{Fore.RESET} em {pokemon_rival}")

        elif rand == 4:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou uma {Fore.LIGHTGREEN_EX}Corte Eletrico{Fore.RESET} em {pokemon_rival}")

        elif rand == 5:
            print(f"{self} {Fore.LIGHTYELLOW_EX}lancou um {Fore.LIGHTRED_EX}Pulso Eletrico{Fore.RESET} em {pokemon_rival}")

        # Chamada de metodo de ataque da classe pai (Pessoa ou outra classe)
        return super().atacar(pokemon_rival=pokemon_rival)