# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words


def binarydiag(board):
    cols = len(board[0])
    rows = len(board)
    print("i_max/cols:", cols)
    print("j_max/rows:", rows) 


    g_bin = ""
    # For each digit
    for i in range(cols):
        s0 = 0
        # Iterate through row
        for j in range(len(board)):
            if board[j][i] == '0':
                s0 += 1
        g_bin += '0' if s0 > rows - s0 else '1'

    print("Gamma - Bin:\t", g_bin)
    gb_dec = int(g_bin, base=2)
    print("Gamma - Dec:\t", gb_dec)

    # gamma + epsilon = 2^cols - 1
    max = pow(2, cols) -1
    es_dec = max - gb_dec
    print("Epsilon - Dec:\t", es_dec)

    # Pad with zeros for consistency
    es_bin = "0" * (cols - len(str(bin(es_dec))[2:]))+ str(bin(es_dec))[2:]
    print("Epsilon - Bin:\t", es_bin)



    ## ** P2 ** 

    # Sets for elimination
    oxy_set = set(board)
    co2_set = set(board)

    # For each letter
    for i in range(cols):

        # Get Counts for each elem set 
        s0 = 0
        for string in oxy_set:
            if string[i] == '0':
                s0 += 1
        oxy_check = '1' if s0 <= len(oxy_set) - s0 else '0'

        s0 = 0
        for string in co2_set:
            if string[i] == '0':
                s0 += 1
        co2_check = '0' if s0 <= len(co2_set) - s0 else '1'
    
        # Eliminate based on checks
        for j in range(rows):
            if board[j][i] != oxy_check and board[j] in oxy_set and len(oxy_set) > 1:
                oxy_set.remove(board[j])

            if board[j][i] != co2_check and board[j] in co2_set and len(co2_set) > 1:
                co2_set.remove(board[j])
                
            
    (oxy_bin, ) = oxy_set
    print("Oxy - Bin:\t", oxy_bin)
    oxy_dec = str(int(oxy_bin, base=2))
    print("Oxy - Dec:\t", oxy_dec)

    (co2_bin, ) = co2_set
    print("CO2 - Bin:\t", co2_bin)
    co2_dec = str(int(co2_bin, base=2))
    print("Co2 - Dec:\t", co2_dec)



    # p1
    # return es_dec * gb_dec

    return int(oxy_dec) * int(co2_dec)


arr = readFile("AoC_2021_d3_input.txt")
print(binarydiag(arr))
