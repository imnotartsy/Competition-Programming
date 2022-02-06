# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import sys

# def min(x, y, z):
#         if (x < y):
#             return x if (x < z) else z
#         else:
#             return y if (y < z) else z

def min(x, y):
    if x < y:
        return x
    else:
        return y

# def minCost(cost, m, n):
#         if (n < 0 or m < 0):
#             return sys.maxsize
#         elif (m == 0 and n == 0):
#             return cost[m][n]
#         else:
#             print("recursing on", m, n, cost[m][n])
#             return cost[m][n] + min( minCost(cost, m-1, n),
#                                     minCost(cost, m, n-1) )

def minCost(cost, m, n):
  
    # Instead of following line, we can use int tc[m + 1][n + 1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(100)] for x in range(100)]
  
    tc[0][0] = cost[0][0]
  
    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
  
    # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
  
    # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min( tc[i-1][j], # tc[i-1][j-1],
                            tc[i][j-1]) + cost[i][j]
  
    return tc[m][n]

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

    m = minCost(cost, rr-1, cc-1)
    
    return m - cost[0][0]

arr = readFile("AoC_Inputs/AoC_2021_d15_input.txt")
print(function(arr))

# 510; too high
