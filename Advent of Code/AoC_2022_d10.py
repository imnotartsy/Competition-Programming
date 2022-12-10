# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


def prettyPrint(CRT):
    for line in CRT:
        print("".join(line))
    print()

# * I/O Prepper
def function(arr):
    x = 1

    commands = []
    cycle = 1
    outputs = [0 for _ in range(len(arr) * 2)]

    width = 40
    height = 6
    CRT = [["." for _ in range(width + 1)] for _ in range(height + 1)]


    for line in arr:
        if line == "noop":
            commands.append(0)
            cycle += 1
        else:
            commands.append(int(line.split()[1]))
            cycle += 1
            outputs[cycle] = x
            if int((cycle-1)%width) >= x - 1 and int((cycle-1)%width) <= x + 1:
                CRT[int((cycle-1)/width)][int((cycle-1)%width)] = "#"
            
            cycle += 1
            x += int(line.split()[1])
        outputs[cycle] = x

        if int((cycle-1)%width) >= x - 1 and int((cycle-1)%width) <= x + 1:
                CRT[int((cycle-1)/width)][int((cycle-1)%width)] = "#"

    
    signal = 0
    for i in range(cycle):
        if (i - 20) % 40 == 0:
            signal += i*outputs[i]
    print(signal)

    prettyPrint(CRT)

    p1 = signal
    p2 = CRT

    

    return p1, p2

arr = readFile("AoC_Inputs/AoC_2022_d10_input.txt")
print(function(arr))