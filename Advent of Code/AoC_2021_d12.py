# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import collections
import json

# I'm sorry idk how else to do this
class globals:
    paths = []

def getPaths(vertex, edges, visited, path):
    visited[vertex] = True
    path.append(vertex)
    # print(path)

    if vertex == "end":
        print("path", path)#, "AA")
        globals.paths.append(path)
        print(globals.paths)
    else:
        for v in edges.keys():
            if v in edges[vertex] and (v == v.upper() or visited[v] == False):
                    getPaths(v, edges, visited, path)

    path.pop()
    visited[vertex] = False 


def function(arr):
    edges = collections.defaultdict(list)
    visited = collections.defaultdict(bool)
    print(arr)
    for line in arr:
        points = line.split("-")
        edges[points[0]].append(points[1])
        edges[points[1]].append(points[0])

        visited[points[0]] = False
        visited[points[1]] = False
    
    # print(json.dumps(edges, indent=1))
    # print(edges.keys())

    path = []
    getPaths("start", edges, visited, path)
    print(len(globals.paths))
    print("AA", path)
    # print(paths)
    for p in globals.paths:
        print(p)

arr = readFile("AoC_Inputs/AoC_2021_d12_input.txt")
print(function(arr))