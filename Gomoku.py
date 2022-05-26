from Game import Game
from random import randint

logo = '''
 _____                       _          
|  __ \                     | |         
| |  \/ ___  _ __ ___   ___ | | ___   _ 
| | __ / _ \| '_ ` _ \ / _ \| |/ / | | |
| |_\ \ (_) | | | | | | (_) |   <| |_| |
 \____/\___/|_| |_| |_|\___/|_|\_/\__,_|
                                                                              
'''


def gomoku():
    print(logo)

    gomoku_game = Game(15, '[ ]', 'X', 'O', 5)
    game_status = True

    player_1_turn = gomoku_game.start()

    while game_status:
        should_end = gomoku_game.player_move(player_1_turn)
        if should_end:
            if gomoku_game.play_again():
                gomoku_game.restart_game()
            else:
                game_status = gomoku_game.exit()
        player_1_turn = False if player_1_turn else True

gomoku()
