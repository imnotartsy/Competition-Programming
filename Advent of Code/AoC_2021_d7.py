# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


def function(arr):
    crabs = [int(x) for x in arr[0].split(',')]

    maxc = max(crabs)
    minc = min(crabs)

    differences1 = []
    differences2 = []
        
    for i in range(minc, maxc+1):
        difference1 = 0
        difference2 = 0

        for crab in crabs:
            diff = abs(crab - i)
            difference1 += diff
            difference2 += diff*(diff+1)/2

        differences1.append(difference1)
        differences2.append(difference2)

    return min(differences1), min(differences2)

arr = readFile("AoC_Inputs/AoC_2021_d7_input.txt")
print(function(arr))