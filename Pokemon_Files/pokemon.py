# Importacao
from colorama import Fore, init
from random import randint, random

# Inicializando o colorama
init(autoreset=True)

"""
# CLASSE PAI: POKEMON
"""

class Pokemon:

    def __init__(self, especie, nome=None, level=None):

        self.especie = especie
        self.nome = especie if nome is None else nome
        self.level = randint(1, 100) if level is None else level
        self.ataque = self.level * 5
        self.vida = self.level * 10


    def __str__(self):
        return f"{Fore.LIGHTCYAN_EX}{self.especie}{Fore.RESET} {Fore.LIGHTYELLOW_EX}({self.level}){Fore.RESET}"


    def atacar(self, pokemon_rival):

        ataque_efetivo = int(self.ataque * random() * 1.3)

        # Pokemon: Agua Vs Fogo
        if self.tipo == "agua" and pokemon_rival.tipo == "fogo":
            ataque_efetivo = int(ataque_efetivo * 1.2)  # Aumenta o dano

        elif self.tipo == "fogo" and pokemon_rival.tipo == "agua":
            ataque_efetivo = int(ataque_efetivo * 0.5)  # Reduz o dado

        # Pokemon: Eletrico Vs Agua
        elif self.tipo == "eletrico" and pokemon_rival.tipo == "agua":
            ataque_efetivo = int(ataque_efetivo * 1.2)  # Aumenta o dano

        elif self.tipo == "agua" and pokemon_rival.tipo == "eletrico":
            ataque_efetivo = int(ataque_efetivo * 0.5)  # Reduz o dano

        # Aplicando o dano
        pokemon_rival.vida -= ataque_efetivo

        print(f"{pokemon_rival} perdeu {ataque_efetivo} pontos de vida")

        if pokemon_rival.vida <= 0:

            print(f"{pokemon_rival} foi {Fore.LIGHTRED_EX}derrotado !{Fore.RESET}")
            return True
        else:
            return False
