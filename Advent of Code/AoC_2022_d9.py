# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

def prettyPrint(head, tail, places):
    if places != []:
        x = max(max(places, key=lambda tup: tup[0])[0], head[0], tail[0])
        y = max(max(places, key=lambda tup: tup[1])[1], head[1], tail[1])
    else:
        x = max(head[0], tail[0])
        y = max(head[1], tail[1])
    for i in range(x + 1):
        for j in range(y + 1):
            if [i, j] == head:
                print("H", end="")
            elif [i, j] == tail:
                print("T", end="")
            elif tuple([i,j]) in places:
                print("_", end="")
            else:
                print(".", end="")
        print()
    print()

def prettyPrint2(knots, places):
    if places != []:
        x = max(max(places, key=lambda tup: tup[0])[0], max(knots, key=lambda tup: tup[0])[0])
        y = max(max(places, key=lambda tup: tup[1])[1], max(knots, key=lambda tup: tup[1])[1])
    else:
        x = max(knots, key=lambda tup: tup[0])[0]
        y = max(knots, key=lambda tup: tup[1])[1]
    for i in range(x + 1):
        for j in range(y + 1):
            if [i, j] in knots:
                print(knots.index([i, j]), end="")
            elif tuple([i,j]) in places:
                print("_", end="")
            else:
                print(".", end="")
        print()
    print()

def followHead(head, tail):
    if abs(head[0]-tail[0]) + abs(head[1]-tail[1]) > 2:
        if abs(head[0]-tail[0]) == 2:
            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1

            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1

        elif abs(head[1]-tail[1]) == 2:
            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1

            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1

    elif abs(head[0]-tail[0]) > 1:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1

    elif abs(head[1]-tail[1]) > 1:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    # else:
    #     print("NOTHING TO FOLLOW")

    return head, tail


# * I/O Prepper
def function(arr):
    p1 = 0
    p2 = 0

    places = []
    head = [0,0]
    tail = [0,0]

    num_knots = 10
    knots =[[0,0] for _ in range(num_knots)]
    places2 = []

    # print("INIT:")
    for line in arr:
        # pretty print
        # prettyPrint(head, tail, places)
    

        dir, dis = line.split()
        print("MOVE:", dir, dis)
        if dir == "R":
            for _ in range(int(dis)):
                head[1] += 1
                head, tail = followHead(head, tail)
                places.append(tuple(tail))

                knots[0][1] += 1
                for i in range(1, num_knots):
                    followHead(knots[i-1], knots[i])
                places2.append(tuple(knots[9]))
                # prettyPrint2(knots, places2)

                # prettyPrint(head, tail, places)
        elif dir == "L":
            for _ in range(int(dis)):
                head[1] -= 1
                head, tail = followHead(head, tail)
                places.append(tuple(tail))

                knots[0][1] -= 1
                for i in range(1, num_knots):
                    followHead(knots[i-1], knots[i])
                places2.append(tuple(knots[9]))
                # prettyPrint2(knots, places2)

                # prettyPrint(head, tail, places)

        elif dir == "U":
            for _ in range(int(dis)):
                head[0] += 1
                head, tail = followHead(head, tail)
                places.append(tuple(tail))
                
                knots[0][0] += 1
                for i in range(1, num_knots):
                    followHead(knots[i-1], knots[i])
                places2.append(tuple(knots[9]))
                # prettyPrint2(knots, places2)

                # prettyPrint(head, tail, places)
            
        elif dir == "D":
            for _ in range(int(dis)):
                head[0] -= 1
                head, tail = followHead(head, tail)
                places.append(tuple(tail))

                knots[0][0] -= 1
                for i in range(1, num_knots):
                    followHead(knots[i-1], knots[i])
                places2.append(tuple(knots[9]))
                # prettyPrint2(knots, places2)

                # prettyPrint(head, tail, places)



        # move head, move tail
        places.append(tuple(tail))

    # print("FINAL:")
    # head = [0,0]
    # tail = [0,0]
    # prettyPrint(head, tail, places)
    # print(places)
    # p1 = len(set(places))

    print("FINAL:")
    knots =[[0,0] for _ in range(num_knots)]
    prettyPrint2(knots, places2)
    print(places2)
    p2 = len(set(places2))

    return p1, p2

arr = readFile("AoC_Inputs/AoC_2022_d9_input.txt")
print(function(arr))