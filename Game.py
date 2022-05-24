import re


class Game:
    alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

    def __init__(self, side_square: int, background_sign: str, player1_sign: str, player2_sign: str,
                 sequence_number: int):
        board = []
        side_square = self._is_valid_side_square(side_square)
        for i in range(side_square):
            row = []
            for j in range(side_square):
                row.append(background_sign)
            board.append(row)
        self.__board = board
        self.__background_sign = self._is_valid_background_sign(background_sign)
        self.__player1_sign = self._is_valid_player_sign(player1_sign, background_sign)
        self.__player2_sign = self._is_valid_player_sign(player2_sign, background_sign)
        self.__sequence_number = self._is_valid_side_sequence(sequence_number, side_square)

    def get_player1_sign(self):
        return self.__player1_sign

    def get_player2_sign(self):
        return self.__player2_sign

    def _is_valid_side_square(self, side_square: int):
        if 2 < side_square < 27:
            return side_square
        else:
            raise ValueError("Currently side of the board cant be under 3 and over 26")

    def _is_valid_background_sign(self, sign: str):
        if len(sign) == 0:
            raise ValueError("Sign must have any character")
        elif len(sign) > 4:
            raise ValueError("Sign must have less characters then 4")
        else:
            return sign

    def _is_valid_player_sign(self, sign: str, background_sign: str):
        if len(sign) == 0:
            raise ValueError("Sign must have any character")
        elif len(sign) > len(background_sign):
            raise ValueError("Sign must have less characters then background sign")
        else:
            return sign

    def _is_valid_side_sequence(self, sequence: int, side: int):
        if 2 >= sequence:
            raise ValueError("Winning sequence cannot be shorter than 1")
        elif sequence > side:
            raise ValueError("Winning sequence cannot be longer than board edge")
        else:
            return sequence

    def _is_valid_letter(self, letter: str):
        regex = '[A-{letter}a-{l_letter}]'.format(letter=self.alphabet[len(self.__board) - 1],
                                                  l_letter=self.alphabet[len(self.__board) - 1].lower())
        return True if bool(re.match(regex, letter)) and len(letter) == 1 else False

    def _is_valid_number(self, number: str):
        if re.match('[1-9]', number) or re.match('[1-2][0-9]', number):
            return True if int(number) < 27 else False
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
        print("\n")

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
                self.replace_sign(first_player, input('Enter your square: [first number last letter no gap between]\n'))
        else:
            print('Your input is wrong, please try again')
            self.replace_sign(first_player, input('Enter your square: [first number last letter no gap between]\n'))

    def check_win(self, first_player: bool):
        if first_player:
            if self._check_horizontal(self.__player1_sign):
                return True
            elif self._check_vertical(self.__player1_sign):
                return True
            elif self._check_diagonal_left_down(self.__player1_sign):
                return True
            elif self._check_diagonal_right_down(self.__player1_sign):
                return True
            elif self._check_diagonal_right_up(self.__player1_sign):
                return True
            elif self._check_diagonal_left_up(self.__player1_sign):
                return True
        else:
            if self._check_horizontal(self.__player2_sign):
                return True
            elif self._check_vertical(self.__player2_sign):
                return True
            elif self._check_diagonal_left_down(self.__player2_sign):
                return True
            elif self._check_diagonal_right_down(self.__player2_sign):
                return True
            elif self._check_diagonal_right_up(self.__player2_sign):
                return True
            elif self._check_diagonal_left_up(self.__player2_sign):
                return True
        return False

    def _check_horizontal(self, sign: str):
        for row in self.__board:
            sum_of_seq = 0
            for index in range(len(row)):
                if row[index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    return True
        return False

    def _check_vertical(self, sign: str):
        for index in range(len(self.__board)):
            sum_of_seq = 0
            for row in self.__board:
                if row[index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    return True
        return False

    def _check_diagonal_left_down(self, sign: str):
        for start_index in range(len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = start_index
            for index in range(len(self.__board) - start_index):
                if self.__board[start][index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    return True
                start += 1
        return False

    def _check_diagonal_left_up(self, sign: str):
        for start_index in range(1, len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = start_index
            for index in range(len(self.__board) - start_index):
                if self.__board[index][start] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    return True
                start += 1
        return False

    def _check_diagonal_right_down(self, sign: str):
        for start_index in range(1, len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = start_index
            for index in range(len(self.__board) - 1, start_index - 1, -1):
                if self.__board[start][index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    return True
                start += 1
        return False

    def _check_diagonal_right_up(self, sign: str):
        for start_index in range(len(self.__board) + 1 - self.__sequence_number):
            sum_of_seq = 0
            start = 0
            for index in range(len(self.__board) - 1, start_index - 1, -1):
                if self.__board[start][index - start_index] == sign:
                    sum_of_seq += 1
                else:
                    sum_of_seq = 0
                if sum_of_seq == self.__sequence_number:
                    return True
                start += 1
        return False

    def full_board(self):
        for row in self.__board:
            if self.__background_sign in row:
                return False
        return True
