import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_spaceship(level,wrong):
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    if wrong != 0:
         spaceship = f"""
     .'.  
    |o o|
   _| = |_
  |       |
  |_______|

  Battery-level : {"|"*wrong}    
    """
    else:
         spaceship = f"""
     .'.  
    |o o|
   _| = |_
  |       |
  |_______|

  Battery-level : 0    
    """
    if level == 1:
        if wrong >= 5:
            print(GREEN + spaceship + RESET)
        elif wrong >= 3:
            print(YELLOW + spaceship + RESET)
        else:
            print(RED + spaceship + RESET)

    


    '''spaceship = {
        6: GREEN + spaceship_full + RESET,
        5: GREEN + spaceship_full + RESET,
        4: YELLOW + spaceship_full + RESET,
        3: YELLOW + spaceship_full + RESET,
        2: RED + spaceship_full + RESET,
        1: RED + spaceship_full + RESET,
        0: RED + spaceship_full + RESET
    }  
'''

    