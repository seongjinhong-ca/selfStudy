# input : string representation of instruction
    # ("L2, R4" == turn left and move forward 2 block
    # and turn right and move forward 4 blocks)
# output : int : how many block away from starting point
# goal : How many blocks away is Easter Bunny HQ?
"""
R2R2R2
(0,0)
where I am, where I'm facing(where I'm looking at)
def move(){
    currentStatus = {N:1, E:2, S: - 3, W: - 4, facing: N}
    verticalLocation = currentStatus.N + currentStatus.S
    horizontalLocation = currentStatus.E + currentStatus.W
    currentPosition = (horizontalLocation, verticalLocation)
}
what we have:
grid -> currentStatus={N:1, E:2, S: - 3, W: - 4, facing: N}
instruction =R2R2R2

turnRight = {N:E, E:S, S:W, W:N}
turnLeft = {N:W, W:S, S:E, E:N}





state : grid, faced
turnRight()
moveForward
turnRight
moveForward
turnRight
moveForward

"""
turnRight = {"N":"E", "E":"S", "S":"W", "W":"N"}
turnLeft = {"N":"W", "W":"S", "S":"E", "E":"N"}

def turn(direction, currentStatus):
    changedStatus = currentStatus.copy()

    if direction == "R":
        changedStatus.facing = turnRight[currentStatus.facing]
    if direction == "L":
        changedStatus.facing = turnLeft[currentStatus.facing]

    return changedStatus

def moveForward(blocks, changedStatus):
    moved = changedStatus.copy()
    # moved[changedStatus.facing] += blocks
    moved[changedStatus.facing] = moved[changedStatus.facing] + blocks
    return moved
def getDistanceOfBlocksFromStartingPoint(instruction, currentStatus):
    numBlocks = 0
    instrunctionsList_noSpace = instruction.strip()
    instrunctionsList= instrunctionsList_noSpace.split(",")
 #["R23435","R2", "R2"]
    #["R2L3R4","R2", "R2"]
    #"R2L3R4,R2,R2"
    for instruction in instrunctionsList:
        #"R2"
        changedStatus = turn(instruction[0], currentStatus)
        currentStatus = moveForward(instruction[1:], changedStatus)

    v_block = abs(currentStatus["N"] - currentStatus["S"])
    h_block = abs(currentStatus["E"] - currentStatus["W"])
    numBlocks = numBlocks + v_block + h_block
    return numBlocks

if __name__=="__main__":
    instruction = input()
    currentStatus = {"N": 0, "E": 0, "S": 0, "W": 0, "facing": "N"}
    blocks = getDistanceOfBlocksFromStartingPoint(instruction, currentStatus)