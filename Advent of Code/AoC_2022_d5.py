# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

from collections import deque

# * I/O Prepper
def function(arr):
    # * Part 1
    # sum = 0
    
    spots = [deque() for _ in range(int((len(arr[0])+1)/4))]
    print("Spots:", len(spots))

    input = True
    for line in arr:
        # Processes input
        if input:
            for i in range(len(line)):
                if line[i].isupper(): 
                    spots[int((i-1)/4)].appendleft(line[i])
                    # left is bottom of the stack
        
        # Processes move cmds
        if not input and line!= "":
            cmd =line.split()
            # print(cmd[1], cmd[3], cmd[5])

            # * Part 1
            # for i in range(int(cmd[1])):
            #     item = spots[int(cmd[3])-1].pop()
            #     spots[int(cmd[5])-1].append(item)

            # * Part 2
            items = []
            for i in range(int(cmd[1])):
                items.append(spots[int(cmd[3])-1].pop())
            for i in range(int(cmd[1])):
                spots[int(cmd[5])-1].append(items[len(items)-i-1])

        # Finds end of input
        if input and any(char.isdigit() for char in line):
            input = False

    # * Pretty Print (added after)
    # print("Final arrangement:")
    # for spot in spots:
    #     print("".join(spot))

    # Collects output
    ret = ""
    for spot in spots:
        ret+= spot.pop()

    return ret

    # 25 minutes; 2/2




arr = readFile("AoC_Inputs/AoC_2022_d5_input.txt")
print(function(arr))

