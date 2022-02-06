# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


def function(arr):
    print(arr)

arr = readFile("AoC_Inputs/AoC_2021_dX_input.txt")
print(function(arr))