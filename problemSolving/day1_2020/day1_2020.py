# input : expense report
# do:
# find the two entries that sum to 2020 and then multiply those two numbers together
# output : [x, y] where x+y == 2020

def findTwoEntriesAddUpTo2020(expenseList):
    # twoEntries = []
    target = 2020
    expenseList.sort()
    # print("sortedList: ", expenseList)
    l = 0
    r = len(expenseList) - 1
    while l < r:
        twoEntriesSum = expenseList[l] + expenseList[r]
        if twoEntriesSum < target:
            l += 1
        elif twoEntriesSum > target:
            r -= 1
        else: # sortedList[l] + sortedList[r] == target
            # twoEntries = [expenseList[l], expenseList[r]]
            return [expenseList[l], expenseList[r]]
    # print(twoEntries)
    # return twoEntries
    return None

if __name__=="__main__":
    expenseReport = [1721, 979, 366, 299, 675, 1456]
    # print("expense:",expenseReport.sort())
    twoEntries = findTwoEntriesAddUpTo2020(expenseReport)
    print(twoEntries)