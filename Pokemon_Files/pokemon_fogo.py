# Importacao
from random import randint
from colorama import Fore, init

# Diretorio
from Pokemon_Files.pokemon import Pokemon

# Inicializacao (colorama)
init(autoreset=True)

"""
# SUB CLASSE: POKEMON_FOGO
"""

class Pokemon_Fogo(Pokemon):

    def __init__(self, especie, nome=None, level=None):
        super().__init__(especie=especie, nome=nome, level=level)

        self.tipo = "eletrico"


    def atacar(self, pokemon_rival):

        # Exemplo de ataques de Fogo do universo Pokémon
        rand = randint(1, 5)

        if rand == 1:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Chama{Fore.RESET} em {pokemon_rival}")

        elif rand == 2:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Lanca Chamas{Fore.RESET} em {pokemon_rival}")

        elif rand == 3:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Explosao de Fogo{Fore.RESET} em {pokemon_rival}")

        elif rand == 4:
            print(f"{self} {Fore.LIGHTRED_EX}lancou uma {Fore.RED}Chama da Fenix{Fore.RESET} em {pokemon_rival}")

        elif rand == 5:
            print(f"{self} {Fore.LIGHTRED_EX}lancou um {Fore.RED}Giro Fogo{Fore.RESET} em {pokemon_rival}")

        # Aqui chamamos o metodo de ataque da classe pai (Pessoa ou outra classe)
        return super().atacar(pokemon_rival)
