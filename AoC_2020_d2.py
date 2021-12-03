# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words



def validPass(arr):
    validCount = 0
    for line in arr:
        # print(line)
        x = line.split(" ")
        # for word in x:
        bounds = x[0].split("-")
        lower = int(bounds[0])
        upper = int(bounds[1])

        letter = x[1][:-1]
        pw = x[2]

        letterCount = 0
        # walks through each word
        for letterIdx in range(len(pw)):
            if pw[letterIdx] == letter:
                letterCount += 1

        if letterCount >= lower and letterCount <= upper:
            validCount += 1

    return validCount

def validPass2(arr):
    validCount = 0
    for line in arr:
        # print(line)
        x = line.split(" ")
        # for word in x:
        bounds = x[0].split("-")
        lower = int(bounds[0])
        upper = int(bounds[1])

        letter = x[1][:-1]
        pw = x[2]

        print(pw, "\t", pw[lower-1], pw[upper-1], "\t", letter, end="")
        if pw[lower-1] == letter and not(pw[upper-1] == letter):
            validCount += 1
            print("\t MATCH", end="")
        elif not(pw[lower-1] == letter) and pw[upper-1] == letter:
            validCount += 1
            print("\t MATCH", end="")
        print()

    return validCount

arr = readFile("AoC_2020_d2_input.txt")
# print(validPass(arr))
print(validPass2(arr))