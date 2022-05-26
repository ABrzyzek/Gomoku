from Game import Game
from random import randint

logo = '''
  _____ _ _      _____     _      _____          
 |_   _(_) | __ |_   _|_ _| | __ |_   _|__   ___ 
   | | | | |/ /   | |/ _` | |/ /   | |/ _ \ / _ \ 
   | | | |   <    | | (_| |   <    | | (_) |  __/
   |_| |_|_|\_\   |_|\__,_|_|\_\   |_|\___/ \___|
                                                 
'''

def tik_tak_toe():
    print(logo)

    tik_tak_toe_game = Game(3, '[ ]', 'X', 'O', 3)
    game_status = True

    player_1_turn = tik_tak_toe_game.start()

    while game_status:
        should_end = tik_tak_toe_game.player_move(player_1_turn)
        if should_end:
            if tik_tak_toe_game.play_again():
                tik_tak_toe_game.restart_game()
            else:
                game_status = tik_tak_toe_game.exit()
        player_1_turn = False if player_1_turn else True

tik_tak_toe()
