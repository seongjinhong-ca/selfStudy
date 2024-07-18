"""
input: string = "1234123111222"
output: integer = 6

input:
sequenceOfDigit = "1234123111222"

class FindTotalSum
properties:
totalSum = 0
l = 0
r = 1


def getTotalSum(s):
    sum = 0
    l = 0
    r = 1

    while l < len(s):
        if l == len(s):
            if s[l] == s[0]:
                sum +=int(s[l])
                return sum

        else: # l < len(s)
            if s[l] == s[r]:
                sum += int(s[l])
                l++
                r++
            else:
                l++
                r++
    return sum

isCurrCharEqualNextchar(currChar, currCharIdx, nextCharIdx){
 if currCharIdx == nextCharIdx:
    totalSum += int(currChar)
    currCharIdx ++
    nextCharIdx ++
else:
    currCharIdx ++
    nextCharIdx ++
}
addToTotalSum(curr, totalSum)

"""

def getTotalSum(s):
    sum = 0
    l = 0
    r = 1

    while l < len(s):
        if l == len(s)-1:
            if s[l] == s[0]:
                sum +=int(s[l])
                return sum
            else:
                return sum

        else: # l < len(s)
            if s[l] == s[r]:
                sum += int(s[l])
                l += 1
                r += 1
            else:
                l += 1
                r += 1
    return sum

print(getTotalSum("11221122"))