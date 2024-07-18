def updateFloor(i,currentFloor, numsStairs):
    goUp = "("
    if i == len(numsStairs):
        return currentFloor
    if numsStairs[i] == goUp:
        currentFloor += 1
        i += 1
    else: # numsStairs[i] == ")":
        currentFloor -= 1
        i += 1
    return updateFloor(i, currentFloor, numsStairs)
def getCurrentFloor(numsStairs):
    floor = 0
    currentFloor = 0
    finalFloor = updateFloor(floor, currentFloor, numsStairs)
    return finalFloor

if __name__=="__main__":
    numsStairs = input()
    print("final floor : "+ str(getCurrentFloor(numsStairs)))