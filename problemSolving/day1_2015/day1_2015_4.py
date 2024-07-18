#while loop

def getCurrentFloor(numsStairs):
    floor = 0
    currentStair = 0
    goUp = "("
    goDown = ")"
    while(currentStair < len(numsStairs)):
        if numsStairs[currentStair] == goUp:
            floor += 1
        else: #numsStairs[currentStair] == goDown
            floor -= 1
        currentStair += 1
    return floor

if __name__=="__main__":
    numsStairs = input()
    print("current Floor is " + str(getCurrentFloor(numsStairs)))
    print(float(int(str(getCurrentFloor(numsStairs)))))

