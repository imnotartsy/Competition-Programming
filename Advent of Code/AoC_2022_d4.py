# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


# * I/O Prepper
def function(arr):
    # * Part 1
    sum = 0
    for line in arr:
        elfs = line.split(",")
        pairs = []
        for e in elfs:
            range = e.split("-")
            pairs.append([int(range[0]), int(range[1])])
        print(line)

        # * Part 1
        # tests if a pair is a subset of another pair
        if pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1]:
            sum += 1
            print("\tA", pairs[0], "contains", pairs[1])

        elif pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]:
            sum += 1
            print("\tB", pairs[1], "contains", pairs[0])

        # * Part 2
        # tests if pairs overlap at all
        elif pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][0]:
            sum += 1
            print("\tC", pairs[0], "overlaps", pairs[1])
        elif pairs[1][0] <= pairs[0][0] and pairs[1][1] >= pairs[0][0]:
            sum += 1
            print("\tD", pairs[1], "overlaps", pairs[0])
        else:
            print("\tE", pairs[0], "does not overlap", pairs[1])

    print(sum)


    # not 548

    # not 40-, 669

    return sum




arr = readFile("AoC_Inputs/AoC_2022_d4_input.txt")
print(function(arr))

