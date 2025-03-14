"""
# Deletar Arquivo
"""

# Importacao
from os import path, remove
from colorama import Fore, init

# Inicializacao (Coloroma)
init(autoreset=True)

def reiniciar_jogo():

    memory_card = "Main_extended/memory_card.csv"

    if path.exists(memory_card):

        esc = input(f"{Fore.LIGHTRED_EX}Dados serao apagados permanentemente [s] [n]: {Fore.RESET}").lower()

        if esc == "s":
            remove(memory_card)
            print(f"{Fore.LIGHTMAGENTA_EX}Jogo foi reiniciado com sucesso, favor executar novamente !{Fore.RESET}")

        elif esc == "n":
            print(f"{Fore.LIGHTBLUE_EX}Jogo nao reiniciado !{Fore.RESET} !")

    else:
        print(f"Jogo nao reiniciado ! Tente novamente !!!")