import utils

vals = utils.readFileLinesInt("day1input.txt")
for idx, val in enumerate(vals):
    found = False
    for idx2, val2 in enumerate(vals[idx+1:-1]):
        if val + val2 == 2020:
            print("Vals: " + str(val) + " and " + str(val2))
            print("Idxs: " +str(idx) + " and " + str(idx2))
            print("Answer: " + str(val * val2))
            found = True
            break
    if found:
        break

for idx, val in enumerate(vals):
    for idx2, val2 in enumerate(vals[idx + 1:-1]):
        for idx3, val3 in enumerate(vals[idx + idx2 + 1:-1]):
            if val + val2 + val3 == 2020:
                print("Vals: " + str(val) + " and " + str(val2) + " and " + str(val3))
                print("Idxs: " + str(idx) + " and " + str(idx2) + " and " + str(idx3))
                print("Answer: " + str(val * val2 * val3))
