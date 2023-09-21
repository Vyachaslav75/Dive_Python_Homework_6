from random import shuffle as sh


# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]


def check_queen(queens):
    board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
    if len(queens) > 8:
        return False
    #print(len(queens))
    for i in range(len(queens)):
        column, row = queens[i]
        #print(f"{column = }, {row = },  {i = }")
        if board[row][column] == 0:
            board = mark_board(board, column, row, i)
            #print_board(board)
            #print(f"True   {i = }")
        else:
            #print(f"{column = }, {row = }")
            return False
        #print()
    return True


def mark_board(board, column, row, i):
    offset1 = column - row
    offset2 = column + row
    for j in range(8):
        # if board[row][j] == 0:
        board[row][j] = i + 1
        # if board[j][column] == 0:
        board[j][column] = i + 1

        # offset1=column-row
        if j + offset1 > 0 and j + offset1 < 8:
            board[j][j + offset1] = i + 1

        # offset2=column+row
        if j + offset2 > 0 and j + offset2 < 8:
            board[j][j + offset2] = i + 1
            offset2 -= 2
    return board


def print_board(board):
    for i in board:
        print(i)


def gen_chess():
    res = []
    temp = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
    temp1 = [0, 1, 2, 3, 4, 5, 6, 7]
    while len(res) < 4:
        temp = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]]
        temp1 = [0, 1, 2, 3, 4, 5, 6, 7]
        # board = [
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        # ]
        for _ in range(8):
            sh(temp1)
            # print(temp1)
            temp[_][0] = temp1.pop(0)
        #print(temp)
        if check_queen(temp):
            res.append(temp)
    print('Четыре варианта размещения ферзей')
    print_board(res)
    # print(temp)


if __name__ == "__main__":
    queens = [[7, 4], [5, 0], [3, 7], [1, 3], [6, 6], [4, 2], [2, 5], [0, 1]]
    print(check_queen(queens))
    gen_chess()
