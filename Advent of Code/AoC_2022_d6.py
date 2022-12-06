# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

from collections import deque

# * I/O Prepper
def function(arr):

    for i in range(len(arr[0])):

        # * part 1 & 2
        interval = 14 # 4 for part 1; 14 for part 2
        match = False

        # if past buffer
        if i >= interval-1:
            print("Testing:", arr[0][i], arr[0][i-(interval-1):i], i-(interval-1), i)

            # for each number in the interval
            for k in range(0, interval-1):
                # check if equal to another number in the interval
                for j in range(1, interval-k):
                    # print("\t", i-k, i+k-j, "\t", arr[0][i-k], arr[0][i-k-j])

                    # if match; invalid interval; break
                    if arr[0][i-k] == arr[0][i-k-j]:
                        # print("match")
                        # ! could short circut here; i-k is the new i (scrap entire interval)
                        match = True
                        break
                if match:
                    break

            if not match:
                print("\tVALID Interval", i, arr[0][i], arr[0][i-(interval-1):i])
                return i + 1

arr = readFile("AoC_Inputs/AoC_2022_d6_input.txt")
print(function(arr))