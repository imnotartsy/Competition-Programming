numTestCases = int(input())
print("Cases:", numTestCases)
for case in range(numTestCases):
    houses = int(input())
    bins = str(input())
    print("Problem:", case, houses, bins)
    
    distance = 0
    
    for i in range(houses):
        print("Curr house:", i, "has can?", True if bins[i] == '1' else False)
        
        if bins[i] == '1':
            print("\tBin for", i, "found at", i)
            
        else:
            j = i - 1
            k = i + 1
            found = False

            while not(found):
                print("\t\tHouse", i, "-- Checking: ", j, "and", k)
                if j >= 0:
                    if bins[j] == '1':
                        print("\tBin for", i, "found at", j, "distance", abs(j-i))
                        found = True
                        distance += abs(j-i)
                    else:
                        j-= 1
                else:
                    print("\t\tLower bound out of range")
                    
                if k < houses:
                    if bins[k] == '1':
                        print("\tBin for", i, "found at", k, "distance:", abs(i-k))
                        found = True
                        distance += abs(i-k)
                    else:
                        k+= 1
                else:
                    print("\t\tUpper bound out of range")

                if j < 0 and k >= houses - 1:
                    print("Out of range")
                    break
                    
                
                
    print("Case #", case, ": ", distance)
                