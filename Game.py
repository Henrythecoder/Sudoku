import math
import copy
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



playerBoard = copy.deepcopy(board)


def solve(bo):

    position = get_empty(bo)

    if position == False:
        return True

    row, col = position

    for num in range (1,10):
        if valid(bo,row, col, num):
            bo[row][col] = num

            if solve(bo):
                return True

            bo[row][col] = 0

    return False






def valid(bo, row, col, number):
    # check valid on row
    for c in range(9):
        if bo [row][c] == number:
            return False

    # check valid on col
    for r in range(9):
        if bo[r][col] == number:
            return False

    # check valid on square
    temp_row =  math.floor(row/3) * 3
    temp_col = math.floor(col/3) * 3
    max_row = temp_row + 3
    max_col = temp_col + 3

    for r in range(temp_row, max_row):
        for c in range(temp_col, max_col):
            if bo[r][c] == number:
                return False

    return True



def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            print(bo[i][j], end=" ")
            if j == 8:
                print()


def get_empty(bo):
    for i in range(len(bo)):

        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j


    return False








