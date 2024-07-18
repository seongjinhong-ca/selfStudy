"""
input : instruction "R2R2R2"
output : final |distance| from origin

what: human
do: turn, moveForward
- turn (direction, currentDirection) : changedPosition_direction
- moveForward(distance, currentDirection, position) : changedPosition_distance

what to know :
- position : tuple = (x, y)
- currentDirection : String = "N"
- totalDistance = 0
- instruction : String = "R2R2R2"
- sumSignDistanceBasedOnCurrentDirection : map = {"N": "+", "E": "+", "S": "-", "W": "-"}
- rightTurn :map = {"N": "E". "E": "S", "S": "W", "W": "N"}
- leftTurn :map = {"N": "W". "W": "S", "S": "E", "E": "N"}

main(){
    changedPosition = human.turn("R")
    changedPosition = haman.moveForward("2", changedPosition)
    changedPosition = human.turn("R", changedPosition)
    changedPosition = haman.moveForward("2", changedPosition)
    changedPosition = human.turn("R", changedPosition)
    changedPosition = haman.moveForward("2", changedPosition)

    finalDistance_abs = abs(changedPosition[0]) + abs(changedPosition[1])
    return finalDistance_abs
}

class Human{
    position : tuple = (x, y)
    currentDirection : String = "N"
    totalDistance = 0
    instruction : String = "R2R2R2"
    sumSignDistanceBasedOnCurrentDirection : map = {"N": "+", "E": "+", "S": "-", "W": "-"}
    rightTurn :map = {"N": "E". "E": "S", "S": "W", "W": "N"}
    leftTurn :map = {"N": "W". "W": "S", "S": "E", "E": "N"}

    Human(position, currentDirection, distance, instruction)
    currentDirection = currentDirection
    totalDistance = distance
    instruction = instruction


}

def turn (direction, changedPosition) : changedPosition_direction{
 currentDirection = changedPosition[1]
}
def moveForward(distance, changedPosition) : changedPosition_distance{
 position = changedPosition[0]
 currentDirection = changedPosition[1]
 distance = distance
 return

}

def calculateFinalDistance(human, instruction){
  currentDirection = human.getCurrentDirection()
    changedPosition = [human.getPosition(), currentDirection]
    for(i in range(0, len(instructions))):
        turnDir = instruction[i][0]
        distance = int(instruction[i][1])
        changedPosition = human.turn(turnDir, changedPosition)
        changedPosition = haman.moveForward(distance, changedPosition)

    finalDistance_abs = abs(changedPosition[0]) + abs(changedPosition[1])
    return finalDistance_abs
}

main(){
    instruction = input()
    instruction_removeWhiteSpace = instruction.strip()
    instructions = instruction_removeWhiteSpace.split(",")
    human = new Human((0,0), "N", 0, instructions)
    calculateFinalDistance(human, human.getInstruction())

}


"""