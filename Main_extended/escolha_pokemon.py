"""
# Escolhendo Pokemon inicialmente
"""

# Importacoes
from Pokemon_Game.Support.importacoes import *

# Colorama
init(autoreset=True)


def escolher_pokemon_inicio(player):

    picachu = Pokemon_Eletrico(especie="Picachu", level=1)
    charmander = Pokemon_Fogo(especie="Charmander", level=1)
    squirtle = Pokemon_Agua(especie="Squirtle", level=1)

    print(f"# {player} escolha dentre 3 pokemons o seu pokemon inicial: ")
    print(f"[1] - {picachu}")
    print(f"[2] - {charmander}")
    print(f"[3] - {squirtle}")
    print(f"[0] - Nenhum !")

    while True:

        try:
            opc = int(input("Escolha o seu Pokemon: "))
            print("")

            if opc == 0:
                print(f"{Fore.RED}NUNCA SERA UM MESTRE POKEMON !!!{Fore.RESET}")
                exit(0)

            elif opc == 1:
                player.capturar_pokemon(picachu)

            elif opc == 2:
                player.capturar_pokemon(charmander)

            elif opc == 3:
                player.capturar_pokemon(squirtle)

            else:
                print("# Vamos, capture seu Pokemon !!!")
                continue

        except ValueError:
            print(f"{Fore.RED}Opcao Invalida !{Fore.RESET}")
            continue

        break