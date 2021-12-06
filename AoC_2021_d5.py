# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

def makeMap(x):
    board = []
    for i in range(x):
        row = []
        for j in range(x):
            row.append(0)
        board.append(row)
    return board

def printBoard(arr):
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if arr[j][i] == 0:
                print(".", end=' ')
            else:
                print(arr[j][i], end=' ')
        print()


def overlapClouds(arr):
    segments = []
    for line in arr:
        coords = line.split()
        start = [int(x) for x in coords[0].split(',')]
        stop = [int(x) for x in coords[2].split(',')]
        segments.append([start,stop])

    for segment in segments:
        print(segment)
    # print(clouds)        

    # Get Board bounds (flatten and find max)
    size = max([i for sub in [j for sub in segments for j in sub] for i in sub])

    clouds = makeMap(size + 1)
    printBoard(clouds)

    for segment in segments:
        start = segment[0]
        stop  = segment[1]

        # directions
        x_inc = 1 if stop[0] - start[0] > 0 else -1 if stop[0] - start[0] < 0 else 0
        y_inc = 1 if stop[1] - start[1] > 0 else -1 if stop[1] - start[1] < 0 else 0
        
        x = start[0]
        y = start[1]

        # loop iterations; invarient: will be straight ot +/- 45'
        dist = abs(stop[0] - start[0]) if abs(stop[0] - start[0]) > abs(stop[1] - start[1]) else abs(stop[1] - start[1])
        print("POINT:", [start[0], start[1]], "TO", [stop[0], stop[1]])#, "; Dist", dist)


        ## P1
        # if x_inc == 0 or y_inc == 0:
        #     print("H or V")
        #     clouds[x][y] += 1

        # Starting Point
        clouds[x][y] += 1
        for i in range(dist):
            x += x_inc
            y += y_inc
            # print([x, y])

            ## P1
            # if x_inc == 0 or y_inc == 0:
            #     clouds[x][y] += 1
            clouds[x][y] += 1

        # printBoard(clouds)


    overlap = 0
    for row in clouds:
        for cloud in row:
            if cloud > 1:
                overlap += 1

    return overlap

        


    


arr = readFile("AoC_Inputs/AoC_2021_d5_input.txt")
print(overlapClouds(arr))