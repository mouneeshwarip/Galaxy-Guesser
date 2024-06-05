import os
import random
from colorama import Fore, Style
from spaceship import print_spaceship, clear_terminal
from intro import display_logo, display_rules

def main_game():
   # word lists for different levels
    wordlist_level1 = ['universe', 'galaxy', 'milkyway', 'planet', 'star', 'comet']
    wordlist_level2 = ['astronaut', 'telescope', 'satellite', 'nebula', 'orbit', 'gravity']
    wordlist_level3 = ['constellation', 'interstellar', 'microgravity',  'blackhole', 'exoplanet', 'quasar']
   
   # maximum wrong guesses for different levels
    max_wrongguesses_level1 = 6
    max_wrongguesses_level2 = 5
    max_wrongguesses_level3 = 4

    # Clears the terminal
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    # Choosing the level
    def choose_level():
        while True:
            try:
                level = int(input(" Which level would you like to play? Choose 1, 2, or 3:  \n"))
                if level in [1, 2, 3]:
                    return level
                else:
                    print(" Invalid input! Please enter 1, 2, or 3.\n")
            except ValueError:
                print(" Invalid input! Please enter a number (1, 2, or 3).\n")
    level = choose_level() 

    # Setting word list and max wrong guesses based on chosen level
    if level == 1:
        wordlist = wordlist_level1
        max_wrongguesses = max_wrongguesses_level1
    elif level == 2:
        wordlist = wordlist_level2
        max_wrongguesses = max_wrongguesses_level2
    else:
        wordlist = wordlist_level3
        max_wrongguesses = max_wrongguesses_level3

    # choose a random word from the list
    randomword=random.choice(wordlist_level1)
    print(" \n" + "_ " * len(randomword))
    print(" \nGuess this word correctly and travel to space with our spaceship\n")
    print(f""" {Fore.GREEN}
         .'.  
        |o o|
       _| = |_
      |       |
      |_______|

      Battery-level : |||||| <---- This indicates the battery level of the spaceship{Style.RESET_ALL}""")   

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
        if not first_iteration:
            print(" \n Letters Guessed so far: \n")
            for letter in current_letters_guessed:
                    print(  letter, end=" ")
        else:
            first_iteration = False

        letterguessed = input(" \n Guess a letter: \n").lower()  # Convert input to lower

        # check if the input is a valid alphabetical letter and the length of the letter
        if not letterguessed.isalpha() or len(letterguessed) !=1:
            print(" Invalid input! Please enter an alphabetical letter.\n")
            continue
        if letterguessed in current_letters_guessed:
            print(" You already guessed that letter!\n")
            continue
        current_letters_guessed.append(letterguessed) 
        # when the user is right
        remaining_guesses=max_wrongguesses-amount_of_timeswrong
        if letterguessed in randomword:
            print_spaceship(level,remaining_guesses)
            current_letters_right =printword(current_letters_guessed)
        # when the user is wrong
        else:
            amount_of_timeswrong+=1
            remaining_guesses=max_wrongguesses-amount_of_timeswrong
            print(f" Wrong guess!! You are allowed to make {remaining_guesses} more wrong guesses\n")   
            print_spaceship(level,remaining_guesses)
            printword(current_letters_guessed)    
    
    if current_letters_right == len(randomword):
        print(" \nCongratulations! You guessed the word:\n", randomword)
    else:
        print(" \nGame is over! The word was:\n", randomword)

#if the user continue to play        
def play_again():
    while True:
        play_again = input(" Do you want to play again? (Y/N):\n ").strip().lower()
        if play_again == 'y':
            return True
        elif play_again == 'n':
            return False
        else:
            print(" Invalid input! Please enter 'Y' or 'N'.\n")
            
# Display the logo and rules
display_logo()
display_rules()

#perpetual loop for the main game
while True:
    main_game()
    if not play_again():
        print(" Thank you for playing!\n")
        break   
