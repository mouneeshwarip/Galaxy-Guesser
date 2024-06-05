import os
import random

wordlist_level1 = ['universe', 'galaxy', 'milkyway', 'planet', 'star', 'comet']

max_wrongguesses_level1 = 6

# Clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# choose a random word from the list
randomword=random.choice(wordlist_level1)
print("\n" + "_ " * len(randomword))
print("\nGuess this word correctly and travel to space with our spaceship")
print(f""" {Fore.GREEN}
     .'.  
    |o o|
   _| = |_
  |       |
  |_______|

  Battery-level : |||||| <---- This indicates the battery level of the spaceship. Finish the game before exhausting the battery. {Style.RESET_ALL}""")   
