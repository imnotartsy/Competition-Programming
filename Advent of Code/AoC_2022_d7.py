# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

from collections import defaultdict

# * I/O Prepper
def function(arr):
    files = defaultdict(list)
    file_sizes = defaultdict(int)
    # dir = namedtuple("dir", "name children")

    mode = ""
    path = []
    for line in arr:

        # command
        if line[0] == "$":
            mode = line[2:4]
            if mode == "cd":
                if line[5:] == "/":
                    path = ["/"]
                elif line[5:] != "..":
                    path.append(line[5:])
                else:
                    path.pop()
                    
        # output
        elif mode == "ls":
            meta = line.split()

            # inner dirs
            if meta[0] == "dir":
                pass
            else:
                p = ""
                for t in path:
                    p += t + "\\"
                    file_sizes[p] += int(meta[0])
                    
                files[p].append([int(meta[0]), meta[1]])
                

    # * part 1
    p1 = 0
    for f in file_sizes:
        if file_sizes[f] <= 100000:
            p1 += file_sizes[f]

    # * part 2
    space = 70000000
    need = 30000000
    goal = -((space - file_sizes["/\\"]) - need)
    p2 = min([file_sizes[f] for f in file_sizes if file_sizes[f] >= goal])


    # sum = 0
    # pretty print
    for dir in files:
        print(dir, file_sizes[dir])
        for f in files[dir]:
            print("\t", f)

    return p1, p2


arr = readFile("AoC_Inputs/AoC_2022_d7_input.txt")
print(function(arr))