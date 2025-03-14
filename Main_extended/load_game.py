"""
# Carregar Jogo
"""

# Importacao
from colorama import Fore, init
from pickle import load

init(autoreset=True)

def loading():

    memory_card = "Main_extended/memory_card.csv"

    try:
        with open(memory_card, "rb") as file:

            print(f"{Fore.LIGHTBLUE_EX}Loading...{Fore.RESET}")
            return load(file)

    except (FileNotFoundError, UnpicklingError):

        print(f"{Fore.LIGHTWHITE_EX}Loading... Failed !!!{Fore.RESET}")
        return None
