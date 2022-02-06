# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words



def printBoard(board, x, y):
    for j in range(y+1):
        for i in range(x+1):
            print(board[i][j], end="")
        print()
    print()



def function(arr):
    print(arr)

    ## * Parses Inputs
    coords = []
    folds = []
    foldinput = False
    for line in arr:
        # Parse '#' input
        if line != "" and not foldinput:
            coord = line.split(",")
            coords.append([int(coord[0]), int(coord[1])])
        
        # Parse fold input
        elif foldinput:
            temp = line.split(" ")
            fold = temp[2].split("=")
            folds.append([fold[0], int(fold[1])])

        # If newline, fold input starts
        else:
            foldinput = True

    ## * Preps "Paper"
    ## Get X and Y maxes for array creation
    Xmax = 0 # max(lis, key=lambda x:x[0])[0]
    Ymax = 0 # max(lis, key=lambda x:x[1])[1]
    for coord in coords:
        if coord[0] > Xmax:
            Xmax = coord[0]
        if coord[1] > Ymax:
            Ymax = coord[1]

    ## Create board
    board = []
    for i in range(Xmax+1):
        line = []
        for j in range(Ymax+1):
            line.append('.')
        board.append(line)

    
    ## Enters '#''s into board
    for coord in coords:
        board[coord[0]][coord[1]] = '#'

    printBoard(board, Xmax, Ymax)
    print(len(board), len(board[0]))
    print(Xmax, Ymax)        
    ## Done prepping board


    ## Performs each fold; P1 change to 1 fold
    for f in range(len(folds)):
        fold = folds[f]
        print(fold)

        if fold[0] == 'y':
            y = fold[1]
            for j in range(y):
                for i in range(Xmax + 1):
                    if board[i][j] == '#' or (((2*y) - j) <= Ymax and board[i][(2*y) - j] == '#'):
                        board[i][j] = '#'
            Ymax = y - 1


        elif fold[0] == 'x':
            x = fold[1]
            for i in range(x):
                for j in range(Ymax + 1):
                    if board[i][j] == '#' or (((2*x)-i) <= Xmax and board[(2*x)-i][j] == '#'):
                        board[i][j] = '#'
            Xmax = x - 1


        printBoard(board, Xmax, Ymax)

    count = 0
    for i in range(Xmax + 1):
        for j in range(Ymax + 1):
            if board[i][j] == '#':
                count += 1


    return count


arr = readFile("AoC_Inputs/AoC_2021_d13_input.txt")
print(function(arr))


## Both d13 and d13_2 work; d13_2 is cleaner