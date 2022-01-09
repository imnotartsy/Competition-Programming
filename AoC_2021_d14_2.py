# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

from collections import defaultdict
import json


def function(arr):
    polymer_raw = arr[0]
    template = defaultdict(int)
    insertions = {}
    start = polymer_raw[0]
    end = polymer_raw[len(polymer_raw)-1]

    # Prep initial string
    for i in range(len(polymer_raw)-1):
        template[polymer_raw[i] + polymer_raw[i+1]] += 1
    # print(json.dumps(template, indent=1))

    # Prep insertion rules
    for line in arr[2:]:
        rule = line.split()
        insertions[rule[0]] = str(rule[2])
    # print(json.dumps(insertions, indent=1))



    # Computes days
    for day in range(40):
        updates = []

        # Find updates
        for key, item in template.items():
            # print("key", key)
            if item != 0 and key in insertions:
                # Decrease [0] by [3], [1] and [2] increase by [3]
                p1 = key[0] + insertions[key]
                p2 = insertions[key] + key[1]
                updates.append([key, p1, p2, item])

        # Apply updates
        for update in updates:
            template[update[0]] -= update[3]
            template[update[1]] += update[3]
            template[update[2]] += update[3]
        
    # Counts chars
    counts = defaultdict(int)
    counts[start] = 1
    counts[end] = 1
    for key, item in template.items():
        counts[key[0]] += item
        counts[key[1]] += item

    max_char = max(counts, key=counts.get)
    min_char = min(counts, key=counts.get)

    print("Day", day+1, ":")
    
    # Note since every (overlapping) pair is kept in template, every count is double
    print("\tMax char:", max_char, int(counts[max_char]/2))
    print("\tMin char:", min_char, int(counts[min_char]/2))

    # print(json.dumps(counts, indent=1))


    return int((counts[max_char] - counts[min_char])/2)

arr = readFile("AoC_Inputs/AoC_2021_d14_input.txt")
print(function(arr))