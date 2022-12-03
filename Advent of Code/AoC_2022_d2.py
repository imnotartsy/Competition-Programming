# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


opp = {
    "A": 0, # rock
    "B": 1, # paper
    "C": 2, # scissors
}

your = {
    "X": 0, # rock
    "Y": 1, # paper
    "Z": 2, # scissors
}

out = {
    "X": 1, # lose
    "Y": 2, # draw
    "Z": 3, # win
}

p = {
    0: "rock",
    1: "paper",
    2: "scissors"
}

# * I/O Prepper
def function(arr):
    you = 0
    ## Part 1
    # for line in arr:
    #     move = line.split()
    #     print("Input:", move[0], ":",move[1],  "/", p[opp[move[0]]], ":", p[your[move[1]]])

    #     you += your[move[1]] + 1
    #     if (opp[move[0]] - your[move[1]]) % 3 == 1: # lose
    #         print("\tlose")
    #     elif (opp[move[0]] - your[move[1]]) % 3 == 2: # win
    #         you += 6
    #         print("\twin")
    #     else:
    #         you += 3
    #         print("\ttie")

    #     print("\tscore:", you)

 ## Part 2
    for line in arr:
        move = line.split()
        print("Input:", move[0], ":",move[1], end=" --> ")

        y = 0
        if out[move[1]] == 1: # lose
            print("lose")
            y = (opp[move[0]] - 1) % 3
        elif out[move[1]] == 3: # win
            print("win")
            y = (opp[move[0]] + 1) % 3
            you += 6
        else:
            print("tie")
            y = opp[move[0]]
            you += 3

        you += y + 1   

        print("\t", opp[move[0]], ":", y , "/", p[opp[move[0]]], ":", p[y])
        # print("score:", you)

    return you




arr = readFile("AoC_Inputs/AoC_2022_d2_input.txt")
print(function(arr))

