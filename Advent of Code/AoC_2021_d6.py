# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

# Linear 
def function(arr):
    days = 18

    fishh = [int(x) for x in arr[0].split(',')]
    # print(fishh)

    for day in range(days):
        # print(day, len(fishh), fishh)
        for i in range(len(fishh)):
            if fishh[i] == 0:
                fishh[i] = 6
                fishh.append(8)
            else:
                fishh[i] -= 1

    # print(days, fishh)
    # print(day, len(fishh))
    return len(fishh)

def function2(arr):
    days = 256

    fishh = [int(x) for x in arr[0].split(',')]

    ## Array for holding counts; index == age
    fishhh = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in fishh:
        fishhh[fish] += 1

    # print(fishhh)
    fish_count = 0

    for day in range(days):
        # For intermediate fishhh count total
        # fish_count = 0
        # for fish in fishhh:
        #     fish_count += fish
        # print(day, fish_count)

        ## This could be done in a prettier way; but in essence it's subtracting the timers
        birthing = fishhh[0]
        fishhh[0] = fishhh[1]
        fishhh[1] = fishhh[2]
        fishhh[2] = fishhh[3]
        fishhh[3] = fishhh[4]
        fishhh[4] = fishhh[5]
        fishhh[5] = fishhh[6]
        fishhh[6] = fishhh[7] + birthing
        fishhh[7] = fishhh[8] 
        fishhh[8] = birthing
        print(fishhh)

    print(fishhh)
    fish_count = 0
    for fish in fishhh:
        fish_count += fish
    return fish_count

arr = readFile("AoC_Inputs/AoC_2021_d6_input.txt")
print(function(arr))
print(function2(arr))