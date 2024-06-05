import os
import random

wordlist_level1 = ['universe', 'galaxy', 'milkyway', 'planet', 'star', 'comet']

max_wrongguesses_level1 = 6

# Clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')