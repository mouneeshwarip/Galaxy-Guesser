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

def printword(guessedletters):
    counter=0 ##index position
    correct_letters=0
    for char in randomword:
        if(char in guessedletters):
            print(randomword[counter], end=" ")
            correct_letters +=1
        else:
            print("_", end=" ") 
        counter+=1
    return correct_letters    