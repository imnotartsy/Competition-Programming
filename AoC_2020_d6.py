# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import collections 

def function1(arr):
    # print(arr)
    groups = []
    group = []
    for line in arr:
        if line == "":
            groups.append(len({e for l in group for e in l}))
            group = []
        for char in line:
            group.append(char)
    groups.append(len({e for l in group for e in l}))

    print(sum(groups))


def function2(arr):

    groups = [] ## Could reduce space complexity by making this just an intger and adding
    ## groups represent the amount of questions everyone in each group said yes to

    group = collections.defaultdict(int)
    ## group represents the amount of yeses 
    group_size = 0


    for line in arr:

        ## New group case
        if line == "":
            q_count = 0
            for k,v in group.items():
                ## print("%s - %s" % (str(k), str(v)))

                ## if the amount of yes's is equal to the group size (everyone says yes)
                if v == group_size:
                    q_count += 1
            groups.append(q_count)

            ## Reset 
            print("group size:", group_size)
            print("new group!")
            group = collections.defaultdict(int)
            group_size = 0
            
        else:
            group_size += 1
            for char in line:
                group[char] += 1

    ## New group case for last group (without new line at the end of file)
    q_count = 0
    for char in group.keys():
        if group[char] == group_size:
            q_count += 1
    groups.append(q_count)

    print(sum(groups))
    print(groups)

arr = readFile("AoC_Inputs/AoC_2020_d6_input.txt")
print(function2(arr))