# Biblioteca
from time import sleep
from colorama import Fore, init
from random import choice, sample, randint

# Diretorio
from Pokemon_Game.Pokemon_Files.pokemon_agua import Pokemon_Agua
from Pokemon_Game.Pokemon_Files.pokemon_fogo import Pokemon_Fogo
from Pokemon_Game.Pokemon_Files.pokemon_eletrico import Pokemon_Eletrico

"""
# CLASSE: PESSOA
"""

# Inicializando o colorama
init(autoreset=True)

class Pessoa:

    def __init__(self, nome=None, pokemons=None, dinheiro=100):

        self.nome = nome_aleatorios() if nome is None else nome
        self.pokemons = pokemons if pokemons is not None else []
        self.dinheiro = dinheiro


    # Personalizacao do objeto em string
    def __str__(self):
        return f"{Fore.LIGHTGREEN_EX}{self.nome}{Fore.RESET}"

    """"""""""""""""""""""""""
    """ Metodos Principais """
    """"""""""""""""""""""""""

    def mostrar_pokemon(self):

        if len(self.pokemons) > 0:
            print(f"| Pokemon de {self} |")

            # Enumerando pokemons: Indice e Valor
            for i, j in enumerate(self.pokemons):
                print(f"{i}: {j}")

        else:
            print(f"{self} {Fore.RED}nao possui pokemons{Fore.RESET}")


    def escolher_pokemon(self):

        if len(self.pokemons) > 0:
            pokemon_rival_escolhido = choice(self.pokemons)

            print(f"{self} escolheu {pokemon_rival_escolhido}")
            return pokemon_rival_escolhido

        else:
            print(f"{self} esta sem pokemons para a batalha !")
            return None


    def batalhar(self, rival):

        print(f"{self} iniciou uma batalha com {rival}")

        # Mostrar Pokemons do adversario
        rival.mostrar_pokemon()
        pokemon_rival = rival.escolher_pokemon()

        # Escolha Player
        self.mostrar_pokemon()
        pokemon = self.escolher_pokemon()

        # Verificacao
        if pokemon and pokemon_rival:

            while True:
                sleep(1)

                if pokemon.atacar(pokemon_rival):
                    print(f"{self} ganhou a batalha")
                    self.ganhar_dinheiro(pokemon.level * 10)
                    break

                if pokemon_rival.atacar(pokemon):
                    print(f"{self} perdeu a batalha")
                    self.perder_dinheiro(pokemon.level * 10)
                    break
        else:
            print("Batalha Cancelada !")


    def explorar(self):

        # Chance de encontrar um Pokémon selvagem
        if randint(1, 10) <= 3:

            pokemon = choice(lista_pokemons_aleatorios())
            print(f"Um Pokemon {pokemon} selvagem apareceu!")

            resp = input("Deseja capturá-lo? [s] / [n]: ").lower()

            if resp == "s":

                # Chance de captura baseada no nível do Pokémon
                chance_captura = max(30, 100 - (pokemon.level * 10) + self.calcular_bonus_de_captura() * 5)

                if randint(1, 100) <= chance_captura:
                    print(f"{self} capturou {pokemon}!")
                    self.pokemons.append(pokemon)
                    self.mostrar_pokemon()

                else:
                    print(f"{Fore.GREEN}Pokemon escapou!{Fore.RESET}")

            else:
                print("Voce decidiu nao capturar o Pokemon.")

        else:
            print(f"{Fore.RED}Exploracao sem sucesso!{Fore.RESET}")


    """"""""""""""""""""""""""""""""""""
    """ Metodos de suporte a Classe """
    """"""""""""""""""""""""""""""""""""

    def mostrar_dinheiro(self):

        print(f"{self} possui R$ {self.dinheiro}")


    def ganhar_dinheiro(self, montante):

        self.dinheiro += montante
        print(f"{self} ganhou R$ {montante}")
        self.mostrar_dinheiro()


    def perder_dinheiro(self, montante):

        self.dinheiro -= montante
        print(f"{self} perdeu R$ {montante}")

        if self.dinheiro < 0:
            self.dinheiro = 0
            self.mostrar_dinheiro()


    def calcular_bonus_de_captura(self):

        if self.pokemons:

            # Retorna o maior nivel diretamente
            return max(i.level for i in self.pokemons)

        return 0

"""""""""""""""""""""""""""""
"""""" Metodos Suporte """"""
"""""""""""""""""""""""""""""

def nome_aleatorios():

    nomes = [
        "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas",
        "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua",
        "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffrey", "Ryan",
        "Gary", "Nicholas", "Eric", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel",
        "Frank", "Gregory", "Alexander", "Raymond", "Patrick", "Jack", "Dennis", "Jerry", "Tyler", "Aaron",
        "Jose", "Adam", "Zachary", "Nathan", "Peter", "Harold", "Douglas", "Kyle", "Walter", "Ethan",
        "Carl", "Arthur", "Gerald", "Roger", "Joe", "Juan", "Jackie", "Christian", "Roy", "Bobby", "Albert",
        "Russell", "Mason", "Dylan", "Lucas", "Henry", "Wayne", "Eugene", "Ralph", "Juan", "Billy", "Bruce",
        "Willie", "Jordan", "Carl", "Dean", "Alan", "Randy", "Craig", "Danny", "Victor", "Lee", "Melvin",
        "Leonard", "Curtis", "Ernest", "Chad", "Francis", "Herman", "Claude", "Edwin", "Charlie", "Brett",
        "Bill", "Leroy", "Todd", "Danny", "Arthur", "Dennis", "Marvin", "Alfred", "Wesley", "Clifford",
        "Calvin", "Martin", "Ruben", "Tony", "Harry", "Glen", "Howard", "Manuel", "Theodore", "Norman"
    ]

    return choice(nomes)


