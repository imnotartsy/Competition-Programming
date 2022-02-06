#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimizeCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numPeople
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY y
#

numPeople = [1, 2, 3, 4, 5, 4, 1, 2, 3, 4, 0, 1, 3, 2, 1, 4]
x = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
y = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]


def distance(x, y, xs, ys):
    distance = 0
    for curr_x, curr_y in zip(xs, ys):
        distance += abs(x - curr_x) + abs(y - curr_y)
    


def minimizeCost_MEAN(numPeople, x, y):

    x_avg = 0
    y_avg = 0
    numPeople_total = 0
    for i in range(len(numPeople)):
        numPeople_total += numPeople[i]
        x_avg += x[i] * numPeople[i]
        y_avg += y[i] * numPeople[i]
    
    print(numPeople_total)
    x_avg /= numPeople_total
    y_avg /= numPeople_total
    
    x_avg = int(x_avg)
    y_avg = int(y_avg)
    print(x_avg)
    print(y_avg)
    
    distance = 0
    for i in range(len(numPeople)):
        temp = abs(x[i] - x_avg) + abs(y[i] - y_avg)
        distance += numPeople[i] * temp

    return int(distance)
    # Write your code here
# if __name__ == '__main__':
    
print(minimizeCost_MEAN(numPeople, x, y))