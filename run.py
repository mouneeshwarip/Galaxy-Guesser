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

amount_of_timeswrong=0
current_letters_guessed=[]
current_letters_right=0
# Flag to control the execution of "Letters Guessed so far" print statement
first_iteration = True   

while(amount_of_timeswrong != max_wrongguesses and current_letters_right != len(randomword)):
    '''
    print("\n Letters Guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    letterguessed=input("\n Guess a letter: \n").lower() ##convert input to lower
    '''
    if not first_iteration:
        print("\n Letters Guessed so far: ")
        for letter in current_letters_guessed:
            print(letter, end=" ")
    else:
        first_iteration = False

    letterguessed = input("\n Guess a letter: \n").lower()  # Convert input to lower

    ##check if the input is a valid alphabetical letter and the length of the letter
    if not letterguessed.isalpha() or len(letterguessed) !=1:
        print("Invalid input! Please enter an alphabetical letter.")
        continue
    if letterguessed in current_letters_guessed:
        print("You already guessed that letter!")
        continue
    current_letters_guessed.append(letterguessed) 
    ##when the user is right
    remaining_guesses=max_wrongguesses-amount_of_timeswrong
    if letterguessed in randomword:
        print_spaceship(level,remaining_guesses)
        current_letters_right =printword(current_letters_guessed)
   
