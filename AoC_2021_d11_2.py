# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' # yellow
    FAIL = '\033[91m'    # red
    ENDC = '\033[0m'     # normal
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

## Globals are to keep track of flash count in a single round
##  or if all octos flash
# I'm so sorry
class globals:
    flash = 0
    singleflash = 0


## Helper function to print colored octos!
def printOctos(octos, tabs=0):
    tab = '\t'*tabs
    for i in range(len(octos)):
        print(tab, end='')
        for j in range(len(octos[i])):
            if octos[i][j] == 0:
                print(bcolors.FAIL + "0" + bcolors.ENDC, end="   ")
            elif octos[i][j] >= 10:
                print(bcolors.WARNING + str(octos[i][j]) + bcolors.ENDC, end="  ")
            else:
                print(octos[i][j], end="   ")

        print()
    print()


## Recursive BFS; if position exists, increment, check for flash
## If there's a flash, recurse
def octoFlash(octos, checked, pos):
    checked[pos[0]][pos[1]] = 1
    globals.flash += 1
    globals.singleflash += 1

    if pos[0] > 0:
        
        ## Left
        octos[pos[0]-1][pos[1]] += 1
        if octos[pos[0]-1][pos[1]] > 9 and checked[pos[0]-1][pos[1]] == 0:
            octoFlash(octos, checked, [pos[0]-1, pos[1]])

        ## Upper Left
        if pos[1] > 0:
            octos[pos[0]-1][pos[1]-1] += 1
            if octos[pos[0]-1][pos[1]-1] > 9 and checked[pos[0]-1][pos[1]-1] == 0:
                octoFlash(octos, checked, [pos[0]-1, pos[1]-1])

        ## Lower Left
        if pos[1] < len(octos[0]) - 1:
            octos[pos[0]-1][pos[1]+1] += 1
            if octos[pos[0]-1][pos[1]+1] > 9 and checked[pos[0]-1][pos[1]+1] == 0:
                octoFlash(octos, checked, [pos[0]-1, pos[1]+1])

    if pos[0] < len(octos)-1:

        ## Right
        octos[pos[0]+1][pos[1]] += 1
        if octos[pos[0]+1][pos[1]] > 9 and checked[pos[0]+1][pos[1]] == 0:
            octoFlash(octos, checked, [pos[0]+1, pos[1]])
    
        ## Upper Right
        if pos[1] > 0:
            octos[pos[0]+1][pos[1]-1] += 1
            if octos[pos[0]+1][pos[1]-1] > 9 and checked[pos[0]+1][pos[1]-1] == 0:
                octoFlash(octos, checked, [pos[0]+1, pos[1]-1])

        ## Lower Right
        if pos[1] < len(octos[0]) - 1:
            octos[pos[0]+1][pos[1]+1] += 1
            if octos[pos[0]+1][pos[1]+1] > 9 and checked[pos[0]+1][pos[1]+1] == 0:
                octoFlash(octos, checked, [pos[0]+1, pos[1]+1])

    ## Top
    if pos[1] > 0:
        octos[pos[0]][pos[1]-1] += 1
        if octos[pos[0]][pos[1]-1] > 9 and checked[pos[0]][pos[1]-1] == 0:
            octoFlash(octos, checked, [pos[0], pos[1]-1])

    ## Bottom
    if pos[1] < len(octos[0]) - 1:
        octos[pos[0]][pos[1]+1] += 1
        if octos[pos[0]][pos[1]+1] > 9 and checked[pos[0]][pos[1]+1] == 0:
            octoFlash(octos, checked, [pos[0], pos[1]+1])

       

   
def function(arr):
    octos = []
    checked = []
    for line in arr:
        octo = []
        check = []
        for num in line:
            octo.append(int(num))
            check.append(0)
        octos.append(octo)
        checked.append(check)


    print("Before any steps", 0)
    printOctos(octos)  

    # step
    for d in range(500):
        # Reset single round flash count
        globals.singleflash = 0

        # Iterate (+ Reset) all
        for i in range(len(octos)):
                for j in range(len(octos[i])):
                    # Iterate all
                    octos[i][j] = octos[i][j] + 1

                    # Reset check
                    checked[i][j] = 0

        # Check for flashing
        for i in range(len(octos)):
            for j in range(len(octos[i])):

                    # If not flashed already and flashable; BFS flash
                    if octos[i][j] > 9 and checked[i][j] == 0:
                        octoFlash(octos, checked, [i, j])                        

        # Reset energy levels
        for i in range(len(octos)):
            for j in range(len(octos[i])):
                    if octos[i][j] > 9:
                        octos[i][j] = 0

        print(globals.flash)
        print(globals.singleflash)
        
        print("END OF STEP", d+1)
        printOctos(octos)

        ## Part 2
        if globals.singleflash == 100:
            print("FLASH")
            break

    return globals.flash


arr = readFile("AoC_Inputs/AoC_2021_d11_input.txt")
print(function(arr))