# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    castles = 0
    # Main 
    for seg in range(len(A)):

        # left edge
        if seg == 0:
            castles += 1

        # right edge
        elif seg == len(A)-1 and len(A) > 2:
            castles += 1

        elif A[seg-1] < A[seg] and A[seg] < A[seg+1]:
            castles += 1

        elif A[seg-1] > A[seg] and A[seg] > A[seg+1]:
            castles += 1

    return castles
        



A = [2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]
print("I:", A)
print("E: 4")
print("O:", solution(A))

print("**********")

A = [-3, -3]
print("I:", A)
print("E: 1")
print("O:", solution(A))

