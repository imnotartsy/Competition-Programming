# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import math

def findSeat(arr):
    max_ticket = 0
    tickets = []
    print(arr.sort())
    for ticket in arr:
        y_max = ticket.count('F') + ticket.count('B')
        x_max = ticket.count('L') + ticket.count('R')

        y_upper = pow(2, y_max)-1
        y_lower = 0
        x_upper = pow(2, x_max)-1
        x_lower = 0

        for c in ticket:
            if c == 'R':
                x_lower = math.ceil((x_upper + x_lower)/2) # maybe + 1?
            if c == 'L':
                x_upper = int((x_upper + x_lower)/2)
            if c == 'B':
                y_lower = math.ceil((y_upper + y_lower)/2) # maybe + 1?
            if c == 'F':
                y_upper = int((y_upper + y_lower)/2)

            # print("RANGES:\tX:", [x_lower, x_upper], "\tY:", [y_lower, y_upper])
            
        
        ticket = pow(2, (x_max)) * y_lower + x_lower
        tickets.append(ticket)
        max_ticket = ticket if ticket > max_ticket else max_ticket
    
    tickets_sorted = tickets.sort()
    # print(tickets)
    # print(tickets_sorted)
    for i in range (0, 885-35):
        # print(tickets[i], i+35)
        if tickets[i] != i+35:
            # print("AA", tickets[i], i)
            print(tickets[i] - 1, "is missing")
            break
    print(max_ticket, "is max")
    return max_ticket

    # 877 your answer is too high 

arr = readFile("AoC_Inputs/AoC_2020_d5_input.txt")
print(findSeat(arr))