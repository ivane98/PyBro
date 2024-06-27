import random

while True:
    choices = ['rock', 'paper', 'scissors']
    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input('rock, paper, or scissors?: ').lower()

        if player == computer:
            print("computer: ", computer)
            print("player: ", player)
            print('it is a tie!')
        elif player == 'rock':
            if computer == 'scissors':
                print("computer: ", computer)
                print("player: ", player)
                print('you win!')
            if computer == 'paper':
                print("computer: ", computer)
                print("player: ", player)
                print('you lose!')
        elif player == 'paper':
            if computer == 'scissors':
                print("computer: ", computer)
                print("player: ", player)
                print('you lose!')
            if computer == 'rock':
                print("computer: ", computer)
                print("player: ", player)
                print('you win!')
        elif player == 'scissors':
            if computer == 'paper':
                print("computer: ", computer)
                print("player: ", player)
                print('you win!')
            if computer == 'rock':
                print("computer: ", computer)
                print("player: ", player)
                print('you lose!')

    play_again = input('do you want to play again? ').lower()

    if play_again != 'yes':
        break

print('bye')