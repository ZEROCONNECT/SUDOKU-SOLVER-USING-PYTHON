import copy

board = [
    '.........',
    '5.3.67...',
    '9..3421..',
    '.....4...',
    '..1...72.',
    '..2.1....',
    '.3......9',
    '.8.1..2..',
    '...75.8.6'
]

def main():
    global board
    for idx, line in enumerate(board): #enumerate returns the index of each line
        board[idx] = list(line)
        #print(list(line))
    solve()
    print_board()


def solve():

        global board
        try:
            fill_all_obvious()
        except:
            return False

        if is_complete():
            return True

        i,j = 0,0
        for row_idx,row in enumerate(board):
            for col_idx,col in enumerate(row):
                if col ==".":
                    i,j = row_idx, col_idx

        possibilities = get_possibilities(i, j)
        for value in possibilities:
            snapshot = copy.deepcopy(board)

            board[i][j]= value
            result = solve()
            if result == True:
                return True
            else:
                board = copy.deepcopy(snapshot)
        return False

# for filling all obvious places..
def fill_all_obvious():
    global board

    while True:
        something_change = False
        for i in range(0,9):
            for j in range(0,9):
                possibilities = get_possibilities(i, j)
                if possibilities == False:
                    continue
                if len(possibilities)== 0:
                    raise RuntimeError("no moves left")
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    something_change = True
        if something_change == False:
         return

#  For getting all possible states to be there in a empty place
def get_possibilities(i, j):
    global board
    if board[i][j] != '.':
        return False

    possibilities = {str(n) for n in range(1,10)} # creating a set so for the subtraction of values will we easy
                                                    # giving every thing from 1 t0 9

    for val in board[i]:              # this is for the row_operation: remove everything that is not required in the row
        possibilities -= set(val)

    for idx in range(0,9):
        possibilities -= set(board[idx][j]) # j is fixed  so that we can traverse through the column
                                                # removing everything that is not required bu the column also
# now we have to consider of a square of 3x3
    i_start = (i//3) *3  # ['//' integer division] by doing so, we are at exact square in which we want to do operation -- row
    j_start = (j//3) *3  # by doing so, we are at exact square in which we want to do operation -- column


    sub_board = board[i_start:i_start+3]
    for idx, row in enumerate(sub_board):      # also removing elements that are not required in its own square
        sub_board[idx] = row[j_start:j_start+3]

    for row in sub_board:
        for col in row:
            possibilities -= set(col)
    return list(possibilities)

# for checking if the places were filled or not
def is_complete():
    for row in board:
        for col in row:
            if col == "." :
                return  False
    return True


# just for printing in a nice way
def print_board():
    global board
    for row in board:
        for col in row:
            print(col,end="")
        print("")

main()



