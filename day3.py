import utils

vals = utils.readFileLinesString("day3input.txt")

modMax = len(vals[0])
answer = 1
sidewaysMotionArray = [1,3,5,7,1]

for runIdx, sidewaysMotion in enumerate(sidewaysMotionArray):
    skipRow = (runIdx == 4)
    horizontalIndex = 0
    treeCount = 0
    nonTreeCount = 0

    for idx, val in enumerate(vals):
        if skipRow and (idx % 2 == 1):
            continue

        if val[horizontalIndex] == "#":
            treeCount += 1
        else:
            nonTreeCount += 1

        horizontalIndex += sidewaysMotion
        horizontalIndex = horizontalIndex % modMax

    answer *= treeCount

    print("Tree count: " + str(treeCount))
    print("Non treee count: " + str(nonTreeCount))

print("Answer count: " + str(answer))