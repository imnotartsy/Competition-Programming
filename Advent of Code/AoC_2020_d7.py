# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

# import collections
import json

def function(arr):
    # print(arr)


    rules = {}

    for line in arr:
        rules_raw = line.split(" contain ")
        bag = rules_raw[0][:-5]
        contains_raw = [x.replace(' bags', '').replace('.', '') for x in rules_raw[1].split(",")]
        
        contains = {}
        for contain in contains_raw:
            split = contain.split()
            if split[0] == "no":
                contains[split[1]] = 0
            else:
                contains[split[1] + " " + split[2]] = int(split[0])
        print(bag, contains)
        rules[bag] = contains

    print(json.dumps(rules, indent=1))

    while 

arr = readFile("AoC_Inputs/AoC_2020_d7_input.txt")
print(function(arr))