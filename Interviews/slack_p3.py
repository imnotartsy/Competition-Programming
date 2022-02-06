# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, F, M):
    # write your code in Python 3.6

    expected_sum = (len(A)  + F) * M
    A_sum = sum(A)

    # Catch not possible case
    if A_sum + 6*F < expected_sum or A_sum + 1*F > expected_sum:
        return [0]

    else:
        to_add = round((expected_sum - A_sum)/F)
        
        A_sum += to_add * (F-1)
        ret = [to_add] * (F-1)

        ## Add the difference probably lost by rounding
        if expected_sum - A_sum > 0 and expected_sum - A_sum <= 6:
            ret.append(expected_sum - A_sum)
            A_sum += expected_sum - A_sum 
            
        return ret



A = [3, 2, 4, 3]
F = 2
M = 4
print("I: ", A, F, M)
print("E: [6, 6]")
print("O:", solution(A, F, M))

print("******************")

A = [1, 5, 6]
F = 4
M = 3
print("I: ", A, F, M)
print("E: [6, 1, 1, 1]")
print("O:", solution(A, F, M))

print("******************")

A = [6, 6]
F = 8
M = 2
print("I: ", A, F, M)
print("E: [1, 1, 1, 1, 1, 1, 1, 1]")
print("O:", solution(A, F, M))

print("******************")

A = [1, 1]
F = 2
M = 3
print("I: ", A, F, M)
print("E: [0]")
print("O:", solution(A, F, M))

print("******************")

A = [1, 2, 3, 4]
F = 4
M = 6
print("I: ", A, F, M)
print("E: [0]")
print("O:", solution(A, F, M))

print("******************")


A = [6, 1]
F = 1
M = 1
print("I: ", A, F, M)
print("E: [0]")
print("O:", solution(A, F, M))