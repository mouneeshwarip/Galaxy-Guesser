from colorama import Fore, Style

def display_logo():
    logo = f"""
{Fore.CYAN}
  
 
  /$$$$$$            /$$                                      /$$$$$$                                                                  
 /$$__  $$          | $$                                     /$$__  $$                                                                 
| $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$   /$$ /$$   /$$      | $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$  /$$$$$$   /$$$$$$       
| $$ /$$$$ |____  $$| $$ |____  $$|  $$ /$$/| $$  | $$      | $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/ /$$__  $$ /$$__  $$      
| $$|_  $$  /$$$$$$$| $$  /$$$$$$$ \  $$$$/ | $$  | $$      | $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ | $$$$$$$$| $$  \__/      
| $$  \ $$ /$$__  $$| $$ /$$__  $$  >$$  $$ | $$  | $$      | $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$| $$_____/| $$            
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$ /$$/\  $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$$| $$            
 \______/  \_______/|__/ \_______/|__/  \__/ \____  $$       \______/  \______/  \_______/|_______/|_______/  \_______/|__/            
                                             /$$  | $$                                                                                 
                                            |  $$$$$$/                                                                                 
                                             \______/                                                                                  

{Fore.YELLOW}{Style.BRIGHT}*** Welcome to the Astro Hangman Game! ***
{Style.RESET_ALL}                                                                                                 
"""
    print(logo)

# function to display rules

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
       
