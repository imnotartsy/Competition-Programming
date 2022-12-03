# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

letters = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

# * I/O Prepper
def function(arr):
    # * Part 1
    sum = 0
    for line in arr:
        p1 = line[:int(len(line)/2)]
        p2 = line[int(len(line)/2):]

        # find letter in p1 and p2
        o = ''.join(set(p1).intersection(p2))
        sum += letters[o]
    return sum

    # * Part 2
    sum = 0
    for i in range(0, len(arr), 3):
        p1 = arr[i]
        p2 = arr[i+1]
        p3 = arr[i+2]

        # find letter in p1 and p2 and p3
        o = ''.join((set(p1).intersection(p2)).intersection(p3))
        sum += letters[o]
    return sum





arr = readFile("AoC_Inputs/AoC_2022_d3_input.txt")
print(function(arr))

