def convertFromStringToList(frequencies):
    if not(isinstance(frequencies, str)):
        return "not a valid input"
    else:#isinstance(frequencies, str)
        # remove white space
        # separate based on ,
        # freq_nospace = frequencies.strip()
        # freqInList = freq_nospace.split(",")
        freqList = frequencies.strip().replace(" ", "").split(",")
        for i in range(len(freqList)):
            freqList[i] = int(freqList[i])
        # print("freqList:", freqList)
        return freqList
# get the problem solved
# using tool(what python can do: for loop), express the logical step
# changing my thought for instruction to computer (breaking it down)
# find model(state)-> understand the domain of the problem -> think about the multiple actions in terms of functions ->
# obj.function(param1)
# function(obj, param1)
#
def addNewFreqency(currentFreq, currentFreTotal):
    print("currentFreq: ",currentFreq)
    if not isinstance(currentFreq, int):
        return "not valid currentFreq value"
    if not isinstance(currentFreTotal, int):
        return "not valid currentFreqTotal value"
    # if the inputs are all valid
    currentFreTotal += currentFreq
    return currentFreTotal

def final_frequency(frequencies):
    currentFreqTotal = 0
    # frequenciesList = [1,1,1]
    currentFreqIndex = 0

    frequenciesList = convertFromStringToList(frequencies)
    while currentFreqIndex < len(frequenciesList):
        currentFreq = frequenciesList[currentFreqIndex]
        currentFreqTotal = addNewFreqency(currentFreq, currentFreqTotal)
        currentFreqIndex += 1
    return currentFreqTotal


if __name__=="__main__":
    # print (final_frequency("+1, +1, +1, +1, +1, -2, -1, -2, -3"))
    print (final_frequency("+1,         +1, +1, +1, +1, -2, -1, -2, -3"))