# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # yellow
    FAIL = '\033[91m'    # red
    ENDC = '\033[0m'     # normal
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



    # print(bcolors.WARNING + string + bcolors.ENDC, end="  ")


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


    # printBoard(board, Xmax, Ymax)
    

    for coord in coords:
        board[coord[0]][coord[1]] = '#'

    printBoard(board, Xmax, Ymax)
    print(len(board), len(board[0]))
    print(Xmax, Ymax)        
    ## done prepping board


    for f in range(len(folds)):
        fold = folds[f]
        print(fold)
        if fold[0] == 'y':
            y = fold[1]
            for j in range(y):
                for i in range(Xmax + 1):
                    # print("" + str(i) + ":", j, board[i][j], (2*y) - j, board[i][(2*y) - j])
                    if board[i][j] == '#' or (((2*y) - j) <= Ymax and board[i][(2*y) - j] == '#'):
                        board[i][j] = '#'
                    # print(board[i][j], end="")    # print("match")
                    # print("(" + str(i) + "," + str(j) + ")", board[i][j],  "(" + str(i) + "," + str((2*y) - j) + ")", board[i][(2*y) - j])
                # print()
                    
            Ymax = y - 1
        elif fold[0] == 'x':
            x = fold[1]
            for i in range(x):
                for j in range(Ymax + 1):
                    # print("" + str(i) + ":", j, board[i][j], (2*y) - j, board[i][(2*y) - j])
                    if board[i][j] == '#' or (((2*x)-i) <= Xmax and board[(2*x)-i][j] == '#'):
                        board[i][j] = '#'
                    # print(board[i][j], end="")    # print("match")
                    # print("(" + str(i) + "," + str(j) + ")", board[i][j],  "(" + str(i) + "," + str((2*y) - j) + ")", board[i][(2*y) - j])
                # print()
                    
            Xmax = x - 1
        printBoard(board, Xmax, Ymax)

    count = 0
    for i in range(Xmax + 1):
        for j in range(Ymax + 1):
            if board[i][j] == '#':
                count += 1

    # print(Xmax, Ymax)

    # print(coords)
    # print(folds)

    # printBoard(board, Xmax, Ymax)

    return count


arr = readFile("AoC_Inputs/AoC_2021_d13_input.txt")
print(function(arr))


## Both d13 and d13_2 work; d13_2 is cleaner