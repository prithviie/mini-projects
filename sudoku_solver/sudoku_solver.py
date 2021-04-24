
def print_board(bo):
    print()
    count = 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):

            if count >= 3:
                count = 0
                print('---------------------')

            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if bo[i][j] == 0:
                print('- ', end='')
            else:
                print(f'{bo[i][j]} ', end='')

        count += 1
        print()
    print()


def find_empty(bo):
    '''finds an empty spot in the board and returns its position'''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def is_valid(bo, num, pos):
    '''checks if the num is valid to insert into the current state of the board'''

    x, y = pos

    # checking if pos is valid in the row
    row = bo[x]
    if num in row:
        return False


    # checking if pos is valid in the column
    col = [bo[i][y] for i in range(len(bo[0]))]
    if num in col:
        return False


    # checking if pos is valid in box
    box_x = x // 3
    box_y = y // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if num == bo[j][i]:
                return False

    # if valid in all three conditions, return True
    return True


def solve(bo):
    '''solves the board recursively using backtracking'''
    
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

    # try inserting every value in range 1 to 9
    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            # if not solved empty the position
            bo[row][col] = 0

    return False

      
def main(board):
    
    print_board(board)

    input('Hit ENTER to solve ')

    solve(board)
    print_board(board)


# empty spots shown using number 0
board = [
    [3,0,6,  5,0,8,  4,0,0],
    [5,2,0,  0,0,0,  0,0,0],
    [0,8,7,  0,0,0,  0,3,1],

    [0,0,3,  0,1,0,  0,8,0],
    [9,0,0,  8,6,3,  0,0,5],
    [0,5,0,  0,9,0,  6,0,0],

    [1,3,0,  0,0,0,  2,5,0],
    [0,0,0,  0,0,0,  0,7,4],
    [0,0,5,  2,0,6,  3,0,0]
]

main(board)
