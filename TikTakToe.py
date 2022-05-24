from Game import Game
from random import randint

logo = '''
  _____ _ _      _____     _      _____          
 |_   _(_) | __ |_   _|_ _| | __ |_   _|__   ___ 
   | | | | |/ /   | |/ _` | |/ /   | |/ _ \ / _ \ 
   | | | |   <    | | (_| |   <    | | (_) |  __/
   |_| |_|_|\_\   |_|\__,_|_|\_\   |_|\___/ \___|
                                                 
'''


def play_again():
    again = ''
    while again not in ['Y', 'N']:
        again = input('Do you wanna play? [y/n]\n').upper()
    return True if again == 'Y' else False


def tiktaktoe():
    print(logo)

    tiktaktoe_game = Game(3, '[ ]', 'X', 'O', 3)
    game_status = True

    print(f'Player 1 sign: {tiktaktoe_game.get_player1_sign()}')
    print(f'Player 2 sign: {tiktaktoe_game.get_player2_sign()}')

    random_start = ''
    while random_start not in ['Y', 'N']:
        random_start = input('Do you wanna choose who starts? [y/n]\n').upper()

    if random_start.upper() == 'Y':
        player_1_starts = ''
        while player_1_starts not in ['Y', 'N']:
            player_1_starts = input('First player should start? [y/n]\n').upper()
        player_1_starts = True if player_1_starts == 'Y' else False
    else:
        player_1_starts = True if randint(0, 1) == 1 else False

    player_2_starts = True if not player_1_starts else False
    print(f'Player {1 if player_1_starts else 2} will start game')

    while game_status:
        print(f'Player {1 if player_1_starts == True else 2} turn\n')
        tiktaktoe_game.show_board()
        tiktaktoe_game.replace_sign(player_1_starts,
                                    input('Enter your square: [first number last letter no gap between]\n'))
        if tiktaktoe_game.check_win(player_1_starts):
            print(f'Player {1 if player_1_starts else 2} won game\n')
            tiktaktoe_game.show_board()
            if play_again():
                tiktaktoe()
            else:
                break
        elif tiktaktoe_game.full_board():
            print(f'Draw\n')
            tiktaktoe_game.show_board()
            if play_again():
                tiktaktoe()
            else:
                break
        print(f'Player {2 if player_1_starts == True else 1} turn\n')
        tiktaktoe_game.show_board()
        tiktaktoe_game.replace_sign(player_2_starts,
                                    input('Enter your square: [first number last letter no gap between]\n'))
        if tiktaktoe_game.check_win(player_2_starts):
            print(f'Player {1 if player_2_starts else 2} won game\n')
            tiktaktoe_game.show_board()
            if play_again():
                tiktaktoe()
            else:
                break
        elif tiktaktoe_game.full_board():
            print(f'Draw\n')
            tiktaktoe_game.show_board()
            if play_again():
                tiktaktoe()
            else:
                break


tiktaktoe()
