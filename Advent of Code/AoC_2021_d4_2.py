# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

def printBoards(boards):
    for board in boards:
        for row in board:
            print(row)
        print()


# this could be improved to O(n) if the marked spots were kept in a dictionary \
# and updated with each num; instead if is O(n^2)
# Returns: Board #, Row #, Col #, and 0 if row, 1 if column
def checkBoards(boards):
        # row major
        for b in range(len(boards)):
            for row in range(len(boards[b])):
                rowcount = 0
                for col in range(len(boards[b][row])):
                    if boards[b][row][col] < 0:
                        rowcount += 1
                if rowcount == 5:
                    print("FOUND", [b, row, col] )
                    return [b, row, col, 0] 

        # columnwise
            for col in range(len(boards[b][0])):
                colcount = 0
                for row in range(len(boards[b])):
                    if boards[b][row][col] < 0:
                        colcount += 1
                    if colcount == 5:
                        print("FOUND", [b, row, col] )
                        return [b, row, col, 1] 


        return 0

def checkAll(boards):
        found = False

        # row major
        for b in range(len(boards)):
            for row in range(len(boards[b])):
                rowcount = 0
                for col in range(len(boards[b][row])):
                    if boards[b][row][col] <= 0:
                        rowcount += 1
                if rowcount == 5:
                    found = True
                    break
                    # return 0

            # columnwise
            if not found:  
                for col in range(len(boards[b][0])):
                    colcount = 0
                    for row in range(len(boards[b])):
                        if boards[b][row][col] < 0:
                            colcount += 1
                        if colcount == 5:
                            found = True
                            break

            if not found:
                return b
                
            found = False

        return -1

def calcSum(board):
    sum = 0
    for row in board:
        for num in row:
            if num >= 0:
                sum += num
    return sum
            

def bingo(arr):
    # print(arr)
    nums = [int(x) for x in arr[0].split(',')]
    print(nums)

    boards = []
    board = []
    board_count = 0
    for line in arr[2:]:
        # print(line)
        if line == "":
            board_count += 1
            boards.append(board)
            board = []
        else:
            row = [int(x) for x in line.split()]
            board.append(row)

    # no newline at the end of the input
    board_count += 1
    boards.append(board)


    # print(board_count)
    printBoards(boards)

    import collections

    # Creates a dictonary of all call numbers with a list of their
    # position in the boards
    poses = collections.defaultdict(list)

    # Could use lambda function with a triple loop
    for b in range(len(boards)):
        for row in range(len(board)):
            for col in range(len(board[row])):
                poses[boards[b][row][col]].append([b, row, col])
        
    # import json
    # print(json.dumps(poses, indent=1))
    # print(poses)
   

    lastboard = 0
    for num in nums:
        if num in poses:
            print("NUM!", num, end=': ')#, "AT", poses[num])
            for pos in poses[num]:
                print(pos, end="")
                boards[pos[0]][pos[1]][pos[2]] *= -1
                if boards[pos[0]][pos[1]][pos[2]] == 0:
                    boards[pos[0]][pos[1]][pos[2]] = -6969696969
            print()
            printBoards(boards)

            ## P1 - get first winning board
            # win = checkBoards(boards)
            # if win != 0:
            #     return calcSum(boards[win[0]]) * boards[pos[0]][pos[1]][pos[2]] * -1
            
            ## P2 - get last winning board
            lastwin = checkAll(boards)
            print("Last board:", lastboard)
            if lastwin == -1:
                print("LAST WIN!")
                print("Last Board Sum:", calcSum(boards[lastboard]))
                print("Comleting Num:", boards[pos[0]][pos[1]][pos[2]]*-1)
                print(boards[lastboard])
                # print(len(boards))
                return calcSum(boards[lastboard]) * boards[pos[0]][pos[1]][pos[2]] * -1

            # quick and dirty way of saving last (first-in-order)-unsolved puzzle
            lastboard = lastwin





arr = readFile("AoC_Inputs/AoC_2021_d4_input.txt")
print(bingo(arr))