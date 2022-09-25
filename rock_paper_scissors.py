import random
from colorama import Fore
from time import sleep

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

sleep(1)

if player_move == 'r':
    player_move = 'Rock'
elif player_move == 'p':
    player_move = 'Paper'
elif player_move == 's':
    player_move = 'Scissors'
else:
    raise SystemExit('Invalid Input. Try again...')

computer_move = random.randint(1, 3)

if computer_move == 1:
    computer_move = 'Rock'
if computer_move == 2:
    computer_move = 'Paper'
else:
    computer_move = 'Scissors'

print(Fore.LIGHTCYAN_EX + f'The computer chose {computer_move}' + Fore.RESET)

sleep(1)

if (player_move == 'Rock' and computer_move == 'Scissors') or \
        (player_move == 'Paper' and computer_move == 'Rock') or \
        (player_move == 'Scissors' and computer_move == 'Paper'):
    print(Fore.GREEN + "You win!")
elif player_move == computer_move:
    print(Fore.YELLOW + 'Draw!')
else:
    print(Fore.RED + 'You lose!')
