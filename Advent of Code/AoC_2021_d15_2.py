# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import sys

def printSolution(graph, dist):
        print("Vertex tDistance from Source")
        for node in range(len(graph)):
            print(node, "t", dist[node])
 
# A utility function to find the vertex with
# minimum distance value, from the set of vertices
# not yet included in shortest path tree
def minDistance(graph, dist):
    V = len(graph)

    # Initialize minimum distance for next node
    min = sys.maxsize

    # Search not nearest vertex not in the
    # shortest path tree
    for v in range(V):
        if dist[v] < min:# and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

# Function that implements Dijkstra's single source
# shortest path algorithm for a graph represented
# using adjacency matrix representation
def dijkstra(graph):#, src):
    V = len(graph)

    dist = [sys.maxsize] * V
    # dist[src] = 0
    sptSet = [False] * V

    for cout in range(V):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minDistance(dist, sptSet)

        # Put the minimum distance vertex in the
        # shortest path tree
        sptSet[u] = True

        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
        for v in range(V):
            if graph[u][v] > 0 and \
                sptSet[v] == False and \
                dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    printSolution(graph, dist)

def function(arr):
    # print(arr)
    cost = []
    for line in arr:
        c = []
        for char in line:
            c.append(int(char))
        cost.append(c)
    
    for line in cost:
        print(line)


    # A Naive recursive implementation of MCP(Minimum Cost Path) problem
    rr = len(cost)
    cc = len(cost[0])
    
    print(rr, cc)
    
    # Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C]

    # m = minCost(cost, rr-1, cc-1)
    m = dijkstra(cost)
    print(m)
    
    return m - cost[0][0]

arr = readFile("AoC_Inputs/AoC_2021_d15_input.txt")
print(function(arr))

# 510; too high
