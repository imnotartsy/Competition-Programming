# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

# from collections import defaultdict
from math import lcm
from functools import reduce

# * I/O Prepper
def function(arr):
    p1 = 0
    p2 = 0

    monkeys = []

    monkey = {
        "items": [],
        "op": "",
        "operand": 0,
        "test": 0,
        "true": 0,
        "false": 0
    }

    for line in arr:
        if line == "":
            monkeys.append(monkey)
            monkey = {
                "items": [],
                "op": "",
                "operand": 0,
                "test": 0,
                "true": 0,
                "false": 0
            }
        else:
            if line[:6] == "Monkey":
                # print(line[7])
                pass
            elif "Starting" in line:
                split_temp = line.split(":")
                if "," in split_temp[1]:
                    items = split_temp[1].replace(",", "").split(" ")
                    for item in items:
                        if item != "":
                            monkey["items"].append(int(item))
                else:
                    monkey["items"] = [int(split_temp[1])]
            elif "Operation" in line:
                split_temp = line.split("=")

                if "*" in split_temp[1]:
                    if "old * old" in split_temp[1]:
                        monkey["op"] = "^"
                    else:
                        num = split_temp[1].split("*")[-1]
                        monkey["op"] = "*"
                        monkey["operand"] = int(num)
                elif "+" in split_temp[1]:
                    num = split_temp[1].split("+")[-1]
                    monkey["op"] = "+"
                    monkey["operand"] = int(num)
                else:
                    print("unknown operation!!")
                    
            elif "Test" in line:
                split_temp = line.split("by")
                monkey["test"] = int(split_temp[-1])
            elif "true" in line:
                split_temp = line.split()
                monkey["true"] = int(split_temp[-1])
            elif "false" in line:
                split_temp = line.split()
                monkey["false"] = int(split_temp[-1])



                    
                
                # print(monkey["op"])
    monkeys.append(monkey) 

    # * Part 1
    counts = [0 for _ in range(len(monkeys))]
    rounds = 20

    for k in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            # print("Monkey", i)
            for _ in range(len(monkey["items"])):
                counts[i] += 1
                worry = monkey["items"].pop(0)
                # print("\tMonkey inspects an item with a worry level of ", worry)
                if monkey["op"] == "*":
                    worry *= monkey["operand"]
                if monkey["op"] == "+":
                    worry += monkey["operand"]
                if monkey["op"] == "^":
                    monkey["operand"] = worry
                    worry *= worry
                # print("\t  Worry level is multiplied by", monkey["operand"], "to", worry)
                worry /=3
                worry = int(worry)
                # print("\t  Monkey gets bored with item. Worry level is divided by 3 to", worry)
                
                if worry % monkey["test"] == 0:
                    # print("\t Current worry level is divisible by ", monkey["test"])
                    # print("\t  Item with worry level", worry, "is thrown to monkey", monkey["true"])
                    monkeys[monkey["true"]]["items"].append(worry)
                else:
                    # print("\t  Current worry level is not divisible by ", monkey["test"])
                    monkeys[monkey["false"]]["items"].append(worry)
                    # print("\t  Item with worry level", worry, "is thrown to monkey", monkey["false"])

        # print("ROUND", k)
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            # print("\tMonkey", i, ":", monkey["items"])
            
    # print(counts)
    m1 = counts.pop()
    m2 = counts.pop()
    p1 = m1 * m2


    
    # Part 2
    counts = [0 for _ in range(len(monkeys))]
    rounds = 10000
    g = reduce(lcm, [monkey["test"] for monkey in monkeys])

    for k in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            # print("Monkey", i)
            for _ in range(len(monkey["items"])):
                counts[i] += 1
                worry = monkey["items"].pop(0)
                # print("\tMonkey inspects an item with a worry level of ", worry)
                if monkey["op"] == "*":
                    worry *= monkey["operand"]
                if monkey["op"] == "+":
                    worry += monkey["operand"]
                if monkey["op"] == "^":
                    monkey["operand"] = worry
                    worry *= worry
                # print("\t  Worry level is multiplied by", monkey["operand"], "to", worry)
                # worry /=3
                # worry = int(worry)
                # print("\t  Monkey gets bored with item. Worry level is divided by 3 to", worry)
                
                if worry % monkey["test"] == 0:
                    # print("\t Current worry level is divisible by ", monkey["test"])
                    # print("\t  Item with worry level", worry, "is thrown to monkey", monkey["true"])
                    # monkeys[monkey["true"]]["items"].append(worry)
                    monkeys[monkey["true"]]["items"].append(worry%g)
                else:
                    # print("\t  Current worry level is not divisible by ", monkey["test"])
                    # monkeys[monkey["false"]]["items"].append(worry)
                    # print("\t  Item with worry level", worry, "is thrown to monkey", monkey["false"])
                    monkeys[monkey["false"]]["items"].append(worry%g)

        # print("ROUND", k)
        # for i in range(len(monkeys)):
        #     monkey = monkeys[i]
            
            # print("\tMonkey", i, ":", monkey["items"])


    # print(counts)
    m1 = counts.pop()
    m2 = counts.pop()
    p2 = m1 * m2


    return p1, p2

arr = readFile("AoC_Inputs/AoC_2022_d11_input.txt")
print(function(arr))