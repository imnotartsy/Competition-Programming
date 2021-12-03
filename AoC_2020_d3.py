# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


def countTrees(arr):
    board = []
    for line in arr:
        x = []
        for char in line:
            x.append(char)

        board.append(x)

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [2, 1]]
    totalTrees = 1

    for slope in slopes:
        x = 0
        y = 0
        trees = 0
        while y < len(board):
            # print(board[y][x])
            if board[y%len(board)][x%len(board[0])] == '#':
                trees += 1
            x += slope[0]
            y += slope[1]
        totalTrees *= trees


    return totalTrees


arr = readFile("AoC_2020_d3_input.txt")
print(countTrees(arr))

# 5872458240