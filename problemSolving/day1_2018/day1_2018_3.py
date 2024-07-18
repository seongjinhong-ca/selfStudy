import functools
def convertFromStringToList(frequencies):
    if not(isinstance(frequencies, str)):
        return "not a valid input"
    else:#isinstance(frequencies, str)
        # remove white space
        # separate based on ","
        return list(map(int, frequencies.strip().replace(" ", "").split(",")))

def convertStringToInt(frequency):
    # print(frequency)
    return int(frequency)
def final_frequency(frequencies):
    # print(convertFromStringToList(frequencies))
    freqMapObj = map(lambda freq : convertStringToInt(freq), frequencies.strip().replace(" ","").split(","))
    freqList = list(freqMapObj)
    # print(freqList)
    currentFreqTotal = functools.reduce(lambda acc, currFreq: acc + currFreq, freqList)
    return currentFreqTotal

#list.map()
# list.map(lambda a : a + 10)

if __name__=="__main__":
    # print (final_frequency("+1, +1, +1, +1, +1, -2, -1, -2, -3"))
    # print("+3: ",int("+3"))
    print (final_frequency("+1,         +1, +1, +1, +1, -2, -1, -2, -3"))
