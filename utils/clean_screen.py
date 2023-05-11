from os import system, name

def clean():
    if name == 'nt':
        system('cls')
    else:
        system('clear')