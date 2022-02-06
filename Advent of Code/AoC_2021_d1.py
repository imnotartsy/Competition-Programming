# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

def increaseCount(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            count += 1
    return(count)

# def slidingWindow(arr):
#     count = 0
#     for i in range(3, len(arr)):
#         print(arr[i-1], arr[i-2], arr[i-3], "\t", int(arr[i-1]) + int(arr[i-2]) + int(arr[i-3]), "\t compared to\t", arr[i], arr[i-1], arr[i-2], "\t", int(arr[i]) + int(arr[i-1]) + int(arr[i-2]))
        
#         if int(arr[i]) + int(arr[i-1]) + int(arr[i-2]) > int(arr[i-1]) + int(arr[i-2]) + int(arr[i-3]):
#             count += 1
#             print("increase!")
#     return(count)

def slidingWindow(arr):
    count = 0

    leftSum = int(arr[0]) + int(arr[1]) + int(arr[2])
    rightSum = int(arr[1]) + int(arr[2]) + int(arr[3])

    for i in range(0, len(arr)-4):    
        if rightSum > leftSum:
            count += 1

        leftSum = leftSum - int(arr[i]) + int(arr[i+3])
        rightSum = rightSum - int(arr[i+1]) + int(arr[i+4])


    return(count)

# arr = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263
# ]

arr = readFile("AoC_Inputs/AoC_2021_d1_input2.txt")

print(slidingWindow(arr))
print(increaseCount(arr))