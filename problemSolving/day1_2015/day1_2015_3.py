
def checkNotValidType(stringInput):
    return not isinstance(stringInput, str)
def getCurrnetFloor(numsStairs):
    if checkNotValidType(numsStairs):
        print("should be the list of characters")

    floor = 0
    goUp = "("
    goDown = ")"

    for stair in numsStairs:
        if stair == goUp:
            floor = floor + 1
        elif stair == goDown:
            floor = floor - 1
    return floor

if __name__ == "__main__":
    numsStairs = input()
    floor = getCurrnetFloor(numsStairs)
    print(floor)
