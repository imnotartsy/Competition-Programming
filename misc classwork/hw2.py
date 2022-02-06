
# Python3 program to count
# inversions in an array
 
 
def getInvCount(arr, n):
 
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
 
    return inv_count
 
 
# Driver Code
# arr = [0, 1, 2, 3, 4, 5]
arr = [0, 0, 0, 0, 0, 0]
n = len(arr)
print("Number of inversions are",
      getInvCount(arr, n))




## Q6

# def swap(A, a, b):
#     temp = A[a]
#     A[a] = A[b]
#     A[b] = temp

# A = [4]
# print(A)

# i = len(A)
# comp_count = 0

# while i > 0:
#     tmp_large = 0
#     for j in range (0, i):
#         comp_count += 1
#         if A[j] > A[tmp_large]:
#             tmp_large = j
#     swap(A, tmp_large, i-1)
#     print(A)
#     i-=1

# print(A)
# print(comp_count)

# # 1 -- 1
# # 2 -- 3
# # 3 -- 6
# # 4 -- 10
# # 5 -- 15
# # 6 -- 21