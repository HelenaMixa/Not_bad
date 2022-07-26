# Tic-tac-toe, with the possibility of playing on the field 3X3 or nXn, where 5<=n<=10.
import dataclasses

# MODEL


@dataclasses.dataclass
class Board:
    board = list()

    @staticmethod
    def check_win_for_size_3(board):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False

    @staticmethod
    def check_win(board, field_dimension):
        r = field_dimension
        # checking horizontal lines (5 in a row)
        for i in range(field_dimension):
            for j in range(field_dimension - 4):
                if board[j + i * r] == board[j + 1 + i * r] == board[j + 2 + i * r] == board[j + 3 + i * r] \
                        == board[j + 4 + i * r]:
                    if (j + i * r) % r == j and (j + 1 + i * r) % r == j + 1 and (j + 2 + i * r) % r == j + 2 \
                            and (j + 3 + i * r) % r == j + 3 and (j + 4 + i * r) % r == j + 4:
                        return board[j + i * r]
        # checking verticals (5 in a row)
        for j in range(field_dimension - 4):
            for i in range(field_dimension):
                if board[i + j * r] == board[i + (j + 1) * r] == board[i + (j + 2) * r] == board[i + (j + 3) * r] \
                        == board[i + (j + 4) * r] == "X":
                    if (i + j * r) % r == (i + (j + 1) * r) % r == (i + (j + 2) * r) % r == (i + (j + 3) * r) % r \
                            == (i + (j + 4) * r) % r:
                        return board[i + j * r]
                if board[i + j * r] == board[i + (j + 1) * r] == board[i + (j + 2) * r] == board[i + (j + 3) * r]\
                        == board[i + (j + 4) * r] == "O":
                    if (i + j * r) % r == (i + (j + 1) * r) % r == (i + (j + 2) * r) % r == (i + (j + 3) * r) % r \
                            == (i + (j + 4) * r) % r:
                        return board[i + j * r]
        # diagonal check (5 in a row)
        for k in range(field_dimension - 4):
            for i in range(field_dimension-4):
                for j in range(field_dimension-4):
                    if board[k * (r + 1) - i + j] == board[(k + 1) * (r + 1) - i + j] \
                            == board[(k + 2) * (r + 1) - i + j] == board[(k + 3) * (r + 1) - i + j] \
                            == board[(k + 4) * (r + 1) - i + j]:
                        return board[k * (r + 1) - i + j]

                    if board[(k + 1) * (r - 1) - i + j] == board[(k + 2) * (r - 1) - i + j] \
                            == board[(k + 3) * (r - 1) - i + j] == board[(k + 4) * (r - 1) - i + j] \
                            == board[(k + 5) * (r - 1) - i + j]:
                        return board[(k + 1) * (r - 1) - i + j]
        return False


# VIEW


class View:
    def draw_board(self, board):
        print("----" * field_dimension)
        for row in range(field_dimension):
            for cell in range(field_dimension):
                if cell + row * field_dimension < 9 and board[cell + row * field_dimension] != "X" \
                        and board[cell + row * field_dimension] != "O":
                    print((board[cell + row * field_dimension] or ' '), end="  |")
                if cell + row * field_dimension >= 9 and board[cell + row * field_dimension] != "X" \
                        and board[cell + row * field_dimension] != "O":
                    print((board[cell + row * field_dimension] or ' '), end=" |")
                if board[cell + row * field_dimension] == "X" or board[cell + row * field_dimension] == "O":
                    print((board[cell + row * field_dimension] or ' '), end="  |")
            print()
            print("----" * field_dimension)

    def print_message(self, message):
        print(message)


# CONTROLLER

@dataclasses.dataclass
class Controller:

    def take_input(self, player_token, board):
        valid = False
        while not valid:
            player_answer = input("Select a cell for " + player_token + "? ")
            try:
                player_answer = int(player_answer)
            except ValueError:
                view.print_message("Oops! Invalid input. Are you sure you entered a number?  Try again...")
                continue
            if 1 <= player_answer <= size:
                if str(board[player_answer - 1]) not in "XO":
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    view.print_message("This cell is already taken")
            else:
                view.print_message("Incorrect input. Enter a number from 1 to " + str(size))

    def start_game(self, board):
        win = False
        move_number = 0
        while not win:
            view.draw_board(board)
            if move_number % 2 == 0:
                controller.take_input("X", board)
            else:
                controller.take_input("O", board)
            move_number += 1
            if field_dimension == 3:
                if move_number > 4:
                    tmp = Board.check_win_for_size_3(board)
                    view.draw_board(board)
                    if tmp:
                        view.print_message(tmp + "  Won!")
                        win = True
                        break
            else:
                if move_number >= 9:
                    tmp = Board.check_win(board, field_dimension)
                    view.draw_board(board)
                    if tmp:
                        view.print_message(tmp + "  Won!")
                        win = True
                        break
            if move_number == size:
                view.draw_board(board)
                view.print_message("Dead heat!")
                break


if __name__ == '__main__':
    controller = Controller()
    view = View()
    board = Board()
    view.print_message("START THE GAME!")
    while True:
        try:
            field_dimension = int(input("Please enter the field_dimension 3X3 or nXn, n>=5, maximum possible 10x10"))
            if field_dimension in (1, 2, 4) or field_dimension > 10:
                view.print_message("Oops! Invalid input.Please enter the field_dimension 3X3 or nXn, n>=5, "
                                   "maximum possible 10x10.")
                continue
            size = field_dimension * field_dimension
            board = list(range(1, size+1))
            controller.start_game(board)
            play_again = input("Play again? ")
            if not play_again or play_again.lower() in ['no', 'n', 'ні']:
                break
        except ValueError:
            view.print_message("Oops! Invalid input. Are you sure you entered a number?  Try again...")
        continue
