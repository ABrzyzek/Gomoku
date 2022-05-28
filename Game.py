import re
from random import randint


class Game:
    alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    min_sequence = 3
    min_board = 3
    max_board = 26
    win_status = 0
    answers = ['Y', 'N']
    max_background_sign = 4
    question_enter_square = 'Enter your square: [first number last letter no gap between]\n'

    def __init__(self, side_square: int, background_sign: str, player1_sign: str, player2_sign: str,
                 sequence_number: int):
        self.__side_square = self._is_valid_side_square(side_square)
        self.__board = self.create_board(side_square, background_sign)
        self.__background_sign = self._is_valid_background_sign(background_sign)
        self.__player1_sign = self._is_valid_player_sign(player1_sign, background_sign)
        self.__player2_sign = self._is_valid_player_sign(player2_sign, background_sign)
        self.__sequence_number = self._is_valid_side_sequence(sequence_number, side_square)

    def create_board(self, side_square: int, background_sign: str) -> list:
        board = []
        side_square = self._is_valid_side_square(side_square)
        for rows_number in range(side_square):
            row = []
            for columns_number in range(side_square):
                row.append(background_sign)
            board.append(row)
        return board

    def _is_input_valid(self, player_response: str) -> str:
        if player_response.upper() in self.answers:
            return player_response.upper()
        else:
            print('Sorry your input is wrong, please try type it again')
            return self._is_input_valid(input('Do you wanna choose who starts? [y/n]\n'))

    def _is_valid_side_square(self, side_square: int) -> int:
        if self.min_board <= side_square <= self.max_board:
            return side_square
        else:
            raise ValueError(f'Currently side of the board cant be under {self.min_board} and over {self.max_board}')

    def _is_valid_side_sequence(self, sequence: int, side: int) -> int:
        if self.min_sequence >= sequence:
            raise ValueError(f'Winning sequence cannot be shorter than {self.min_sequence}')
        elif sequence > side:
            raise ValueError('Winning sequence cannot be longer than board edge')
        else:
            return sequence

    def _is_valid_background_sign(self, sign: str) -> str:
        if len(sign) == 0:
            raise ValueError('Sign must have any character')
        elif len(sign) > self.max_background_sign:
            raise ValueError(f'Sign must have less characters then {self.max_background_sign}')
        else:
            return sign

    def _is_valid_player_sign(self, sign: str, background_sign: str) -> str:
        if len(sign) == 0:
            raise ValueError('Sign must have any character')
        elif len(sign) > len(background_sign):
            raise ValueError('Sign must have less characters then background sign')
        else:
            return sign

    def _is_valid_letter(self, letter: str) -> bool:
        regex = '[A-{letter}a-{l_letter}]'.format(letter=self.alphabet[len(self.__board) - 1],
                                                  l_letter=self.alphabet[len(self.__board) - 1].lower())
        return True if bool(re.match(regex, letter)) and len(letter) == 1 else False

    def _is_valid_number(self, number: str) -> bool:
        if re.match('[1-9]', number) or re.match('[1-2][0-9]', number):
            return True if int(number) < self.__side_square else False
        else:
            return False

    def show_board(self):
        x = len(self.__board)
        for j in self.__board:
            print('{:{align}{width}}'.format(x, align='^', width=str(len(str(len(self.__board))))), end=' ')
            for i in range(len(j)):
                print('{:{align}{width}}'.format(j[i], align='^', width=str(len(self.__background_sign))), end=' ')
            print()
            x -= 1
        print(len(str(len(self.__board))) * ' ', end=' ')
        for z in range(len(self.__board)):
            print('{:{align}{width}}'.format(self.alphabet[z], align='^', width=str(len(self.__background_sign))),
                  end=' ')
        print('\n')

    def replace_sign(self, first_player: bool, place: str):
        letter = place[-1]
        number = place[:-1]
        if self._is_valid_letter(letter) and self._is_valid_number(number):
            if self.__board[-int(number)][self.alphabet.index(letter.upper())] == self.__background_sign:
                if not first_player:
                    self.__board[-int(number)][self.alphabet.index(letter.upper())] = self.__player2_sign
                else:
                    self.__board[-int(number)][self.alphabet.index(letter.upper())] = self.__player1_sign
            else:
                print('This field is taken')
                self.replace_sign(first_player, input(self.question_enter_square))
        else:
            print('Your input is wrong, please try again')
            self.replace_sign(first_player, input(self.question_enter_square))

    def check_win(self, first_player: bool) -> bool:
        sign = self.__player1_sign if first_player else self.__player2_sign
        self.win_status += self._check_vertical(sign)
        self.win_status += self._check_horizontal(sign)
        self.win_status += self._check_diagonal_left_up(sign)
        self.win_status += self._check_diagonal_left_down(sign)
        self.win_status += self._check_diagonal_right_up(sign)
        self.win_status += self._check_diagonal_right_down(sign)
        return True if self.win_status == 1 else False

    def _check_horizontal(self, sign: str) -> int:
        win_status = 0
        for row in self.__board:
            sum_of_seq = 0
            for index in range(len(row)):
                if row[index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    win_status = 1
                    return win_status
        return win_status

    def _check_vertical(self, sign: str) -> int:
        win_status = 0
        for index in range(len(self.__board)):
            sum_of_seq = 0
            for row in self.__board:
                if row[index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    win_status = 1
                    return win_status
        return win_status

    def _check_diagonal_left_down(self, sign: str) -> int:
        win_status = 0
        for start_index in range(len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = start_index
            for index in range(len(self.__board) - start_index):
                if self.__board[start][index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    win_status = 1
                    return win_status
                start += 1
        return win_status

    def _check_diagonal_left_up(self, sign: str) -> int:
        win_status = 0
        for start_index in range(1, len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = start_index
            for index in range(len(self.__board) - start_index):
                if self.__board[index][start] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    win_status = 1
                    return win_status
                start += 1
        return win_status

    def _check_diagonal_right_down(self, sign: str) -> int:
        win_status = 0
        for start_index in range(1, len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = start_index
            for index in range(len(self.__board) - 1, start_index - 1, -1):
                if self.__board[start][index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    win_status = 1
                    return win_status
                start += 1
        return win_status

    def _check_diagonal_right_up(self, sign: str) -> int:
        win_status = 0
        for start_index in range(len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = 0
            for index in range(len(self.__board) - 1, start_index - 1, -1):
                if self.__board[start][index - start_index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    win_status = 1
                    return win_status
                start += 1
        return win_status

    def full_board(self) -> bool:
        for row in self.__board:
            if self.__background_sign in row:
                return False
        return True

    def play_again(self) -> bool:
        again = None
        while again not in self.answers:
            again = input('Do you wanna play? [y/n]\n')
        return True if again.upper() == self.answers[0] else False

    def player_move(self, player_1_starts: bool) -> bool:
        print(f'Player {1 if player_1_starts else 2} turn\n')
        self.show_board()
        self.replace_sign(player_1_starts, input(self.question_enter_square))
        if self.check_win(player_1_starts):
            print(f'Player {1 if player_1_starts else 2} won game\n')
            self.show_board()
            return True
        elif self.full_board():
            print(f'Draw\n')
            self.show_board()
            return True
        return False

    def restart_game(self):
        self.__board = self.create_board(self.__side_square, self.__background_sign)

    def exit(self) -> bool:
        print('Thanks for the game, see you soon')
        return False

    def start(self) -> bool:
        print(f'Player 1 sign: {self.__player1_sign}')
        print(f'Player 2 sign: {self.__player2_sign}')
        player_choose = self._is_input_valid(input('Do you wanna choose who starts? [y/n]\n'))
        if player_choose.upper() == self.answers[0]:
            if self._is_input_valid(input('Should player 1 start?')) == self.answers[0]:
                player_1_starts = True
            else:
                player_1_starts = False
        else:
            player_1_starts = True if randint(0, 1) == 1 else False
        return player_1_starts