def lista_pokemons_aleatorios():

    pokemons_fogo = [
        "Charmander", "Charmeleon", "Charizard", "Vulpix", "Ninetales", "Growlithe", "Arcanine",
        "Magmar", "Flareon", "Cyndaquil", "Quilava", "Typhlosion", "Entei", "Torchic", "Combusken",
        "Blaziken", "Slugma", "Magcargo", "Numel", "Camerupt", "Torkoal", "Chimchar", "Monferno",
        "Infernape", "Pignite", "Emboar", "Fennekin", "Braixen", "Delphox", "Litten", "Torracat",
        "Incineroar", "Litleo", "Pyroar", "Carkol", "Coalossal", "Firedrake", "Houndoom", "Houndour",
        "Cyndaquil", "Blaziken", "Camerupt", "Flareon", "Heatmor", "Magmar", "Torchic", "Braixen",
        "Delphox", "Numel", "Magcargo", "Slugma", "Combusken", "Flareon", "Entei", "Ho-Oh", "Chandelure",
        "Rotom-Heat", "Reshiram", "Zekrom", "Victini", "Litten", "Torracat", "Incineroar", "Charizard",
        "Blaziken", "Volcanion", "Groudon", "Torkoal", "Flareon", "Arcanine", "Magmar", "Ninetales",
        "Fennekin", "Braixen", "Delphox", "Torchic", "Chimchar", "Monferno", "Infernape", "Torkoal",
        "Slugma", "Magcargo", "Numel", "Fennekin", "Charmander", "Charmeleon", "Blaziken", "Houndoom",
        "Houndour", "Heatmor", "Cyndaquil", "Quilava", "Typhlosion", "Growlithe", "Arcanine", "Flareon",
        "Blaziken", "Magmar", "Numel", "Camerupt", "Litleo", "Pyroar", "Chandelure", "Volcarona",
        "Victini", "Emboar", "Magmortar", "Pignite", "Chimchar", "Infernape"
    ]

    pokemons_agua = [
        "Squirtle", "Wartortle", "Blastoise", "Poliwag", "Poliwhirl", "Politoed", "Magikarp", "Gyarados",
        "Totodile", "Croconaw", "Feraligatr", "Suicune", "Lanturn", "Remoraid", "Octillery", "Corsola",
        "Kingdra", "Barboach", "Whiscash", "Piplup", "Prinplup", "Empoleon", "Oshawott", "Dewott",
        "Samurott", "Chinchou", "Froakie", "Frogadier", "Greninja", "Mudkip", "Marshtomp", "Swampert",
        "Shellder", "Cloyster", "Lotad", "Lombre", "Ludicolo", "Carvanha", "Sharpedo", "Wailmer",
        "Wailord", "Corphish", "Crawdaunt", "Finneon", "Lumineon", "Barboach", "Whiscash", "Seel",
        "Dewgong", "Squirtle", "Poliwag", "Piplup", "Totodile", "Kingdra", "Gyarados", "Seaking",
        "Starmie", "Staryu", "Corsola", "Corphish", "Crawdaunt", "Mudkip", "Swampert", "Marshtomp",
        "Magikarp", "Remoraid", "Octillery", "Piplup", "Prinplup", "Empoleon", "Froakie", "Frogadier",
        "Greninja", "Chinchou", "Lanturn", "Mudkip", "Swampert", "Totodile", "Croconaw", "Feraligatr",
        "Piplup", "Prinplup", "Empoleon", "Totodile", "Poliwag", "Poliwhirl", "Politoed", "Kingdra",
        "Gyarados", "Seel", "Dewgong", "Corsola", "Barboach", "Whiscash", "Carvanha", "Sharpedo",
        "Finneon", "Lumineon", "Seaking", "Lotad", "Lombre", "Ludicolo", "Swampert", "Marshtomp",
        "Wailmer", "Wailord", "Seviper", "Horsea", "Kingdra", "Swampert", "Seaking", "Quagsire",
        "Gyarados", "Magikarp", "Lapras", "Tentacool", "Tentacruel", "Squirtle", "Wartortle", "Blastoise"
    ]

    pokemons_eletrico = [
        "Pikachu", "Raichu", "Electrode", "Voltorb", "Magnemite",
        "Magneton", "Zekrom", "Jolteon", "Electivire", "Raikou",
        "Emolga", "Mareep", "Flaaffy", "Ampharos", "Chinchou",
        "Blitzle", "Zebstrika", "Tynamo", "Eelektrik", "Eelektross",
        "Luxray", "Shinx", "Rotom", "Heliolisk", "Helioptile",
        "Minun", "Plusle", "Tapu Koko", "Magnezone", "Thundurus"
    ]

    fogo_ale = sample(pokemons_fogo, 2)
    agua_ale = sample(pokemons_agua, 2)
    eletrico_ale = sample(pokemons_eletrico, 2)

    # Listagem com os pokemons escolhidos
    lista_pokemons = [
        Pokemon_Fogo(fogo_ale[0]), Pokemon_Fogo(fogo_ale[1]),
        Pokemon_Agua(agua_ale[0]), Pokemon_Agua(agua_ale[1]),
        Pokemon_Eletrico(eletrico_ale[0]), Pokemon_Eletrico(eletrico_ale[1])
    ]

    return lista_pokemons