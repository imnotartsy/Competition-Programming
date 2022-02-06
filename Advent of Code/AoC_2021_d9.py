# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


def function1(arr):
    print(arr)
    board = []
    clouds = []
    for line in arr:
        edge = []
        cloud = []
        for num in line:
            edge.append(int(num))
            cloud.append('X')

        board.append(edge)
        clouds.append(cloud)

    for line in board:
        print(line)
        
    risk = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            
            leftright = False
            topbottom = False
            if i == 0:
                if board[i][j] < board[i+1][j]:
                    leftright = True
            elif i == len(board) -1:
                if board[i][j] < board[i-1][j]:
                    leftright = True
            else:
                if board[i][j] < board[i+1][j] and board[i][j] < board[i-1][j]:
                    leftright = True
            
            if j == 0:
                if board[i][j] < board[i][j+1]:
                    topbottom = True
            elif j == len(board[i]) -1:
                if board[i][j] < board[i][j-1]:
                    topbottom = True
            else:
                if board[i][j] < board[i][j+1] and board[i][j] < board[i][j-1]:
                    topbottom = True

            if leftright and topbottom:
                print("*" + str(board[i][j]) + "*", end="")
                risk += board[i][j] + 1

            else:
                print(board[i][j], end="")
            
        print()

    return risk

import queue

def matrixSumBFS(board, clouds, pos):

    q = queue.Queue()
    q.put(pos)

    # print(q)

    summ = 0
    while not q.empty():
        pos = q.get()
        # print(pos)
        if clouds[pos[0]][pos[1]] == 'O':
            clouds[pos[0]][pos[1]] = 'A'
            summ += 1

            if pos[0] == 0:
                q.put([pos[0]+1, pos[1]])
            elif pos[0] == len(board) -1:
                q.put([pos[0]-1, pos[1]])
            else:
                q.put([pos[0]+1, pos[1]])
                q.put([pos[0]-1, pos[1]])

            
            if pos[1] == 0:
                q.put([pos[0], pos[1]+1])
            elif pos[1] == len(board[pos[0]])-1:
                q.put([pos[0], pos[1]-1])
            else:
                q.put([pos[0], pos[1]+1])
                q.put([pos[0], pos[1]-1])

    return summ  

    

def function2(arr):
    board = []
    clouds = []
    for line in arr:
        edge = []
        cloud = []
        for num in line:
            edge.append(int(num))
            if int(num) == 9:
                cloud.append('X')
            else:
                cloud.append('O')

        board.append(edge)
        clouds.append(cloud)

    sizes = [0, 0, 0]
    for i in range(len(board)):
        for j in range(len(board[i])):

            ## For each basin perform sum-sized BFS
            if clouds[i][j] == 'O':
                temprisk = matrixSumBFS(board, clouds, [i, j])

                ## Keep track of top three
                if temprisk > min(sizes):
                    sizes.remove(min(sizes))
                    sizes.append(temprisk)


    print(sizes)
    return sizes[0] * sizes[1] * sizes[2]

            


    print(board)

arr = readFile("AoC_Inputs/AoC_2021_d9_input.txt")
print(function1(arr))
print(function2(arr))