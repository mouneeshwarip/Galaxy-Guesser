import os


def print_spaceship(level, wrong):
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
    elif level == 2:
        if wrong >= 4:
            print(GREEN + spaceship + RESET)
        elif wrong >= 2:
            print(YELLOW + spaceship + RESET)
        else:
            print(RED + spaceship + RESET)
    else:
        if wrong >= 3:
            print(GREEN + spaceship + RESET)
        elif wrong >= 1:
            print(YELLOW + spaceship + RESET)
        else:
            print(RED + spaceship + RESET)
