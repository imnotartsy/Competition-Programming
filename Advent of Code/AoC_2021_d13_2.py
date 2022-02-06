# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

## D13 and D13_2 should both work; D13_2 handles case where folds 'up', bottom
## of 'paper' is higher than the top of the paper


def printBoard(board, x, y):
    for j in range(y+1):
        for i in range(x+1):
            print(board[i][j], end="")
        print()
    print()

def function(arr):
    print(arr)

    coords = []
    folds = []
    foldinput = False
    for line in arr:
        if line != "" and not foldinput:
            coord = line.split(",")
            coords.append([int(coord[0]), int(coord[1])])
        elif foldinput:
            temp = line.split(" ")
            fold = temp[2].split("=")
            folds.append([fold[0], int(fold[1])])
        else:
            foldinput = True

    Xmax = 0
    Ymax = 0
    for coord in coords:
        if coord[0] > Xmax:
            Xmax = coord[0]
        if coord[1] > Ymax:
            Ymax = coord[1]


    board = []
    for i in range(Xmax+1):
        line = []
        for j in range(Ymax+1):
            line.append('.')
        board.append(line)
    

    for coord in coords:
        board[coord[0]][coord[1]] = '#'

    # Print initial board stats
    print(len(board), len(board[0]))
    print(Xmax, Ymax)        
    ## Done prepping board


    for f in range(len(folds)):
        fold = folds[f]
        print(fold)

        if fold[0] == 'y':
            y = fold[1]
            new_height = y if y > Ymax - y else Ymax - y
            print("New Height:", new_height)

            for j in range(Ymax+1):
                # if j == fold[1]:
                #     print("--"*Xmax)
                for i in range(Xmax+1):
                    if board[i][j] == '#' or (((2*new_height) - j) <= Ymax and board[i][(2*new_height) - j] == '#'):
                        board[i][j] = '#'

            Ymax = new_height - 1

        if fold[0] == 'x':
            x = fold[1]
            new_width = x if x > Xmax - x else Xmax - x
            print("New Width:", new_width)
            for j in range(Ymax+1):
                for i in range(Xmax+1):
                    # if i == fold[1]:
                    #     print(" | ", end="")

                    if board[i][j] == '#' or (((2*new_width)-i) <= Xmax and board[(2*new_width)-i][j] == '#'):
                        board[i][j] = '#'

            Xmax = new_width - 1

    ## P1: Count #'s
    count = 0
    for i in range(Xmax + 1):
        for j in range(Ymax + 1):
            if board[i][j] == '#':
                count += 1

    ## P2: Print final board
    printBoard(board, Xmax, Ymax)

    return count


arr = readFile("AoC_Inputs/AoC_2021_d13_input.txt")
print(function(arr))