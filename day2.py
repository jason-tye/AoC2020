import utils
import re

vals = utils.readFileLinesString("day2input.txt")

part1ValidCount = 0
part1InvalidCount = 0

part2ValidCount = 0
part2InvalidCount = 0

for idx, val in enumerate(vals):
    pieces = val.split()
    print("Pieces: ", end=" ")
    print(*pieces)

    minmax = pieces[0].split("-")
    print("MinMax: ", end=" ")
    print(*minmax)
    min = int(minmax[0])
    max = int(minmax[1])

    letter = pieces[1][0]

    password = pieces[2]

    matches = re.finditer(letter, password)
    matches_positions = [match.start() for match in matches]
    print("Matches positions len: " + str(len(matches_positions)) + " val: ", end=" ")
    print(*matches_positions)
    if min <= len(matches_positions) <= max:
        part1ValidCount += 1
    else:
        part1InvalidCount += 1

    if ((min-1) in matches_positions) != ((max-1) in matches_positions):
        print("Valid 2")
        part2ValidCount += 1
    else:
        print("invalid 2")
        part2InvalidCount += 1

print("Valid count: " + str(part1ValidCount))
print("Invalid count: " + str(part1InvalidCount))

print("Part 2 Valid count: " + str(part2ValidCount))
print("Part 2 Invalid count: " + str(part2InvalidCount))
