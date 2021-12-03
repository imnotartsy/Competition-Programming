# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
from os import read

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

def distance(arr):
    x = 0
    y = 0
    for line in arr:
        dir, dist = line.split()
        dist = int(dist)

        if dir == "forward":
            x += dist
        elif dir == "up":
            y += dist
        elif dir == "down":
            y -= dist
    
    print("X:", x, "Y:", y)

    return abs(x * y)

def distance2(arr):
    x = 0
    y = 0
    aim = 0
    for line in arr:
        dir, dist = line.split()
        dist = int(dist)

        if dir == "forward":
            # depth by your aim multiplied by X.
            y += aim * dist
            x += dist   
        elif dir == "up":
            aim -= dist
        elif dir == "down":
            aim += dist
    
    print("X:", x, "Y:", y)

    return x * y

arr = readFile("AoC_2021_d2_input.txt")
print(distance(arr))
print(distance2(arr))

# 00:06:50; first tries