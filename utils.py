def readFileLinesInt(fileName):
    f = open(fileName, "r")
    vals = f.read().splitlines()
    print("File preview:", end=" ")
    print(*vals[0:10], end=" ")
    print("...")
    results = list(map(int, vals))
    return results

def readFileLinesString(fileName):
    f = open(fileName, "r")
    vals = f.read().splitlines()
    print("File preview:", end=" ")
    print(*vals[0:10], end=" ")
    print("...")
    return vals