# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() # puts the file into an array
        fileObj.close()
        return words

import re

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

f_idx = {
    "byr": 0, 
    "iyr": 1,
    "eyr": 2,
    "hgt": 3,
    "hcl": 4,
    "ecl": 5,
    "pid": 6,
    "cid": 7
}

def binarydiag(arr):
    valid = 0
    passportCount = 1

    passport = [0, 0, 0, 0, 0, 0, 0, 0]
    for line in arr:
        if line == "":
            print("New Passport!")
            passport = [0, 0, 0, 0, 0, 0, 0, 0]
            passportCount += 1
            # print(passport)
        else:
            fields = line.split()
            for field in fields:
                field_name = field.split(":")
                
                # print(field_name)
                # print(f_idx[field_name[0]])
                # print(passport[f_idx[field_name[0]]])
                # print(passport)

                if ((field_name[0] == "byr" and \
                       len(field_name[1]) == 4 and int(field_name[1]) >= 1920 and int(field_name[1]) <= 2002) or \
                        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                    (field_name[0] == "iyr" and \
                        len(field_name[1]) == 4 and int(field_name[1]) >= 2010 and int(field_name[1]) <= 2020) or \
                        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                    (field_name[0] == "eyr" and \
                        len(field_name[1]) == 4 and int(field_name[1]) >= 2020 and int(field_name[1]) <= 2030) or \
                        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                    (field_name[0] == "hgt" and \
                        ((field_name[1][-2:] == "cm" and int(field_name[1][:-2]) >= 150 and int(field_name[1][:-2]) <= 193)) or \
                        ((field_name[1][-2:] == "in" and int(field_name[1][:-2]) >= 59 and int(field_name[1][:-2]) <= 76))) or \
                        # ((bool(re.match("[0-9]*in", field_name[1])) and int(field_name[1]) >= 59  and int(field_name[1]) <= 76)) or \
                        # hgt (Height) - a number followed by either cm or in:
                        # If cm, the number must be at least 150 and at most 193.
                        # If in, the number must be at least 59 and at most 76.
                    (field_name[0] == "hcl" and \
                        (len(field_name[1]) == 7 and bool(re.match("#[0-9,a-f]{6}", field_name[1])))) or \
                        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                    (field_name[0] == "ecl" and \
                        (len(field_name[1]) == 3 and bool(re.match("amb|blu|brn|gry|grn|hzl|oth", field_name[1])))) or \
                        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                    (field_name[0] == "pid" and \
                        (len(field_name[1]) == 9 and bool(re.match("[0-9]{9}", field_name[1]))))):
                    
                    passport[f_idx[field_name[0]]] += 1
                    
                if field_name[0] == "cid":
                    pass
                else:
                    print(field_name)

                


        if sum(passport) ==  8 or (sum(passport) == 7 and passport[f_idx["cid"]] == 0):
            print("\tVALID!", passport)
            valid += 1
            passport = [0, 0, 0, 0, 0, 0, 0, 0]

    print(passportCount)

    return valid
        
        




arr = readFile("AoC_Inputs/AoC_2020_d4_input.txt")
print(binarydiag(arr))
