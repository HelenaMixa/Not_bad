# Tic-tac-toe, with the possibility of playing on the field 3X3 or nXn, where 5<=n<=10.
import dataclasses

# MODEL


@dataclasses.dataclass
class Board:
    field = list(range(0, 100))
    game_is_over = False
    is_valid: bool = False
    is_clicked: bool = False

    def check_win_for_size_3(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.field[each[0]] == self.field[each[1]] == self.field[each[2]]:
                return self.field[each[0]]
        return False

    def click_cell(self, player_answer):
        if str(self.field[player_answer - 1]) in "XO":
            self.is_clicked = True
            return self.is_clicked
        return False

    def is_coords_inside(self, player_answer):
        return (
            1 <= player_answer <= size
        )

    def check_win(self):
        # checking horizontal lines (5 in a row)
        for i in range(field_dimension):
            for j in range(field_dimension - 4):
                chek_hor_line = self.field[j + i * field_dimension]
                count = 0
                for p in range(5):
                    if (self.field[j + i * field_dimension + p] == chek_hor_line) \
                            and ((j+i*field_dimension + p) % field_dimension == j+p):
                        count = count + 1
                if count >= 5:
                    return self.field[j + i * field_dimension]

        # checking verticals (5 in a row)
        for j in range(field_dimension - 4):
            for i in range(field_dimension):
                chek_vert_line = self.field[i + j * field_dimension]
                ind_chek_vert_line = (i + j * field_dimension) % field_dimension
                count = 0
                for p in range(5):
                    if (self.field[i + (j + p) * field_dimension] == chek_vert_line) and \
                            ((i + (j + p) * field_dimension) % field_dimension == ind_chek_vert_line):
                        count = count + 1
                if count >= 5:
                    return self.field[i + j * field_dimension]

        # diagonal check (5 in a row)
        for k in range(field_dimension - 4):
            for i in range(field_dimension-4):
                for j in range(field_dimension-4):
                    ch = self.field[k * (field_dimension + 1) - i + j]
                    ch1 = self.field[(k + 1) * (field_dimension - 1) - i + j]
                    count = 1
                    count1 = 1
                    for p in range(0, 4):
                        if self.field[(k + p) * (field_dimension + 1) - i + j] == ch:
                            count = count + 1
                        if self.field[(k + 1 + p) * (field_dimension - 1) - i + j] == ch1:
                            count1 = count1 + 1
                    if count == 5:
                        return self.field[k * (field_dimension + 1) - i + j]
                    if count1 == 5:
                        return self.field[(k + 1) * (field_dimension - 1) - i + j]
        return False

# VIEW


class View:
    board = Board()

    def draw_board(self, board):
        print("----" * field_dimension)
        for row in range(field_dimension):
            for cell in range(field_dimension):
                if cell + row * field_dimension < 9 and self.board.field[cell + row * field_dimension] != "X" \
                        and self.board.field[cell + row * field_dimension] != "O":
                    print((self.board.field[cell + row * field_dimension] or ' '), end="  |")
                if cell + row * field_dimension >= 9 and self.board.field[cell + row * field_dimension] != "X" \
                        and self.board.field[cell + row * field_dimension] != "O":
                    print((self.board.field[cell + row * field_dimension] or ' '), end=" |")
                if self.board.field[cell + row * field_dimension] == "X" or \
                        self.board.field[cell + row * field_dimension] == "O":
                    print((self.board.field[cell + row * field_dimension] or ' '), end="  |")
            print()
            print("----" * field_dimension)

    def print_message(self, message):
        print(message)


# CONTROLLER

@dataclasses.dataclass
class Controller:
    board = Board()

    def take_input(self, player_token):
        self.board.is_valid = False
        while not self.board.is_valid:
            player_answer = input("Select a cell for " + player_token + "? ")
            try:
                player_answer = int(player_answer)
            except ValueError:
                view.print_message("Oops! Invalid input. Are you sure you entered a number?  Try again...")
                continue
            if self.board.is_coords_inside(player_answer):
                self.board.click_cell(player_answer)
                if self.board.is_clicked:
                    view.print_message("This cell is already taken, choose another one!")
                    self.board.is_clicked = False
                else:
                    self.board.field[player_answer - 1] = player_token
                    self.board.is_valid = True
            else:
                view.print_message("Incorrect input. Enter a number from 1 to " + str(size))

    def start_game(self):
        move_number = 0
        self.board.game_is_over = False
        for row in range(field_dimension*field_dimension):
            self.board.field[row] = row+1
        while not self.board.game_is_over:
            tmp = False
            view.draw_board(self.board)
            if move_number % 2 == 0:
                controller.take_input("X")
            else:
                controller.take_input("O")
            move_number += 1
            if field_dimension == 3 and move_number > 4:
                tmp = self.board.check_win_for_size_3()
                print(tmp)
            else:
                if move_number >= 9:
                    tmp = self.board.check_win()
            if tmp:
                view.draw_board(self.board)
                self.board.game_is_over = True
                view.print_message(tmp + "  Won!")
                break
            if move_number == size:
                view.draw_board(self.board)
                view.print_message("Dead heat!")
                break


if __name__ == '__main__':
    controller = Controller()
    view = View()
    view.print_message("START THE GAME!")
    while True:
        try:
            field_dimension = int(input("Please enter the field_dimension 3X3 or nXn, n>=5, maximum possible 10x10"))
            if field_dimension in (1, 2, 4) or field_dimension > 10:
                view.print_message("Oops! Invalid input.Please enter the field_dimension 3X3 or nXn, n>=5, "
                                   "maximum possible 10x10.")
                continue
            size = field_dimension * field_dimension
            controller.start_game()
            play_again = input("Play again? ")
            if not play_again or play_again.lower() in ['no', 'n', 'РЅС–']:
                break
        except ValueError:
            view.print_message("Oops! Invalid input. Are you sure you entered a number?  Try again...")
        continue
