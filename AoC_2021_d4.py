# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import re

def printBoards(boards):
        for board in boards:
            for line in board:
                print(line)
            print()

def bingo(arr):
    nums = arr[0].split(",")
    print(nums)
    print(arr[1:])

    boards = []
    board = []
    board_size = 5
    board_count = 0

    for line in arr[1:]:
        if line == "":
            boards.append(board)
            board = []
            board_count += 1
        else:
            board.append([int(i) for i in line.split()]) 

    
    boards.append(board)

    board_size -= 2
    boards = boards [1:]
    
    # checks = [[[0]*board_size]*board_size] * board_count
    # checks = [
    #     [
    #         [0, 1, 2, 3, 4],
    #      [10, 11, 12, 13, 14],
    #      [20, 21, 22, 23, 24],
    #      [30, 31, 32, 33, 34],
    #      [40, 41, 42, 43, 44]
    #     ],
    #     [
    #         [0, 1, 2, 3, 4],
    #      [10, 11, 12, 13, 14],
    #      [20, 21, 22, 23, 24],
    #      [30, 31, 32, 33, 34],
    #      [40, 41, 42, 43, 44]
    #     ],
    #     [
    #         [0, 1, 2, 3, 4],
    #      [10, 11, 12, 13, 14],
    #      [20, 21, 22, 23, 24],
    #      [30, 31, 32, 33, 34],
    #      [40, 41, 42, 43, 44]
    #     ]
    # ]
    checks = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],] ]

    printBoards(checks)
    # print(checks[0][0][0])
    printBoards(boards)

    import collections
    poses = collections.defaultdict(list)

    for i in range(len(boards)):
        board = boards[i]
        for x in range(len(board)):
            for y in range(len(board[0])):
                # print(board[x][y])
                poses[board[x][y]].append([i, x, y])

    print(poses)
  
    for num in nums[:2]:
        print("NUM:", num)
        if int(num) in poses:
            print("NUM:", num, poses[num])
            for pos in poses[num]:
                print(pos)
                print(checks[pos[0]][pos[1]][pos[2]])
                print(boards[pos[0]][pos[1]][pos[2]])
                checks[pos[0]][pos[1]][pos[2]] = -1
                boards[pos[0]][pos[1]][pos[2]] *= -1 
            # printBoards(checks)
            # printBoards(boards)


    print(len(boards))
            
    print(boards)
    print(board_size)
           


    

    # print(d)
    # return valid

    
        
        




arr = readFile("AoC_Inputs/AoC_2021_d4_input.txt")
print(bingo(arr))
