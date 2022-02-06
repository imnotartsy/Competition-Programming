# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import collections
import math



def function(arr):
    inputraw_split = arr[0].split()
    x_raw = inputraw_split[2][2:].split(".")
    y_raw = inputraw_split[3][2:].split(".")

    print(x_raw, y_raw)

    txMin = int(x_raw[0])
    txMax = int(x_raw[2][:-1])
    tyMin = int(y_raw[0])
    tyMax = int(y_raw[2])

    print(txMin, txMax)
    print(tyMin, tyMax)

    # To find lowest possible dxMin, first minimize distance and assume
    # dx is zero in the target; adding all the digits from 0 to min speed = txMin
    # n*(n+1)/= txMin
    dxMin = math.floor((pow(8*txMin + 1, 1/2) - 1)/2)
    # print(dxMin)

    accurate = []
    maxY = 0
    for dy in range(tyMin, -tyMin+1):
        # print(str(dy) + ": ", end="")
        for dx in range(dxMin, txMax+1):
            # print(str(dx) + ", ", end="")

            ## Unnecessary variables
            dxx = dx
            dyy = dy

            x = 0
            y = 0
            temp_maxY = 0

            while x <= txMax and y >= tyMin:
                x += dxx
                y += dyy

                if y > temp_maxY:
                    temp_maxY = y

                if x >= txMin and x <= txMax and y >= tyMin and y <= tyMax:
                    if temp_maxY > maxY:
                        maxY = temp_maxY
                    accurate.append([dx, dy])
                    break

                dxx = dxx - 1 if dxx != 0 else 0
                dyy -= 1
        # print()
            
            
    # P1
    print(maxY)

    import pyfade

    # P2
    print(len(accurate))
    i = 0
    for i in range(60):
     
        print(pyfade.Fade.Horizontal(pyfade.Colors.green_to_cyan, f"     [!] Waiting for SMS code... {i + 1}/60"))
    return len(accurate)
    

arr = readFile("AoC_Inputs/AoC_2021_d17_input.txt")
print(function(arr))
