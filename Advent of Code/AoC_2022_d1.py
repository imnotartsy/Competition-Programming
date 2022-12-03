# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


# * I/O Prepper
def function(arr):
    sums = []
    sum = 0
    for line in arr:
        if line == "":
            sums.append(sum)
            sum = 0
        else:
            sum += int(line)
    sums.append(sum)

    print(sums)

    # First star
    # return max(sums)

    # Sum the top three
    # maxx = max(sums)
    # sums.remove(max(sums))
    # maxx += max(sums)
    # sums.remove(max(sums))
    # maxx += max(sums)
    # sums.remove(max(sums))

    # Second star
    # return maxx

    # print(sorted(sums, reverse=True)[:3])
    yes = sorted(sums, reverse=True)[:3]
    print(yes[0] + yes[1] + yes[2])




arr = readFile("AoC_Inputs/AoC_2022_d1_input.txt")
print(function(arr))

