import random


OPEN = ' '
X = 'X'
O = '0'


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


def valid_input(inp: str) -> bool:
    valid: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return inp in valid


def play_turn(_board: dict[int: str], turn: str):
    tmp_board = _board.copy()
    while True:
        print(f"[{turn}] Enter a number that represents an open space on the board:")
        move: str = input()

        if not valid_input(move):
            print("Invalid input. Enter a number from 1-9")
            continue
        if tmp_board[int(move)] == OPEN:
            tmp_board[int(move)] = turn

            if did_i_win(tmp_board):
                print_board(tmp_board)
                print(f"Congratulations team {turn}!")
                exit()
                break

            if all([item != ' ' for item in tmp_board.values()]):
                print('Draw!')
                print_board(tmp_board)
                exit()
                break
            print_board(tmp_board)
            turn = X if turn == O else O
            play_turn(tmp_board, turn)
            break
        else:
            print("That space is occupied")
            continue


def main(_board: dict[int: str], turn: str):
    print_board(_board)
    print("Welcome! Each space on the board is represented by a number. The numbers are in ascending order and continues at the start of each row.")
    play_turn(_board, turn)


if __name__ == '__main__':
    turns = [X, O]
    rnd_turn = random.choice(turns)
    main(board, rnd_turn)
