# input : expense report
# do:
# find the two entries that sum to 2020 and then multiply those two numbers together
# output : [x, y] where x+y == 2020

def findtwoEntriesAddUpTo2020Recursive(expenseList, target, l, r, pair):
    full = 2

    if len(pair) >= full:
        return pair
    else:
        if expenseList[l] + expenseList[r] < target:
            return findtwoEntriesAddUpTo2020Recursive(expenseList, target, l+1, r, pair)
            # print("pair: ",pair)
        elif expenseList[l] + expenseList[r] > target:
            return findtwoEntriesAddUpTo2020Recursive(expenseList, l, r-1, pair)
        else:
            pair = [expenseList[l], expenseList[r]]
            return findtwoEntriesAddUpTo2020Recursive(expenseList, target, l, r, pair)
    # print("pair: ",pair)

def findTwoEntriesAddUpTo2020(expenseList, target):
    if isinstance(expenseList, str):
        expenseList = list(map(lambda item: int(item), expenseList.strip().replace(" ", "").split(",")))
    # twoEntries = []

    # print(expenseList)
    expenseList.sort()
    # print("sortedList: ", expenseList)
    l = 0
    r = len(expenseList) - 1
    pair = []
    findtwoEntriesAddUpTo2020Recursive(expenseList, target, l, r, pair)
    # print(twoEntries)
    # return twoEntries
    return None

if __name__=="__main__":
    expenseReport = [1721, 979, 366, 299, 675, 1456]
    expenseReport2 = "1721, 979, 366, 299, 675, 1456"
    target = 2020
    twoEntries = findTwoEntriesAddUpTo2020(expenseReport2, target)
    print(twoEntries)
