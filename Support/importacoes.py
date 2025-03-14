# Bibliotecas
from colorama import Fore, init
init(autoreset=True)

# Pessoa
from Pokemon_Game.Pessoa_Files.pessoa import Pessoa
from Pokemon_Game.Pessoa_Files.pessoa_player import Player
from Pokemon_Game.Pessoa_Files.pessoa_inimigo import Inimigo

# Pessoa
from Pokemon_Game.Pokemon_Files.pokemon import Pokemon
from Pokemon_Game.Pokemon_Files.pokemon_agua import Pokemon_Agua
from Pokemon_Game.Pokemon_Files.pokemon_fogo import Pokemon_Fogo
from Pokemon_Game.Pokemon_Files.pokemon_eletrico import Pokemon_Eletrico

# Extended
from Pokemon_Game.Main_extended.save_game import saving
from Pokemon_Game.Main_extended.load_game import loading
from Pokemon_Game.Main_extended.delete_game import reiniciar_jogo
from Pokemon_Game.Main_extended.escolha_pokemon import escolher_pokemon_inicio