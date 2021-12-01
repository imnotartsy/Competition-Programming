def mapAggregate():
    # Num maps
    n = int(input())
    # This is to skip the first blank line
    drop = input()

    ret = {}
    keyCount = {}

    dictionaries = []

    for mapNum in range(n):
        metaString = input()
        meta = metaString.split(' ')

        # Num elems in map
        mapSize = int(meta[0])
        # Num elements in the list
        listSize = int(meta[1])

        currDict = {}

        for elemNum in range(mapSize):
            # Reads in elements in the map
            elems = input()
            # Parses elements read in
            elemsList = elems.split(' ')

            # Processes elements read in
            for elemIdx in range(listSize + 1):

                # If currDict[elemsList[0]], is the first element, it must be the key;
                #   add new entry to current dictionary
                if elemIdx == 0:
                    key = elemsList[0]

                    # Adds key to current dictionary
                    currDict[key] = 0

                    # Dictionary to keep track of current key values across all maps
                    if key in keyCount:
                        keyCount[key] += 1
                    else:
                        keyCount[key] = 1

                # currDict[elemsList[idx]] is not the first element, it must be a value;
                #   add entry sum in current dictionary
                else:
                    currDict[elemsList[0]] += int(elemsList[elemIdx])

        # adds newly created map/dictionaries to list of maps/dictionaries
        dictionaries.append(currDict)

        # This is to skip the blank line between maps
        if mapNum != (n - 1):
            drop = input()


    # Gets duplicate keys and adds the to return dictionary
    for key in keyCount:
        if keyCount[key] > 1:
            ret[key] = 0

    # Iterates through all collected dictionaries and sums entries with duplcate keys
    for dictionary in dictionaries:
        for key in dictionary:
            if key in ret:
                ret[key] += dictionary[key]

b
    for key in ret:
        print(key, ret[key])

mapAggregate()

