# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import collections
import json
from datetime import datetime



def function(arr):
    # print(arr)

    polymer_raw = arr[0]
    template = []
    insertions = []
    for char in polymer_raw:
        template.append(char)
    print("Template:", template)

    for line in arr[2:]:
        rule = line.split()
        # print(line.split())
        # print(rule[0].split())
        insertions.append([[rule[0][0], rule[0][1]], rule[2]])
    # print(insertions)

    for day in range(40):
        # print(day)
        current_time = datetime.now().strftime("%H:%M:%S")
        print(day, "\t\tCurrent Time =", current_time)
        insert = []
        for i in range(len(insertions)):
            print(i, end=" ")
            insertion = insertions[i]
            # print(insertion)
            for char in range(len(template)-1):
                if template[char] == insertion[0][0] and template[char+1] == insertion[0][1]:
                    insert.append([insertion[1], char+1])
        print()
        print(day, "\t\tCurrent Time (2) =", current_time)        
        

        
        insert.sort(key=lambda x:x[1])
        ## print("Inserts:", insert)
        # for i in range(len(insert)):
        #     template.insert(insert[i][1]+i, insert[i][0])

        # print(template)

        new_template = []
        insert_num = 0
        template_num = 0
        for i in range(len(insert) + len(template)):
        #   print(i, insert_num, template_num)
          if insert_num < len(insert) and (insert[insert_num][1]+ insert_num) == i:
             new_template.append(insert[insert_num][0])
             insert_num += 1
          else:
            new_template.append(template[template_num])
            template_num += 1

        ## print(new_template)
        template = new_template

        print(len(template))

    uniq = set(template)
    counts = collections.defaultdict(int)

    least = float('inf')
    most = 0

    for q in uniq:
        counts[q] = template.count(q)
        if counts[q] > most:
            most = counts[q]
        if counts[q] < least:
            least = counts[q]

    print(json.dumps(counts, indent=1))

    return most - least


arr = readFile("AoC_Inputs/AoC_2021_d14_input.txt")
print(function(arr))