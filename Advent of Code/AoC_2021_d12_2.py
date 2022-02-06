# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import collections

# # I'm sorry idk how else to do this
class globals:
    paths = []
    visitedL = []

# Part 1
def depthFirst1(graph, currVertex, path):
    path.append(currVertex)

    if currVertex == "end":
        globals.visitedL.append(path)

    for v in graph[currVertex]:
        if v not in path or v == v.upper():
            depthFirst1(graph, v, path.copy())

# Part 2
def depthFirst2(graph, currVertex, visited, path):            
    path.append(currVertex)
    
    if currVertex == currVertex.lower():
        visited[currVertex] += 1

    if currVertex == "end":
        globals.visitedL.append(path)

    else:
        for v in graph[currVertex]:
            if v != "start" \
            and (v == v.upper() \
            or (v == v.lower() and ( ((max(visited.values()) < 2 and path.count(v) <= 1)) \
                                  or ((max(visited.values()) == 2 and path.count(v) < 1)) \
               ))):
                depthFirst2(graph, v, visited.copy(), path.copy())


def function(arr):
    edges = collections.defaultdict(list)
    visited = collections.defaultdict(int)
    print(arr)

    # Initiate the edge list and visisted list
    for line in arr:
        points = line.split("-")
        edges[points[0]].append(points[1])
        edges[points[1]].append(points[0])

    
    # Prints edge list
    # print(json.dumps(edges, indent=1))
    print(edges.keys())

    # Part 1
    # depthFirst1(edges, "start", [])

    # Part 2
    depthFirst2(edges, "start", visited, [])

    # print(globals.visitedL)

    # print("Paths:")
    # for p in globals.visitedL:
    #     print(p)


    # print(len(globals.visitedL))

    return len(globals.visitedL)

arr = readFile("AoC_Inputs/AoC_2021_d12_input.txt")
print(function(arr))