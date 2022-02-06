# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

brackets = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

points2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

import statistics

def function(arr):
    summ = 0
    lineSumms = []
    for line in arr:

        ## ** P1 **
        q = []

        ## ** P2 **
        bad = False
        lineSumm = 0
        for char in line:
            if char in brackets.keys():
                q.append(brackets[char])
            elif char != q[-1]:
                summ += points[char]
                bad = True
                break
            elif char == q[-1]:
                q.pop()

        if not bad and len(q) > 0:
            q.reverse()
            for i in range(len(q)):
                lineSumm = lineSumm * 5 + points2[q[i]]

            # print(lineSumm)
            lineSumms.append(lineSumm)


    ## ** P1 **
    # return summ
    print(summ)
    ## ** P2 **
    return statistics.median(lineSumms)

arr = readFile("AoC_Inputs/AoC_2021_d10_input.txt")
print(function(arr))