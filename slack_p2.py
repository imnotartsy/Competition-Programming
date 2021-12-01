# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import string

def solution(T, R):
    # write your code in Python 3.6
    scores = {}

    if len(T) > 0:

        if str.isalpha(T[0][-1]):
            base_len = len(T[0][:-1].rstrip(string.digits))
        else:
            base_len = len(T[0].rstrip(string.digits))


    for score in range(len(T)):
        if str.isalpha(T[score][-1]):
            q = T[score][base_len:base_len+1]
        else:
            q = T[score][base_len:]

        # q in scores; true
        if q in scores:
            if not(scores[q] and R[score] == "OK"):
                scores[q] = False
        else:
            scores[q] = R[score] == "OK"

    grade = 0
    for val in scores.keys():
        if scores[val]:
            grade += 1

    return int(100*grade/len(scores.keys()))

        
            




# keep running scores in a dictionary labeled with case
# iterate through for score if all pass

T = ["test1a", "test2", "test1b", "test1c", "test3"]
R = ["Wrong answer", "OK", "Runtime error", "OK", "Time limit exceeded"]
print("I:", T, R)
print("E: 33")
print("O:", solution(T, R))

print("*****************")


T = ["codelily1", "codelily3", "codelily2", "codelily4a", "codelily4b"]
R = ["Wrong answer", "OK", "OK", "Runtime error", "OK"]
print("I:", T, R)
print("E: 50")
print("O:", solution(T, R))

print("*****************")