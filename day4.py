import utils
import re

vals = utils.readFileLinesString("day4input.txt")


fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid = 0
invalid = 0
fieldsToMatch = fields.copy()
for idx, val in enumerate(vals):
    print("Row: " + val)
    if len(val) == 0:
        if len(fieldsToMatch) == 0:
            valid +=1
        else:
            invalid +=1
        fieldsToMatch = fields.copy()
        continue

    rowVals = val.split(" ")
    for el in rowVals:
        keyVal = el.split(":")
        if keyVal[0] == "byr":
            try:
                if (len(keyVal[1]) == 4) and (1920<= int(keyVal[1])<= 2002):
                    fieldsToMatch.remove(keyVal[0])
                else:
                    print("did not pass validation on: " + el)
            except:
                print("failed on: " + el)
                pass
        elif keyVal[0] == "iyr":
            try:
                if (len(keyVal[1]) == 4) and (2010 <= int(keyVal[1]) <= 2020):
                    fieldsToMatch.remove(keyVal[0])
                else:
                    print("did not pass validation on: " + el)
            except:
                print("failed on: " + el)
                pass
        elif keyVal[0] == "eyr":
            try:
                if (len(keyVal[1]) == 4) and (2020 <= int(keyVal[1]) <= 2030):
                    fieldsToMatch.remove(keyVal[0])
                else:
                    print("did not pass validation on: " + el)
            except:
                print("failed on: " + el)
                pass
        elif keyVal[0] == "hgt":
            try:
                end = keyVal[1][-2:]
                if (end == "cm") and (150 <= int(keyVal[1][:-2]) <= 193):
                    fieldsToMatch.remove(keyVal[0])
                elif (end == "in") and (59 <= int(keyVal[1][:-2]) <= 76):
                    fieldsToMatch.remove(keyVal[0])
                else:
                    print("did not pass validation on: " + el)
            except:
                print("failed on: " + el)
                pass
        elif keyVal[0] == "ecl":
            try:
                idx = ecolors.index(keyVal[1])
                if idx >=0:
                    fieldsToMatch.remove(keyVal[0])
                else:
                    print("did not pass validation on: " + el)
            except:
                print("failed on: " + el)
                pass
        elif keyVal[0] == "hcl":
            try:
                if (keyVal[1][0] == "#") and (re.match('[a-fA-f0-9_]', keyVal[1][-6:])):
                    fieldsToMatch.remove(keyVal[0])
                else:
                    print("did not pass validation on: " + el)
            except:
                print("failed on: " + el)
                pass
        elif keyVal[0] == "pid":
            try:
                num = int(keyVal[1])
                if len(keyVal[1]) == 9:
                    fieldsToMatch.remove(keyVal[0])
                else:
                    print("did not pass validation on: " + el)
            except:
                print("failed on: " + el)
                pass

if len(fieldsToMatch) == 0:
    valid +=1
else:
    invalid +=1

print("Valid count: " + str(valid))
print("Invalid count: " + str(invalid))