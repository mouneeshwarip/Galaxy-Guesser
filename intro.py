from colorama import Fore, Style

def display_logo():
    logo = f"""
{Fore.ORANGE}
  
 
 
 ____   _   _      _   _   _ _  _   ____  _  _ ___  ___  ___ ___ ____   
).-._( )_\ ) |    )_\ ) ( ) | () ( ).-._() () | __((  _((  _| __(  _ \  
|( ,-./( )\| (__ /( )\ ) | ('.  /  |( ,-.| \/ | _) _) \ _) \| _))  ' /  
)_`__|_/ \_|____|_/ \_|_( )_(/_(   )_`__()____|___|____)____)___(_()_\  
                                                                        
                        

{Fore.YELLOW}{Style.BRIGHT}*** Welcome to the Astro Hangman Game! ***
{Style.RESET_ALL}                                                                                                 
"""
    #print(logo)
    print(logo.center(80))  # Center the logo on an 80-character wide console

# function to display rules
'''
def display_rules():
    rules = f"""
{Fore.GREEN}Rules:{Style.RESET_ALL}
1. Choose a level to play: 1, 2, or 3.
2. Guess the letters to complete the word.
3. You have a limited number of wrong guesses based on the level.
4. Each wrong guess reduces the spaceship's battery level.
5. Try to guess the word before the battery runs out!
"""
    print(rules)

    '''  

def display_rules():
    '''
    Requesting user to provide input whether
    user wants to read the game rules.
    '''
    while True:
        try:
            user_input = input("Do you want to read the rules?(Y/N)\n").lower()
            if user_input == 'y':
                print(f"""
                {Fore.GREEN}Rules:{Style.RESET_ALL}

                 1. Choose a level to play: 1, 2, or 3.
                 2. Guess the letters to complete the word.
                 3. You have a limited number of wrong guesses based on the level.
                 4. Each wrong guess reduces the spaceship's battery level.
                 5. Try to guess the word before the battery runs out!\n
                 """)
                return True
                print(rules)
            elif user_input == 'n':
                print("Okay!, Lets Start!")
                return False
            else:
                raise ValueError
        except ValueError:
            typewriter_effects("Invalid choice: Please enter 'Y' or 'N'.\n")  
