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
    