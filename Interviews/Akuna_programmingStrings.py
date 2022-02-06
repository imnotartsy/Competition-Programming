#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'programmerStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def programmerStrings(s):
    # Write your code here

    expected = {
        'p': 1,
        'r': 3,
        'o': 1,
        'g': 1,
        'a': 1,
        'm': 2,
        'e': 1
    }
    
    first = {
        'p': 0,
        'r': 0,
        'o': 0,
        'g': 0,
        'a': 0,
        'm': 0,
        'e': 0
    }
    
    second = {
        'p': 0,
        'r': 0,
        'o': 0,
        'g': 0,
        'a': 0,
        'm': 0,
        'e': 0
    }
    
    matched = 0
    end = 0    
    for i in range(len(s)):
        if s[i] in first:
            first[s[i]] = first[s[i]] + 1
            if first[s[i]] == expected[s[i]]:
                matched += 1
            if matched == 7:
                print(s[:(i+1)])
                end = i
                break
    
    matched = 0
    start = len(s) - 1
    for i in range(len(s)):
        if s[len(s) - 1 - i] in second:
            second[s[len(s) - 1 - i]] = second[s[len(s) - 1 - i]] + 1
            if second[s[len(s) - 1 - i]] == expected[s[len(s) - 1 - i]]:
                matched += 1
            if matched == 7:
                print(s[len(s) - i - 1:])
                start = len(s) - i - 2
                break
    
    return  start - end
    
    
if __name__ == '__main__':