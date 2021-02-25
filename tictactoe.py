import random
import time

OPEN = ' '
X = 'X'
O = '0'
valid: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

board: dict[int: str] = {1: OPEN, 2: OPEN, 3: OPEN,
                         4: OPEN, 5: OPEN, 6: OPEN,
                         7: OPEN, 8: OPEN, 9: OPEN}


def print_board(_board: dict[int: str]):
    print(_board[1] + '|' + _board[2] + '|' + _board[3])
    print("-+-+-")
    print(_board[4] + '|' + _board[5] + '|' + _board[6])
    print("-+-+-")
    print(_board[7] + '|' + _board[8] + '|' + _board[9])


def did_i_win(_board: dict[int: str]) -> bool:
    if _board[1] == _board[2] == _board[3] != OPEN:
        return True
    if _board[4] == _board[5] == _board[6] != OPEN:
        return True
    if _board[7] == _board[8] == _board[9] != OPEN:
        return True
    if _board[1] == _board[4] == _board[7] != OPEN:
        return True
    if _board[2] == _board[5] == _board[8] != OPEN:
        return True
    if _board[3] == _board[6] == _board[9] != OPEN:
        return True
    if _board[1] == _board[5] == _board[9] != OPEN:
        return True
    if _board[3] == _board[5] == _board[7] != OPEN:
        return True
    return False


def valid_input(inp: int) -> bool:
    return inp in valid


def empty_squares(_board: dict[int: str]) -> bool:
    return ' ' in _board.values()


def play_turn(_board: dict[int: str], turn: str, computer: bool = False):
    tmp_board = _board.copy()
    while empty_squares(tmp_board):

        if computer and turn == O:
            unoccupied_squares: list[int] = [i for i in range(1, len(tmp_board)+1) if tmp_board[i] == ' ']
            val: int = random.choice(unoccupied_squares)
            time.sleep(0.8)
        else:
            print(f"[{turn}] Enter a number that represents an open space on the board:")
            move: str = input()
            try:
                val = int(move)
                if not valid_input(val):
                    raise ValueError
            except ValueError:
                print("Invalid input. Enter a number from 1-9")
                continue
        if tmp_board[val] == OPEN:
            tmp_board[val] = turn

            if did_i_win(tmp_board):
                print_board(tmp_board)
                print(f"Congratulations team {turn}!")
                exit()
            print_board(tmp_board)
            turn = X if turn == O else O
            play_turn(tmp_board, turn, computer)
            break
        else:
            print("That space is occupied")

    print('Draw!')
    exit()


def main(_board: dict[int: str], turn: str):
    print_board(_board)
    print("Welcome! Each space on the board is represented by a number. The numbers are in ascending order and continues at the start of each row.")

    while True:
        print("Would you like to play with a computer?")
        ans: str = input()

        if ans == 'Y':
            play_turn(_board, turn, computer=True)
        elif ans == 'N':
            play_turn(_board, turn)
        else:
            print("Invalid answer. Looking for 'Y' or 'N'")


if __name__ == '__main__':
    rnd_turn = random.choice([X, O])
    print(rnd_turn)
    main(board, rnd_turn)
