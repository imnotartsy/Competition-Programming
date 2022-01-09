# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

# * Helper function to return the product of a list
def prod(l):
    p = 1
    for num in l:
        p *= num
    return p


## Literal helper functions

# * Recursive function to concatenate all of the 4/5 bit data packets
# * Expects a "binary" string
# * Returns an struct/array where:
# *   - first element: the binary concatenated string
# *   - second element: the length of all of th data packets
## (This could have also been done by ceil(len(binary) % 16))*16)
def concatenate(binary):
    next = int(binary[0], 2)
    a = binary[1:5]

    if next == 1:
        c = concatenate(binary[5:])
        return [a + c[0], 5 + c[1]]
    else:
        return [a, 5]

# * Convert output of concatenate into a list of literal and value length
# * Expects a "binary" string s
# * Returns an struct/array where:
# *   - first element: the decimal value of the string s
# *   - second element: the length of all of th data packets
def literal(s):
    concat = concatenate(s)
    return [int(concat[0], 2), concat[1]]



# *  Decode is a recursive function expecting an input of a 'binary' string
# * Decode returns a 'struct'(array) where:
# *    - first element: the ongoing result
# *    - second element: current spot in the string
# *    - third element: running sum of version numbers
def decode(binary):
    # print("\nDECODE:", binary)
    version = int(binary[0:3], 2)
    id      = int(binary[3:6], 2)

    ## Literal case
    if id == 4:
        l = literal(binary[6:]) # l[0] is the decoded literal value

        ## Adds 6 for version and id lengths
        l[1] += 6

        ## Adds version to follow recursion template
        l.append(version)
        return l


    ## Operand Packet
    else:
        len_type = int(binary[6], 2)

        ## Keeps track of nested version sum
        version_sum = 0

        ## Returns of nested packets
        nums = []

        ## Len Type == 0 is based on the amount of chars in sub packets; len(L) == 15
        if len_type == 0:
            l = int(binary[7:22], 2)

            ## Current length read
            curr_l = 0

            ## Start decoding sub packets
            start = 22
            while curr_l != l:
                p = decode(binary[start:])

                ## Keep track of characters red
                curr_l += p[1]

                ## Add operand to nums
                nums.append(p[0])
                ## Increment where to start decoding the next packet
                start += p[1]
                ## Keep track of the version sum
                version_sum += p[2]


        ## Len Type == 1 is based on amount of sub packets; len(L) = 11
        elif len_type == 1:
            l = int(binary[7:18], 2)

            ## Start decoding sub packets
            start = 18
            for _ in range(l):
                p = decode(binary[start:])

                ## Add operand to nums
                nums.append(p[0])
                ## Increment where to start decoding the next packet
                start += p[1]
                ## Keep track of the version sum
                version_sum += p[2]

        # print("Nums!", nums)
        ## Uncomment this and remove everything the if statements below to see
        ## the nesting structure of the packets

        # print("** RUNNING VERSION SUM:", version_sum + version)

        ## P2 - Operations (Note there's some funky dynamic type stuff)
        ## Should have used a dictionary switch statement
        if id == 0: nums = sum(nums)
        if id == 1: nums = prod(nums)
        if id == 2: nums = min(nums)
        if id == 3: nums = max(nums)
        if id == 5: nums = 1 if nums[0] > nums[1] else 0
        if id == 6: nums = 1 if nums[0] < nums[1] else 0
        if id == 7: nums = 1 if nums[0] == nums[1] else 0
        
        # print("** RUNNING RESULT:", nums)
        return [nums, start, version_sum + version]


# * I/O Prepper
def function(arr):
    line = arr[0]

    ## Convert hex input into binary
    binary = str(bin(int(line, 16)))[2:]

    ## Prep input because of leading zeros
    zero = (4 - (len(binary) % 4)) * '0' if len(binary) % 4 != 0 else '' # leading zero case for first digit < 8
    zero = "0000" + zero if line[0] == '0' else zero # leading zero case for first digit 0
    binary = "" +  zero + binary
    

    ## Start decoding the nested packets    
    p = decode(binary)

    ## Prints output
    # P1
    print("VERSION NUMBER TOTAL SUM:", p[2])
    # P2
    print("RESULT", p[0])

    return p


arr = readFile("AoC_Inputs/AoC_2021_d16_input.txt")
print(function(arr))

