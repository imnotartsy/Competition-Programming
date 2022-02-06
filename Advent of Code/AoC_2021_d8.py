# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import json
import difflib

numbers = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

number_strings = {
    0: "abcefg", #6 
    1: "cf",     #2 * - 1
    2: "acdeg",  #5 - missing f (count of 9)
    3: "acdfg",  #5
    4: "bcdf",   #4 * - 4 
    5: "abdfg",  #5
    6: "abdefg", #6 - 6: len == 6 and segment from 1 is missing
    7: "acf",    #3 * - 7
    8: "abcdefg",#7 * - 8
    9: "abcdfg"  #6 - len == 6 and missing e (count of 4)
}

number_seg_count = {
    'a' : 8,
    'b' : 6, # *
    'c' : 8,
    'd' : 7, 
    'e' : 4, # *
    'f' : 9, # *
    'g' : 7
}


#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def function(arrs):
    # strings_numbers = dict((v,k) for k,v in number_strings.items())

    # print(numbers)
    # print(json.dumps(number_strings, indent=1))
    # print(json.dumps(strings_numbers, indent=1))
    # print(arrs)

    ## P1
    ones = 0   #2
    fours = 0  #4
    sevens = 0 #3
    eights = 0 #7

    ## P2
    summ = 0
    for arr in arrs:
        lines = arr.split("|")

        ## Get codes for 0 - 10
        patterns = lines[0].split(" ")[:10]
        ## Get keys for four numbers
        patterns_keys = lines[1].split(" ")[1:]

        
        ## Identify seg_a as the difference between 1 (len 2)and 7 (len 3) which is seg a
        patterns = sorted(patterns, key=len)
        output_list = [li for li in difflib.ndiff(''.join(sorted(patterns[0])), \
                                ''.join(sorted(patterns[1]))) if li[0] != ' ']
        seg_a = output_list[0][2:]

        ## Identify matchable segments by count in 0-9
        number_seg_count = { 'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0}

        ## Get letter counts in patterns
        for line in patterns:
            for char in line:
                number_seg_count[char] += 1

        seg_b = 'a'
        seg_c = 'a'
        seg_e = 'a'
        seg_f = 'a'

        ## Set letters by unique letter counts
        for char in number_seg_count.keys():
            if number_seg_count[char] == 6:
                seg_b = char
            if number_seg_count[char] == 4:
                seg_e = char
            if number_seg_count[char] == 9:
                seg_f = char
            if number_seg_count[char] == 8 and char != seg_a:
                seg_c = char
                

        ## Match keys with length and identified segments
        number = 0
        for i in range(len(patterns_keys)):
            line = patterns_keys[i]
            # zero
            if len(line) == 6 and (seg_c in line) and (seg_e in line): # and (seg_b in line)
                num = 0

            # one
            if len(line) == 2:
                ones += 1
                num = 1

            # two
            if len(line) == 5 and not(seg_b in line) and not(seg_f in line):
                num = 2

            # three
            if len(line) == 5 and not(seg_b in line) and not(seg_e in line):
                num = 3

            # four
            if len(line) == 4:
                fours += 1
                num = 4

            # five
            if len(line) == 5 and (seg_b in line) and (seg_f in line):
                num = 5

            # six
            if len(line) == 6 and not(seg_c in line) and (seg_e in line):
                num = 6

            # seven
            if len(line) == 3:
                sevens += 1
                num = 7

            # eight
            if len(line) == 7:
                eights += 1
                num = 8

            # nine
            if len(line) == 6 and not(seg_e in line) and (seg_b in line):
                num = 9

            number = number*10 + num
            

        # print(number)
        summ += number

   
    ## P1
    # return ones + fours + sevens + eights
    ## P2
    return summ

            

arr = readFile("AoC_Inputs/AoC_2021_d8_input.txt")
print(function(arr))