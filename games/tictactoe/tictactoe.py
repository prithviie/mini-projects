import random

def print_board(board):

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == ' '


def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
            (bo[4] == le and bo[5] == le and bo[6] == le) or \
            (bo[1] == le and bo[2] == le and bo[3] == le) or \
            (bo[1] == le and bo[4] == le and bo[7] == le) or \
            (bo[2] == le and bo[5] == le and bo[8] == le) or \
            (bo[3] == le and bo[6] == le and bo[9] == le) or \
            (bo[1] == le and bo[5] == le and bo[9] == le) or \
            (bo[3] == le and bo[5] == le and bo[7] == le)


def select_random(li):
    return random.choice(li)


def is_board_full(board):
    if board.count(' ') >= 1:
        return False
    else:
        return True


def player_move():
    run = True

    while run:
        move = input("Select position to place 'x' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('x', move)
                else:
                    print('The position is occupied')
            else:
                print('Please insert position in range 1-9')

        except:
            print('Please enter a number!')


def comp_move():
    
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and  x != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let

            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
    
    return move


def main():
    print('Welcome to Tic-Tac-Toe!')
    print_board(board)

    while not(is_board_full(board)):

        if not(is_winner(board, 'o')):
            player_move()
            # print_board(board)
        else:
            print('Computer won!')
            break

        if not(is_winner(board, 'x')):
            move = comp_move()
            if move == 0:
                print('Tie')
            else:
                insert_letter('o', move)
                print('Computer placed o at position ' + str(move))
                print_board(board)

        else:
            print('You won!')
            break

    if is_board_full(board):
        print('Tie')


board = [' ' for x in range(10)]
main()
