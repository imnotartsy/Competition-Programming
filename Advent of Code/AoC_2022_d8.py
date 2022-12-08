# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


# * I/O Prepper
def function(arr):
    trees = []
    for line in arr:
        trees.append([int(thing) for thing in line])

    print(trees)
    
    edges = 0
    visable = 0
    views = []
    for i in range(len(trees)): # row
        for j in range(len(trees[0])): # col

            # * part 1
            # edges
            if i == 0 or i == len(trees)-1 or j == 0 or j == len(trees[0])-1:
                edges += 1
            else:
                print(trees[i][j], ": (" + str(i), ",", j, end="): ")
                seen = [True, True, True, True]
                # left
                for k in range(0, j):
                    if trees[i][k] >= trees[i][j]:
                        seen[0] = False       
                        break         
                # right
                for k in range(j+1, len(trees[0])):
                    if trees[i][k] >= trees[i][j]:
                        seen[1] = False
                        break
                # top
                for k in range(0, i):
                    if trees[k][j] >= trees[i][j]:
                        seen[2] = False
                        break
                # bottom
                for k in range(i+1, len(trees)):
                    if trees[k][j] >= trees[i][j]:
                        seen[3] = False
                        break

                if True in seen:
                    # print(seen)
                    print("SEEN FROM:", end=" ")
                    if seen[0]:
                        print("LEFT", end=" ")
                    if seen[1]:
                        print("RIGHT", end=" ")
                    if seen[2]:
                        print("TOP", end=" ")
                    if seen[3]:
                        print("BOTTOM", end=" ")
                    print()
                    visable += 1
                else:
                    print( "Not seen")

            # * part 2
            seen = [0, 0, 0, 0]
            view = 1
            # edges
            if i == 0 or i == len(trees)-1 or j == 0 or j == len(trees[0])-1:
                pass
            else:
                # print(trees[i][j], ": (" + str(i), ",", j, end="): ")

                # left
                for k in range(0, j):
                    seen[0] += 1
                    if trees[i][j-k-1] >= trees[i][j]:    
                        break
                # right
                for k in range(j+1, len(trees[0])):
                    seen[1] += 1
                    if trees[i][k] >= trees[i][j]:
                        break 
                # top
                for k in range(0, i):
                    seen[2] += 1
                    if trees[i-k-1][j] >= trees[i][j]:
                        break
                # bottom
                for k in range(i+1, len(trees)):
                    seen[3] += 1
                    if trees[k][j] >= trees[i][j]:
                        break
                # products view
                for d in seen:
                    view *= d # only trees on the edge are zero and are not considered
                views.append(view)
                print("\t\t", seen, view)

    p1 = edges + visable
    p2 = max(views)


    return p1, p2

arr = readFile("AoC_Inputs/AoC_2022_d8_input.txt")
print(function(arr))