def convertFromStringToList(frequencies):
    if not(isinstance(frequencies, str)):
        return "not a valid input"
    else:#isinstance(frequencies, str)
        # remove white space
        # separate based on ","
        return map(int, frequencies.strip().replace(" ", "").split(","))

def final_frequency(frequencies):
    currentFreqTotal = 0

    for freq in convertFromStringToList(frequencies):
        currentFreqTotal += freq
    return currentFreqTotal

#list.map()
# list.map(lambda a : a + 10)

if __name__=="__main__":
    # print (final_frequency("+1, +1, +1, +1, +1, -2, -1, -2, -3"))
    print (final_frequency("+1,         +1, +1, +1, +1, -2, -1, -2, -3"))