
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    count = 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):

            if count >= 3:
                count = 0
                print('---------------------')

            if j % 3 == 0 and j != 0:
                print('| ', end='')

            print(str(bo[i][j]) + ' ', end='')
            # print(str((i, j)) + ' ', end='')

        count += 1
        print()


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def is_valid(bo, num, pos):

    x, y = pos

    # bo[x][y] = '*'
    # print_board(bo)

    # print()
    # print('num -->', str(num))
    
    # print('pos --> ', end='')
    # print(x, y)
    # print()


    # check row

    row = bo[x]
    if num in row:
        # print('row', end=' --> ')
        # print(row)
        return False


    # check col

    col = [bo[i][y] for i in range(len(bo[0]))]
    if num in col:
        # print('col', end=' --> ')
        # print(col)
        return False


    # check box

    box_x = x // 3
    box_y = y // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if num == bo[j][i]:
                # print('box', end=' --> ')
                return False

    return True


def solve(bo):
    
    find = find_empty(bo)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


print_board(board)
solve(board)
print()
print('---------------------')
print()
print_board(board)
