# import heapq
from MaxHeap import MaxHeap

input = [5, 13, 19, 11, 15, 5, 17, 7, 23, 11]
heap = MaxHeap(10)
h = []
for value in input:
#     heapq.heappush(h, value)
    heap.insert(value)
# print(h)
heap.Print()




def ParodyPartition(arr):
    mid = 0
    for i in range(0, len(arr)):
        if arr[i]%2 == 0:
            swap(arr, i, mid)
            mid += 1
    return arr


def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp
    return arr

memo = {}
def CombinationsOfN(n, k):
    if k == n or k == 0:
        return 1
    elif [n, k] in memo:
        return memo[[n, k]]
    else:
        combination =  CombinationsOfN((n - 1), (k - 1)) + CombinationsOfN((n - 1), k)
        memo[[n, k]] = combination
        return combination

tests = [[1, 2, 3, 4, 5, 6],
          [2, 4, 2, 5, 3, 6, 4, 1],
          [2, 4, 6, 8, 1, 3, 5],
          [1, 3, 5, 7, 9, 11],
          [2, 4, 6, 8, 10, 12]
        ]

for test in tests:
    print("Input:", test)
    print("Output:", ParodyPartition(test))