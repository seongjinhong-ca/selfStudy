
def getCurrnetFloor(numsStairs):
    if not isinstance(numsStairs, str):
        print("should be the list of characters")

    floor = 0

    for stair in numsStairs:
        if stair == "(":
            floor = floor + 1
        elif stair == ")":
            floor = floor - 1
    return floor

if __name__ == "__main__":
    numsStairs = input()
    floor = getCurrnetFloor(numsStairs)
    print(floor)
