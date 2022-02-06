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

def printOctos(octos):
    for i in range(len(octos)):
        for j in range(len(octos[i])):
            if octos[i][j] == 0:
                print(bcolors.FAIL + "0" + bcolors.ENDC, end=" ")
            else:
                print(octos[i][j], end=" ")
        print()
    print()



import queue
def octoFlash(octos, checked, pos):

    q = queue.Queue()
    q.put(pos)

    # print(q)

    while not q.empty():
        pos = q.get()
        # print(pos, end=" ")
        if octos[pos[0]][pos[1]] == 0 and checked[pos[0]][pos[1]] == 1:
            # print("FLASH!")
            checked[pos[0]][pos[1]] = 0
            # octos[pos[0]][pos[1]] = (octos[pos[0]][pos[1]] + 1) %10

            if pos[0] == 0:
                q.put([pos[0]+1, pos[1]])
                octos[pos[0]+1][pos[1]] = (octos[pos[0]+1][pos[1]] + 1)
            elif pos[0] == len(octos) -1:
                q.put([pos[0]-1, pos[1]])
                octos[pos[0]-1][pos[1]] = (octos[pos[0]-1][pos[1]] + 1)
            else:
                q.put([pos[0]+1, pos[1]])
                octos[pos[0]+1][pos[1]] = (octos[pos[0]+1][pos[1]] + 1)
                q.put([pos[0]-1, pos[1]])
                octos[pos[0]-1][pos[1]] = (octos[pos[0]-1][pos[1]] + 1)

            
            if pos[1] == 0:
                q.put([pos[0], pos[1]+1])
                octos[pos[0]][pos[1]+1] = (octos[pos[0]][pos[1]+1] + 1)
            elif pos[1] == len(octos[pos[0]])-1:
                q.put([pos[0], pos[1]-1])
                octos[pos[0]][pos[1]-1] = (octos[pos[0]][pos[1]-1] + 1)
            else:
                q.put([pos[0], pos[1]+1])
                octos[pos[0]][pos[1]+1] = (octos[pos[0]][pos[1]+1] + 1)
                q.put([pos[0], pos[1]-1])
                octos[pos[0]][pos[1]-1] = (octos[pos[0]][pos[1]-1] + 1)


            ## need to add diagonals
            if pos[0] != 0:
                if pos[1] != 0:
                    q.put([pos[0]-1, pos[1]-1])
                    octos[pos[0]-1][pos[1]-1] = (octos[pos[0]-1][pos[1]-1] + 1)
                if pos[1] != len(octos[pos[0]])-1:
                    q.put([pos[0]-1, pos[1]+1])
                    octos[pos[0]-1][pos[1]+1] = (octos[pos[0]-1][pos[1]+1] + 1)
            if pos[0] != len(octos) -1:
                if pos[1] != 0:
                    q.put([pos[0]+1, pos[1]-1])
                    octos[pos[0]+1][pos[1]-1] = (octos[pos[0]+1][pos[1]-1] + 1)
                if pos[1] != len(octos[pos[0]])-1:
                    q.put([pos[0]+1, pos[1]+1])
                    octos[pos[0]+1][pos[1]+1] = (octos[pos[0]+1][pos[1]+1] + 1)
        # else:
        #     print()

    # printOctos(checked)
    # return summ  

def function(arr):
    # print(arr)
    octos = []
    checked = []
    for line in arr:
        octo = []
        check = []
        for num in line:
            octo.append(int(num))
            check.append(1)
        octos.append(octo)
        checked.append(check)
    # print(octos)
    # print(checked)

    # step
    for d in range(3):
        print("STEP", d)
        printOctos(octos)  
        for i in range(len(octos)):
                for j in range(len(octos[i])):
                    octos[i][j] = octos[i][j] + 1

        for i in range(len(octos)):
            for j in range(len(octos[i])):

                    # may need to bfs After incrementing
                    if octos[i][j] > 9:
                        octoFlash(octos, checked, [i, j])                        

        for i in range(len(octos)):
            for j in range(len(octos[i])):

                    # may need to bfs After incrementing
                    if octos[i][j] > 9:
                        octos[i][j] = 0


        printOctos(checked)
        
        # printOctos(octos)



arr = readFile("AoC_Inputs/AoC_2021_d11_input.txt")
print(function(arr))